import json
from enum import Enum
from typing import List

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from esi.decorators import token_required
from esi.models import Token
from ninja import Router
from pydantic import BaseModel

from authentication import AuthBearer
from eveonline.models import EveCharacter, EvePrimaryCharacter
from eveonline.scopes import (
    ADVANCED_SCOPES,
    BASIC_SCOPES,
    CEO_SCOPES,
    PUBLIC_SCOPES,
)

router = Router(tags=["Characters"])


class TokenType(Enum):
    CEO = "CEO"
    BASIC = "Basic"
    ADVANCED = "Advanced"


class BasicCharacterResponse(BaseModel):
    character_id: int
    character_name: str


class CharacterResponse(BasicCharacterResponse):
    skills: dict

@router.get(
    "",
    summary="Get characters",
    auth=AuthBearer(),
    response=List[BasicCharacterResponse],
)
def get_characters(request):
    characters = EveCharacter.objects.filter(token__user=request.user)
    response = []
    for character in characters:
        response.append(
            {
                "character_id": character.character_id,
                "character_name": character.character_name,
            }
        )
    return response


@router.get(
    "/{int:character_id}",
    summary="Get character by ID",
    auth=AuthBearer(),
    response=CharacterResponse,
)
def get_character_by_id(request, character_id: int):
    character = EveCharacter.objects.get(character_id=character_id)

    if (
        request.user.has_perm("eveonline.view_evecharacter")
        or Token.objects.filter(
            user=request.user, character_id=character_id
        ).exists()
    ):
        return {
            "character_id": character.character_id,
            "character_name": character.character_name,
            "skills": json.loads(character.skills_json),
        }

    return 403, "You do not have permission to view this character."


@router.get(
    "/primary",
    summary="Get primary character",
    auth=AuthBearer(),
    response=BasicCharacterResponse,
)
def get_primary_character(request):
    if not EvePrimaryCharacter.objects.filter(
        character__token__user=request.user
    ).exists():
        return 404, "Primary character not found."

    character = EvePrimaryCharacter.objects.get(
        character__token__user=request.user
    ).character
    return {
        "character_id": character.character_id,
        "character_name": character.character_name,
    }


@router.get("/primary/add", summary="Add primary character using EVE Online SSO")
def add_primary_character(request, redirect_url: str):
    request.session["redirect_url"] = redirect_url
    scopes = PUBLIC_SCOPES

    @login_required()
    @token_required(scopes=scopes, new=True)
    def wrapped(request, token):
        if EveCharacter.objects.filter(
            character_id=token.character_id
        ).exists():
            character = EveCharacter.objects.get(
                character_id=token.character_id
            )
            if character.token is None:
                character.token = token
                character.save()
        else:
            character = EveCharacter.objects.create(
                character_id=token.character_id,
                character_name=token.character_name,
                token=token,
            )
        EvePrimaryCharacter.objects.create(character=character)
        return redirect(request.session["redirect_url"])

    return wrapped(request)  # pylint: disable=no-value-for-parameter


@router.get("/add", summary="Add character using EVE Online SSO")
def add_character(request, redirect_url: str, token_type: TokenType):
    request.session["redirect_url"] = redirect_url
    scopes = None
    match token_type:
        case TokenType.BASIC:
            scopes = BASIC_SCOPES
        case TokenType.ADVANCED:
            scopes = ADVANCED_SCOPES
        case TokenType.CEO:
            scopes = CEO_SCOPES

    @login_required()
    @token_required(scopes=scopes, new=True)
    def wrapped(request, token):
        if EveCharacter.objects.filter(
            character_id=token.character_id
        ).exists():
            character = EveCharacter.objects.get(
                character_id=token.character_id
            )
            character.token = token
            character.save()
        else:
            character = EveCharacter.objects.create(
                character_id=token.character_id,
                character_name=token.character_name,
                token=token,
            )
        return redirect(request.session["redirect_url"])

    return wrapped(request)  # pylint: disable=no-value-for-parameter


