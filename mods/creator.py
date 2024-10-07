import os
import subprocess

from utils.response_checker import response_checker


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
        pass

    def create_fullstack_app(self):
        pass

    # Back-end Section
    def create_django_app(self):
        pass

    def create_flask_app(self):
        pass

    def create_fastapi_app(self):
        pass

    def create_express_app(self):
        pass
