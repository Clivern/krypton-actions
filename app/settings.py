# Copyright 2019 Clivern
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import time
from urllib.parse import urlparse

# Third Party Library
from dotenv import load_dotenv
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


if os.getenv("APP_ENVIRONMENT", "") != "heroku":
    if os.path.exists(os.path.join(BASE_DIR, ".env")):
        load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))
    else:
        load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env.example"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ")lj2@3@y&5ofgoekbt2c-4$$w2bedn@-(hr&i^!#%wype&wp6d" if os.getenv("APP_KEY", "") == "" else os.getenv("APP_KEY", "")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("APP_DEBUG", "false").lower() == "true"

ALLOWED_HOSTS = [] if (os.getenv("ALLOWED_HOSTS", "") == "") else os.getenv("ALLOWED_HOSTS", "").split(",")


# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'app.middleware.correlation.Correlation',
    'app.middleware.logging.Logging',
    'app.middleware.errors.Errors'
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + "/themes/child",
            BASE_DIR + "/themes/" + os.getenv("CURRENT_THEME", "default"),
            BASE_DIR + "/themes/default",
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Email Settings
# https://docs.djangoproject.com/en/2.0/topics/email/
if os.getenv("EMAIL_HOST", None) is not None:
    EMAIL_HOST = os.getenv("EMAIL_HOST", "localhost")

if os.getenv("EMAIL_PORT", None) is not None:
    EMAIL_PORT = os.getenv("EMAIL_PORT", 25)

if os.getenv("EMAIL_HOST_USER", None) is not None:
    EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")

if os.getenv("EMAIL_HOST_PASSWORD", None) is not None:
    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")

if os.getenv("EMAIL_USE_TLS", None) is not None:
    EMAIL_USE_TLS = True if os.getenv("EMAIL_USE_TLS", "false").lower() == "true" else False

if os.getenv("EMAIL_USE_SSL", None) is not None:
    EMAIL_USE_SSL = True if os.getenv("EMAIL_USE_SSL", "false").lower() == "true" else False

if os.getenv("EMAIL_TIMEOUT", None) is not None:
    EMAIL_TIMEOUT = os.getenv("EMAIL_TIMEOUT", None)

if os.getenv("EMAIL_SSL_KEYFILE", None) is not None and os.path.isfile(BASE_DIR + os.getenv("EMAIL_SSL_KEYFILE", "")):
    EMAIL_SSL_KEYFILE = BASE_DIR + os.getenv("EMAIL_SSL_KEYFILE", "")

if os.getenv("EMAIL_SSL_CERTFILE", None) is not None and os.path.isfile(BASE_DIR + os.getenv("EMAIL_SSL_CERTFILE", "")):
    EMAIL_SSL_CERTFILE = BASE_DIR + os.getenv("EMAIL_SSL_CERTFILE", "")

if os.getenv("EMAIL_BACKEND", None) is not None and os.getenv("EMAIL_BACKEND", None) in ["smtp", "console", "filebased"]:
    EMAIL_BACKEND = "django.core.mail.backends." + os.getenv("EMAIL_BACKEND", "smtp") + ".EmailBackend"
    if os.getenv("EMAIL_BACKEND", None) == "filebased":
        EMAIL_FILE_PATH = BASE_DIR + "/storage/mails"


WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

db_connection = os.getenv("DB_CONNECTION")
db_name = os.getenv("DB_DATABASE")
db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

if os.getenv("DATABASE_URL", "") != "":
    url_parts = urlparse(os.getenv("DATABASE_URL", ""))
    db_connection = url_parts.scheme
    db_name = url_parts.path.lstrip("/")
    db_username = url_parts.username
    db_password = url_parts.password
    db_host = url_parts.hostname
    db_port = url_parts.port

if db_connection == "mysql":
    default_db = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_name,
        'USER': db_username,
        'PASSWORD': db_password,
        'HOST': db_host,
        'PORT': db_port,
    }

elif db_connection == "postgres":
    default_db = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': db_name,
        'USER': db_username,
        'PASSWORD': db_password,
        'HOST': db_host,
        'PORT': db_port,
    }
else:
    default_db = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR + "/storage/database/", 'db.sqlite3')
    }

DATABASES = {
    'default': default_db
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Logging
# https://docs.djangoproject.com/en/2.0/topics/logging/
DJANGO_LOGGING_HANDLERS = [] if os.getenv("DJANGO_LOGGING_HANDLERS", "") == "" else os.getenv("DJANGO_LOGGING_HANDLERS", "").split(",")
DJANGO_LOGGING_LEVEL = "WARNING" if os.getenv("DJANGO_LOGGING_LEVEL", "") == "" else os.getenv("DJANGO_LOGGING_LEVEL", "").upper()
DJANGO_LOGGING_PROPAGATE = True if os.getenv("DJANGO_LOGGING_PROPAGATE", "") == "" or os.getenv("DJANGO_LOGGING_PROPAGATE", "") == "true" else False

APP_LOGGING_HANDLERS = ["file"] if os.getenv("APP_LOGGING_HANDLERS", "") == "" else os.getenv("APP_LOGGING_HANDLERS", "").split(",")
APP_LOGGING_LEVEL = "WARNING" if os.getenv("APP_LOGGING_LEVEL", "") == "" else os.getenv("APP_LOGGING_LEVEL", "").upper()
APP_LOGGING_PROPAGATE = True if os.getenv("APP_LOGGING_PROPAGATE", "") == "" or os.getenv("APP_LOGGING_PROPAGATE", "").lower() == "true" else False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(filename)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR + "/storage/logs/", time.strftime("%d-%m-%Y") + ".log"),
            'formatter': 'simple'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': DJANGO_LOGGING_HANDLERS,
            'level': DJANGO_LOGGING_LEVEL,
            'propagate': DJANGO_LOGGING_PROPAGATE,
        },
        'app': {
            'handlers': APP_LOGGING_HANDLERS,
            'level': APP_LOGGING_LEVEL,
            'propagate': APP_LOGGING_PROPAGATE,
        },
        'django.db.backends': {
            'handlers': APP_LOGGING_HANDLERS,
            'level': APP_LOGGING_LEVEL,
            'propagate': APP_LOGGING_PROPAGATE,
        },
        'django.request': {
            'handlers': APP_LOGGING_HANDLERS,
            'level': APP_LOGGING_LEVEL,
            'propagate': APP_LOGGING_PROPAGATE,
        },
        'django.server': {
            'handlers': APP_LOGGING_HANDLERS,
            'level': APP_LOGGING_LEVEL,
            'propagate': APP_LOGGING_PROPAGATE,
        },
        'django.template': {
            'handlers': APP_LOGGING_HANDLERS,
            'level': APP_LOGGING_LEVEL,
            'propagate': APP_LOGGING_PROPAGATE,
        },
    },
}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# Languages List
LANGUAGES = (
    ('fr', _('French')),
    ('en', _('English')),
    ('de', _('Deutsch'))
)

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/
LANGUAGE_CODE = "en-us"

TIME_ZONE = os.getenv("APP_TIMEZONE", "UTC")

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR + STATIC_URL

STATICFILES_DIRS = [BASE_DIR + "/assets"]

LOCALE_PATHS = [
    BASE_DIR + "/translation/"
]

# Celery Configs
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")

# Security Configs
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = False
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
X_FRAME_OPTIONS = "DENY"
