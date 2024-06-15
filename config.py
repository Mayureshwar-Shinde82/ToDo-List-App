import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    KEYCLOAK_SERVER_URL = 'http://localhost:8080/auth/'
    KEYCLOAK_REALM = 'myralm'
    KEYCLOAK_CLIENT_ID = 'myclient'
    KEYCLOAK_CLIENT_SECRET = 'your_client_secret'
    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', 'your_stripe_public_key')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', 'your_stripe_secret_key')
