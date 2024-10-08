import os
import subprocess

from utils.response_checker import response_checker

from tmpl.flask_base import FLASK_BASE_APP


class Creator:
    def __init__(self):
        pass

    # Front-end Section
    def create_frontend_vite(self):
        current_dir = os.getcwd()
        project_name = input("Enter project name: ")
        subprocess.run(
            f"npm create vite@latest {project_name}",
            shell=True,
            cwd=current_dir
        )
        os.system("cd {project_name} && npm install")
        run_app = response_checker("Do you want to run the app? (y/n): ")
        if run_app:
            os.system("npm run dev")

    def create_next_app(self):
        current_dir = os.getcwd()
        project_name = input("Enter project name: ")
        subprocess.run(
            f"npm create next@latest {project_name}",
            shell=True,
            cwd=current_dir
        )
        os.system("cd {project_name} && npm install")
        run_app = response_checker("Do you want to run the app? (y/n): ")
        if run_app:
            os.system("npm run dev")

    # Back-end Section
    def create_django_app(self):
        venv_prompt = response_checker("Do you have a venv? (y/n): ")
        if not venv_prompt:
            os.system("python -m venv .venv")

        os.system("source .venv/bin/activate")
        current_dir = os.getcwd()
        project_name = input("Enter project name: ")
        subprocess.run(
            f"django-admin startproject {project_name}",
            shell=True,
            cwd=current_dir
        )
        os.system(f"cd {project_name} && python manage.py migrate")
        run_app = response_checker("Do you want to run the app? (y/n): ")
        if run_app:
            os.system("python manage.py runserver")

    def create_flask_app(self):
        venv_prompt = response_checker("Do you have a venv? (y/n): ")
        if not venv_prompt:
            os.system("python -m venv .venv")

        os.system("source .venv/bin/activate")
        os.system("pip install flask")
        current_dir = os.getcwd()
        project_name = input("Enter project name: ")
        subprocess.run(
            f"mkdir {project_name} && cd {project_name} && echo '{FLASK_BASE_APP}' > app.py",
            shell=True,
            cwd=current_dir
        )
        run_app = response_checker("Do you want to run the app? (y/n): ")
        if run_app:
            os.system("python app.py")

    def create_fastapi_app(self):
        pass

    def create_express_app(self):
        pass

    def create_fullstack_app(self, tech_frontend: str, tech_backend: str):
        pass