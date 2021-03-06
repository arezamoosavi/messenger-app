import os
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'z!8kx9vs-hsq2&v8^!qpmq)kn-u&jfzsy(m@3@b6@&b=d&s--8'

# SECURITY WARNING: don't run with debug turned on in production!
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
    
    # Installed
    'rest_framework',
    'rest_framework.authtoken',
    'simple_email_confirmation',
    'widget_tweaks',
    
    # Created
    'core',
    'apps.chat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = "config.routing.application"

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("ENGINE", ""),
        "NAME": os.environ.get("DATABASE_NAME", ""),
        "USER": os.environ.get("USER", ""),
        "PASSWORD": os.environ.get("PASSWORD", ""),
        "HOST": os.environ.get("HOST", ""),
        "PORT": os.environ.get("PORT", ""),
    }
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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, '/uploaded_files')
STATIC_ROOT = os.path.join(BASE_DIR, '/static_files')

AUTH_USER_MODEL = 'core.User'

# Caching
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Number of seconds of inactivity before a user is marked offline
USER_ONLINE_TIMEOUT = 1

# Number of seconds that we will keep track of inactive users for before
# their last seen is removed from the cache
USER_LASTSEEN_TIMEOUT = 60 * 60 * 24 * 7

# Celery

CELERY_BROKER_URL = "amqp://rabbitmq"
CELERY_ACCEPT_CONTENT = ['json',]
CELERY_TASK_SERIALIZER = 'json'

# Email

EMAIL_HOST = os.environ.get("ENV_EMAIL_HOST","smtp.fastmail.com")
EMAIL_PORT = os.environ.get("ENV_EMAIL_PORT",465)
EMAIL_HOST_USER = os.environ.get("ENV_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("ENV_EMAIL_HOST_PASSWORD")
EMAIL_USE_SSL = os.environ.get("ENV_EMAIL_USE_SSL", True)
EMAIL_USE_TSL = os.environ.get("ENV_EMAIL_USE_TSL", False)

# Email Confirmation
EMAIL_CONFIRMATION_PERIOD_DAYS = 7
SIMPLE_EMAIL_CONFIRMATION_PERIOD = timedelta(days=EMAIL_CONFIRMATION_PERIOD_DAYS)
SIMPLE_EMAIL_CONFIRMATION_AUTO_ADD = False
SIMPLE_EMAIL_CONFIRMATION_KEY_LENGTH = 10
# SIMPLE_EMAIL_CONFIRMATION_EMAIL_ADDRESS_MODEL = os.environ.get("ENV_EMAIL_HOST_USER")

# Log
LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'request_format': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d (%(message)s) '
                          '%(remote_addr)s %(user_id)s "%(request_method)s '
                          '%(path_info)s %(server_protocol)s" %(http_user_agent)s ',
            },
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d (%(message)s) '
            },
        },
        'handlers': {
            'console_django': {
                'class': 'logging.StreamHandler',
                # 'filters': ['request'],
                'formatter': 'verbose',
            },
            'console_project': {
                'class': 'logging.StreamHandler',
                # 'filters': ['request'],
                'formatter': 'request_format',
            },
            'file': {
                'class': 'logging.FileHandler',
                'filename': BASE_DIR + '/logs' + 'debug.log'
            },
        },
        'loggers': {
            'django.server': {
                'level': 'DEBUG',
                'handlers': ['console_django'],

            },
            'django.request': {
                'level': 'DEBUG',
                'handlers': ['console_django'],
            },
            'apps': {
                'level': 'DEBUG',
                'handlers': ['file', 'console_django'],
            }
        },
    }