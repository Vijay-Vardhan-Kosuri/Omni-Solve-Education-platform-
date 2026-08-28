"""
One-Click Entrypoint Launcher
OmniSolve EduClear - Academic Doubt Clarification Platform
"""

import os
import sys
import subprocess
import webbrowser
import time

def run():
    print("=" * 70)
    print("      OmniSolve EduClear - Academic Doubt Clarification Platform      ")
    print("=" * 70)
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educlear_backend.settings')
    import django
    django.setup()

    print("[1/3] Running Django Database Migrations...")
    subprocess.run([sys.executable, 'manage.py', 'makemigrations'], check=True)
    subprocess.run([sys.executable, 'manage.py', 'migrate'], check=True)

    print("\n[2/3] Seeding Initial Subject Knowledge Base & Solved Doubts...")
    from knowledge_base.seed_data import seed_database
    seed_database()

    print("\n[3/3] Starting Django Web Server at http://127.0.0.1:8000 ...")
    
    # Launch browser after a short delay
    def open_browser():
        time.sleep(2)
        webbrowser.open('http://127.0.0.1:8000')

    import threading
    threading.Thread(target=open_browser, daemon=True).start()

    subprocess.run([sys.executable, 'manage.py', 'runserver', '127.0.0.1:8000'])

if __name__ == '__main__':
    run()
