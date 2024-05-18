from .common import *


INSTALLED_APPS = [
    'daphne',
    'drf_spectacular',
    'django_extensions',

] + INSTALLED_APPS



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djbase_test',
        'USER': 'mehran',
        'PASSWORD': 'netcarshow/Net23@',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': 'ALTER DATABASE djbase_test DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci',
        }
    }
}