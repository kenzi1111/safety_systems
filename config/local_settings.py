from pathlib import Path
import os

# settings.pyからそのままコピー
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

BASE_DIR = Path(__file__).resolve().parent.parent

# settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True  # ローカルでDebugできるようになります。