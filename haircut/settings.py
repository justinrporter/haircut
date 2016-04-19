"""
Django settings for haircut project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret! 

# In production, set 'DJANGO_SECRET_KEY' to a real key.
try:
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
except KeyError:
    SECRET_KEY = '=-n20ckxfssoc7kti@-j=k4ike#j3ap8j6t@#b6x_d9liy!-x1'

# In production set 'DJANGO_DEBUG' environment var to False
try:
    DEBUG = int(os.environ['DJANGO_DEBUG'])
    print >> sys.stderr, "Setting DEBUG to", DEBUG
except KeyError:
    print >> sys.stderr, \
        "Settings failed to detect DJANGO_DEBUG envrionment variable.", \
        "Falling back to DEBUG == True"
    DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'haircut.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'haircut.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

import dj_database_url

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql', 
            'NAME': 'dfj2s6hkoorl72',
            'USER': 'wghqgdanopcgqh',
            'PASSWORD': 'Z1sCMT1ZZ84_YCPVmCiW-IlE92',
            'HOST': 'ec2-54-225-103-29.compute-1.amazonaws.com', # Or something like this
            'PORT': '5432',                     
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)


if DEBUG:
    CSRF_COOKIE_SECURE = True

PAYPAL_PDT_TOKEN = "PRr9RXwqJn1k2HTnFNk5J19vKntMe8SfmIne90DIfURqRYGce_ZD-QgQBMe"
PAYPAL_URL = 'https://www.sandbox.paypal.com/cgi-bin/webscr'
PAYPAL_PDT_URL = 'https://www.sandbox.paypal.com/cgi-bin/webscr'


MERCHANT_ID = "L8KF3JYDVNWTS"

# live
# PAYPAL_PDT_TOKEN = "k1OPFc7pSY2TkX1sX4-EecbL8vyWWlSkH8dg03u5xBXrF6lW8ehQGpvkWY8"
# PAYPAL_URL = 'https://www.paypal.com/cgi-bin/webscr'
# PAYPAL_PDT_URL = 'https://www.paypal.com/cgi-bin/webscr'
# MERCHANT_ID = "WVUT663HTXM3Q"