import os

from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get("DH_HOST")
DB_PORT = os.environ.get("DH_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
SECRET_FOR_JWT_STRATEGY = os.environ.get("SECRET_FOR_JWT_STRATEGY")
SECRET_FOR_PASSWORD = os.environ.get("SECRET_FOR_PASSWORD")
