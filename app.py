"""
OmniSolve EduClear - Secondary WSGI/ASGI Application Entry Point
"""
import os
from educlear_backend.wsgi import application

app = application

if __name__ == '__main__':
    import sys
    from django.core.management import execute_from_command_line
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educlear_backend.settings')
    execute_from_command_line(['manage.py', 'runserver', '127.0.0.1:8000'])
