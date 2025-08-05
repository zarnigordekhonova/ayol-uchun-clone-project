import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = ["*"]


DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LOCAL_APPS = [
    "apps.common",
    "apps.users",
    "apps.news",
    "apps.courses",
    "apps.text_services"
]

EXTERNAL_APPS = ["daphne", "jazzmin", "rest_framework", "drf_yasg"]

INSTALLED_APPS = LOCAL_APPS + EXTERNAL_APPS + DJANGO_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI_APPLICATION = "core.wsgi.application"
ASGI_APPLICATION = "core.asgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
        "ATOMIC_REQUESTS": True,
    }
}




# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = (BASE_DIR / "static",)

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# CACHES
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
REDIS_DB = os.getenv("REDIS_DB", 0)

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": f"{REDIS_HOST}:{REDIS_PORT}",
        "KEY_PREFIX": "boilerplate",  # todo: you must change this with your project name or something else
    }
}


# CELERY CONFIGURATION
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", f"redis://{REDIS_HOST}:{REDIS_PORT}")
CELERY_RESULT_BACKEND = os.getenv(
    "CELERY_RESULT_BACKEND", f"redis://{REDIS_HOST}:{REDIS_PORT}"
)

CELERY_TIMEZONE = "Asia/Tashkent"

CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60


# CYPHER CONFIGURATION
# AES
AES_KEY = os.getenv("AES_KEY", "")


# RECAPTCHA
RECAPTCHA_PUBLIC_KEY = os.getenv("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.getenv("RECAPTCHA_PRIVATE_KEY")

from core.jazzmin_conf import JAZZMIN_SETTINGS # noqa