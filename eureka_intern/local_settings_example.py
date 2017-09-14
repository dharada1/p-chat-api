# -*- coding: utf-8 -*-

# ローカルの開発環境の設定ファイル
# local_settings_example.py から local_settings.py にリネームしてつかってください

import os

DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
