import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True
DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sds',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
    },
    
}


PHANTOMJS = '/mnt/c/projects/phantomjs/bin/phantomjs'

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/local/',  # end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats-local.json'),
    }
}


