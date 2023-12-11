"""
Django settings for tools project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from app.settings_common import *  # noqa
from app.settings_celery import *  # noqa
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOSTS", "*")]
CSRF_TRUSTED_ORIGINS = [os.environ.get("CSRF_TRUSTED_ORIGINS", "*")]

BROKER_URL = os.environ.get("BROKER_URL", "redis://localhost:6379/1")
CELERYBEAT_SCHEDULER = "django_celery_beat.schedulers.DatabaseScheduler"

# DISCORD
DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN", "")
DISCORD_CLIENT_ID = os.environ.get("DISCORD_CLIENT_ID", "")
DISCORD_CLIENT_SECRET = os.environ.get("DISCORD_CLIENT_SECRET", "")
DISCORD_REDIRECT_URL = os.environ.get("DISCORD_REDIRECT_URL", "")

# ESI
ESI_SSO_CLIENT_ID = os.environ.get("ESI_SSO_CLIENT_ID", "")
ESI_SSO_CLIENT_SECRET = os.environ.get("ESI_SSO_CLIENT_SECRET", "")
ESI_SSO_CALLBACK_URL = os.environ.get("ESI_SSO_CALLBACK_URL", "")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("DB_NAME", "minmatar"),
        "USER": os.environ.get("DB_USER", "root"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "example"),
        "HOST": os.environ.get("DB_HOST", "127.0.01"),
        "PORT": os.environ.get("DB_PORT", "3306"),
        "OPTIONS": {"charset": "utf8mb4"},
    },
}

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

LOGIN_URL = "/oauth2/login"
LOGOUT_REDIRECT_URL = "/oauth2/login"

# Add these new lines
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "staticfiles"),
)

STATIC_ROOT = os.path.join(
    BASE_DIR,
    "static",
)
