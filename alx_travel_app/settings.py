import environ
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize environment variables
env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

INSTALLED_APPS = [
    'drf_yasg',
    'rest_framework',
    'corsheaders',
]