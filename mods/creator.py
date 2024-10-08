import os
import subprocess

from utils.response_checker import response_checker
from utils.venv_creator import venv_creator

from tmpl import flask_base as FLASK_BASE_APP
from tmpl import express_base as EXPRESS_BASE_APP


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
        current_dir = os.getcwd()
        venv_prompt = response_checker("Do you want to create a venv? (y/n): ")
        if venv_prompt:
            venv_creator(current_dir, ["django"])

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
        current_dir = os.getcwd()
        venv_prompt = response_checker("Do you want to create a venv? (y/n): ")
        if venv_prompt:
            venv_creator(current_dir, ["flask", "uvicorn"])

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
        current_dir = os.getcwd()
        venv_prompt = response_checker("Do you want to create a venv? (y/n): ")
        if venv_prompt:
            venv_creator(current_dir, ["fastapi", "uvicorn"])

        project_name = input("Enter project name: ")
        subprocess.run(
            f"mkdir {project_name} && cd {project_name} && echo '{FLASK_BASE_APP}' > app.py",
            shell=True,
            cwd=current_dir
        )
        run_app = response_checker("Do you want to run the app? (y/n): ")
        if run_app:
            os.system("uvicorn app:app")

    def create_express_app(self):
        current_dir = os.getcwd()
        project_folder_name = input("Enter project name: ")
        final_path = f"{current_dir}/{project_folder_name}"
        os.system(f"mkdir {final_path} && cd {final_path}")
        os.system("npm init -y")

        typescript_support_prompt = response_checker("Do you want to use typescript? (y/n): ")
        if typescript_support_prompt:
            os.system("tsc --init")
            os.system("npm install express")
            os.system("npm install typescript --save-dev")
            os.system("npm install @types/express --save-dev")
            os.system("npm install @types/node --save-dev")
            os.system("npm install ts-node-dev --save-dev")
            os.system("npm install ts-node --save-dev")
            os.system("npm install nodemon --save-dev")
        
        else:
            os.system("npm install express")
            os.system("npm install nodemon --save-dev")

        os.system(f"touch {final_path}/app.js")
        os.system(f"echo '{EXPRESS_BASE_APP}' > {final_path}/app.js")

        run_app = response_checker("Do you want to run the app? (y/n): ")
        if run_app:
            os.system("nodemon app.js")

    def create_fullstack_app(self, tech_frontend: str, tech_backend: str):
        pass