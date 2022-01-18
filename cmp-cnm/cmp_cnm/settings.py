"""
Django settings for cmp_cnm project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pg-2*hls3&x0oz@6tgg-t&2_d5*7+u4mj3ky)fhst)254g_^x('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.getenv('DEBUG', 0)))


ALLOWED_HOSTS = ['*']
APPEND_SLASH = False

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'cmp_cnm',
    'nssrc',
    'lb',
    'lb.citrixapi'
]

REST_FRAMEWORK = {
    'DATE_FORMAT': '%Y-%m-%d',
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
    'DEFAULT_PAGINATION_CLASS': 'cmp_cnm.pagination.PageNumberPagination',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'NON_FIELD_ERRORS_KEY': 'all',
}

MIDDLEWARE = [
    'cmp_cnm.middleware.HealthCheckMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cmp_cnm.urls'
HEALTH_CHECK_PATH = os.getenv('HEALTH_CHECK_PATH', '/health')


URL = os.getenv("URL", "127.0.0.1:8080")
WEB_PORT = os.getenv("WEB_PORT", 8080)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cmp_cnm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'cmp_iaas'),
        'USER': os.getenv('DB_USER', 'cmp_iaas'),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': int(os.getenv('DB_PORT', 5432)),
        'CONN_MAX_AGE': 3
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATETIME_FORMAT = 'Y-m-d H:i:s'

DATE_FORMAT = 'Y-m-d'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{asctime}|{levelname}|{process:d}-{thread:d}|{filename}#{lineno}|{module}:{funcName}|{message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {asctime} {created} {message}',
            'style': '{',
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'cmp_cnm': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        }
    }
}


OS_PROJECT_DOMAIN_NAME = os.getenv('OS_PROJECT_DOMAIN_NAME', 'Default')
OS_USER_DOMAIN_NAME = os.getenv('OS_USER_DOMAIN_NAME', 'Default')
OS_PROJECT_NAME = os.getenv('OS_PROJECT_NAME', '')
OS_TENANT_NAME = os.getenv('OS_TENANT_NAME', '')
OS_USERNAME = os.getenv('OS_USERNAME', '')
OS_PASSWORD = os.getenv('OS_PASSWORD', '')
OS_AUTH_URL = os.getenv('OS_AUTH_URL', '')
OS_INTERFACE = os.getenv('OS_INTERFACE', 'internal')
OS_ENDPOINT_TYPE = os.getenv('OS_ENDPOINT_TYPE', 'internalURL')
OS_IDENTITY_API_VERSION = int(os.getenv('OS_IDENTITY_API_VERSION', '3'))
OS_REGION_NAME = os.getenv('OS_REGION_NAME', '')
OS_AUTH_PLUGIN = os.getenv('OS_AUTH_PLUGIN', 'password')

OS_TOKEN_KEY = os.getenv('OPENSTACK_TOKEN_KEY', 'Os-Token')

NS_HOST = os.getenv('NS_HOST', '127.0.0.1')
NS_PROTOCOL = os.getenv('NS_PROTOCOL', 'http')
NS_USER = os.getenv('NS_USER', '')
NS_PASSWD = os.getenv('NS_PASSWD', '')
NS_TIME = os.getenv('NS_TIME', 3600)
HTTP_FILE = os.getenv('HTTP_FILE', '127.0.0.1')

ACCOUNT_INFO_KEY = os.getenv('ACCOUNT_INFO_KEY', 'Account-Info')

SWAGGER = bool(int(os.getenv('SWAGGER', 0)))

if SWAGGER:
    SWAGGER_SETTINGS = {
        'LOGOUT_URL': '/admin/logout/',
        'SECURITY_DEFINITIONS': {
            ACCOUNT_INFO_KEY: {
                'type': 'apiKey',
                'name': ACCOUNT_INFO_KEY.lower(),
                'in': 'header'
            },
            OS_TOKEN_KEY: {
                'type': 'apiKey',
                'name': OS_TOKEN_KEY.lower(),
                'in': 'header'
            }
        },
    }
