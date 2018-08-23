"""
Django settings for config project.
Generated by 'django-admin startproject' using Django 2.1.
"""

import os

from djs import import_secrets

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT_DIR = os.path.dirname(BASE_DIR)
STATIC_DIR = os.path.join(BASE_DIR, 'static')
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
CONFIGS_DIR = os.path.join(ROOT_DIR, '.configs')
SECRETS_DIR = os.path.join(ROOT_DIR, '.secrets')

# Static
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
STATICFILES_DIRS = [
    STATIC_DIR,
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Auth
AUTH_USER_MODEL = 'members.User'
ADMIN_USERNAME = 'pbkdf2_sha256$120000$kQERZDMkpKxs$1ALg7vpcUacEYO7IH3GJvdBgukLJeJr9Pe+P+Itvk3A='
ADMIN_PASSWORD = 'pbkdf2_sha256$120000$Z3gZEyW25bKm$8OMEFPkZ8gGFpFqUX8TiVgvlERUG8/UkKoNz3nJs7VQ='
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'members.backends.SettingsBackend',
]

import_secrets()

INSTALLED_APPS = [
    'members',
    'products',
    'utils',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'sass_processor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'products.middleware.ProductCategoryMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATES_DIR,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'products.context_processors.category',
            ],
        },
    },
]

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
