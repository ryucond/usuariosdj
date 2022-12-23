from .base import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')


ALLOWED_HOSTS = ['*']



# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR, 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = [BASE_DIR, 'media']

