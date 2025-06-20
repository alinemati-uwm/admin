from django.urls import reverse_lazy
import os
from pathlib import Path
from urllib.parse import urlparse
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "SECRET_KEY", "django-insecure-mt50)h#xlucwckt3scq^$f^h@c-_mrl036mj4!0lnbyhyt0d%^")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "True") == "True"

ALLOWED_HOSTS = os.environ.get(
    "ALLOWED_HOSTS", "localhost,127.0.0.1").split(',')


# Application definition

INSTALLED_APPS = [
    "modeltranslation",
    'unfold.contrib.import_export',
    "unfold",  # before django.contrib.admin
    'import_export',
    # 'multi_captcha_admin',
    'django_advanced_password_validation',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'crm',
    'education',
    "cache_cleaner",
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    "unfold.contrib.guardian",  # optional, if django-guardian package is used
    # optional, if django-simple-history package is used
    "unfold.contrib.simple_history",

    "simple_history",
    #   'captcha',
]


# Multi-Captcha Admin settings
# This is a custom app for handling multiple captcha engines in the admin interface.
MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
}


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "elevate.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "elevate.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # replace with your database name
        'NAME': os.environ.get('DB_NAME', 'elevate_db'),
        # replace with your database user
        'USER': os.environ.get('DB_USER', 'eval_user'),
        # replace with your database password
        'PASSWORD': os.environ.get('DB_PASSWORD', 'eval_password'),
        # or your PostgreSQL host
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        # Docker PostgreSQL port
        'PORT': os.environ.get('DB_PORT', '5436'),
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
    {
        'NAME': 'django_advanced_password_validation.advanced_password_validation.ContainsDigitsValidator',
        'OPTIONS': {
            'min_digits': 1
        }
    },
    {
        'NAME': 'django_advanced_password_validation.advanced_password_validation.ContainsUppercaseValidator',
        'OPTIONS': {
            'min_uppercase': 1
        }
    },
    {
        'NAME': 'django_advanced_password_validation.advanced_password_validation.ContainsLowercaseValidator',
        'OPTIONS': {
            'min_lowercase': 1
        }
    },
    {
        'NAME': 'django_advanced_password_validation.advanced_password_validation.ContainsSpecialCharactersValidator',
        'OPTIONS': {
            'min_characters': 1
        }
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en"


USE_I18N = True

LANGUAGES = (
    ("de", _("German")),
    ("en", _("English")),
    ("fa", _("Persian")),
    ("fr", _("French")),
    ("it", _("Italian")),
    ("es", _("Spanish")),
)

# Locale paths for translation files
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# Modeltranslation settings
MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'en'


TIME_ZONE = "UTC"


USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"
# The URL prefix for static files. This is used to serve static files in development and production.
# STATIC_ROOT = os.path.join(BASE_DIR, "static")


# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


UNFOLD = {
    "SITE_TITLE": "Nemati AI",
    "SITE_HEADER": "Nemati AI Admin",
    "SITE_SUBHEADER": "Elevate your business with Nemati AI",
    "SITE_FOOTER": "Nemati AI © 2024",
    # "SITE_LOGO": "https://nemati.ai/images/common/logo.svg",
    "SITE_DROPDOWN": [
        {
            "icon": "diamond",
            "title": _("Nemati AI"),
            "link": "https://nemati.ai",
        },
        {
            "icon": "diamond",
            "title": _("Dev Nemati ai"),
            "link": "https://dev.nemati.ai",
            # "link": reverse_lazy("admin:index"),

        },
    ],
    "SIDEBAR": {
        "show_search": False,  # Search in applications and models names
        "show_all_applications": False,  # Dropdown with all applications and models
        "navigation": [
            {
                "title": _("Navigation"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "dashboard",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:index"),
                        "badge": "Admin",
                        "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Users"),
                        "icon": "people",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                ],
            },
        ],
    },
    "SHOW_LANGUAGES": True,

    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "de": "🇩🇪",
                "fr": "🇫🇷",
                "es": "🇪🇸",
                "it": "🇮🇹",
                "fa": "🇮🇷",
            },
        },
    },


}
