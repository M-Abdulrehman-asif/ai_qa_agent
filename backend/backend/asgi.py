import os
import django
from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

# Django ASGI app
django_app = get_asgi_application()

# FastAPI app import
from backend.fastapi_server.main import app as fastapi_app

# Mount Django inside FastAPI
fastapi_app.mount("/django", WSGIMiddleware(django_app))

# Set FastAPI app as the main ASGI app
app = fastapi_app
