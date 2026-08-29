"""
OmniSolve EduClear - Primary Application Entry Point
"""
import os
import sys
import subprocess

def main():
    print("Launching OmniSolve EduClear Platform...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educlear_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django. Ensure it is installed.") from exc
    
    if len(sys.argv) == 1:
        sys.argv = ['manage.py', 'runserver', '127.0.0.1:8000']
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
