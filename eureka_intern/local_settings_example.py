# -*- coding: utf-8 -*-

import os

DEBUG = True

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# local
# postgresql
# DATABASES = {
#     'default': {
#          'ENGINE': 'django.db.backends.postgresql_psycopg2',
#          'NAME': 'p_chat_api',
#          'USER': 'Daichi',
#          'PASSWORD' : '',
#          'HOST' : '127.0.0.1',
#          'PORT' : 5432,
#      }
#  }
