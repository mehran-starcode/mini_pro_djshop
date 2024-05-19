from .common import *

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '0.0.0.0',
    '192.168.43.116'
]


INSTALLED_APPS = [
     'daphne',
     'drf_spectacular',
     'django_extensions',

 ] + INSTALLED_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mini_pro_djshop',
        'USER': 'mehran',
        'PASSWORD': 'netcarshow/Net23@',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': 'ALTER DATABASE mini_pro_djshop DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci',
        }
    }
}
