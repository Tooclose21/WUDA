from dotenv import load_dotenv
from os import environ
load_dotenv()

hostname = environ.get('BACKEND_HOSTNAME', 'localhost')
port = environ.get("BACKEND_PORT", 5000)

SECRET_KEY = environ.get('SECRET_KEY', 'dev-secret-key')

BACKEND_URL = f"http://{hostname}:{port}"
APP_PORT = environ.get('APP_PORT', 8000)
APP_HOST = environ.get('APP_HOST', "localhost")