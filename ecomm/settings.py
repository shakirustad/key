"""
Django settings for ecomm project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
from decouple import config
# Add Render DB support if using PostgreSQL
# import dj_database_url

# DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config("SECRET_KEY")
SECRET_KEY = 'django-insecure-5$r91x#k2_00fnh!+0naf@w*(g$9y84v&6a_jb$5$3zhr2%m#3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG")

# ALLOWED_HOSTS = []



ALLOWED_HOSTS = ['*']
# import os
# DEBUG = os.getenv("DEBUG", "False") == "True"


# # Static files settings
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_URL = '/static/'


# Application definition

SITE_ID = 2

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps
    'products',
    'accounts',
    'home',

    # Django Social Auth Configurations
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',  # For Google authentication
    'allauth.socialaccount.providers.facebook',  # For Facebook authentication

    # for crispy forms
    'django_countries',
    'crispy_forms',
    'crispy_bootstrap4',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Facebook API KEYS
SOCIAL_AUTH_FACEBOOK_KEY = config('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = config('SOCIAL_AUTH_FACEBOOK_SECRET')

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'APP': {
            'client_id': '53126655196-3jv1qj502du0drg6dtqmgil9pjifgvv1.apps.googleusercontent.com',
            'secret': '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',
            'key': '',  # Optional, leave empty
        }
    }

    # Facebook authentication
    # "facebook": {
    #     'APP': {
    #         # Facebook API KEYS
    #         'client_id': SOCIAL_AUTH_FACEBOOK_KEY,
    #         'secret': SOCIAL_AUTH_FACEBOOK_SECRET,
    #     },
    #     'METHOD': 'oauth2',  # Set to 'js_sdk' to use the Facebook connect SDK
    #     'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
    #     'SCOPE': ['email', 'public_profile'],
    #     'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
    #     'INIT_PARAMS': {'cookie': True},
    #     'FIELDS': [
    #         'id',
    #         'first_name',
    #         'last_name',
    #         'middle_name',
    #         'name',
    #         'name_format',
    #         'picture',
    #         'short_name',
    #     ],
    #     'EXCHANGE_TOKEN': True,
    #     'VERIFIED_EMAIL': False,
    #     'VERSION': 'v17.0',
    #     'GRAPH_API_URL': 'https://graph.facebook.com/v17.0',
    # }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'ecomm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecomm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [os.path.join(BASE_DIR, "public/media")]

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Mail Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# EMAIL_HOST_USER = config('ustadhismailgunia@gmail.com')
# EMAIL_HOST_PASSWORD = config('povpdzlworltrbwv')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='ustadhismailgunia@gmail.com')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='povpdzlworltrbwv')

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_USE_SSL = False

# # RazorPay API KEYS
# RAZORPAY_KEY_ID = config('RAZORPAY_KEY_ID')
# RAZORPAY_SECRET_KEY = config('RAZORPAY_SECRET_KEY')

# Auth Backends Configurations
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Auto signup
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_LOGIN_ON_GET = True

DEFAULT_DOMAIN = '127.0.0.1:8000'
DEFAULT_HTTP_PROTOCOL = 'http'
