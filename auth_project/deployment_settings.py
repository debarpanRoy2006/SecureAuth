import os
import dj_database_url
from .settings import *

DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY", SECRET_KEY)

ALLOWED_HOSTS = ["secureauth-7xqy.onrender.com", "localhost", "127.0.0.1"]

# Static files
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

 # Change this line

# Only keep this if you truly have a /static folder in the repo
# If you have a 'static' folder at your project root containing global static files, keep this.
# Otherwise, you can remove it.


MIDDLEWARE.insert(
    1,
    "whitenoise.middleware.WhiteNoiseMiddleware",
)

TEMPLATES[0]["DIRS"] = [
    os.path.join(BASE_DIR, "templates"),
]

DATABASES = {
    "default": dj_database_url.config(
        conn_max_age=600,
        ssl_require=True,
        default=f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}",
    )
}