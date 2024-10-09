from rich_menu import Menu
import os

from creator import Creator

def menu():
    creator = Creator()
    menu = Menu(
        "Create Frontend Vite",
        "Create Next App",
        "Create Django App",
        "Create Flask App",
        "Create FastAPI App",
        "Create Express App",
        "Create Fullstack App",
        "Exit",
    )
    match menu.ask():
        case "Create Frontend Vite":
            creator.create_frontend_vite()
        case "Create Next App":
            creator.create_next_app()
        case "Create Django App":
            creator.create_django_app()
        case "Create Flask App":
            creator.create_flask_app()
        case "Create FastAPI App":
            creator.create_fastapi_app()
        case "Create Express App":
            creator.create_express_app()
        case "Create Fullstack App":
            creator.create_fullstack_app("Vite", "Django")
        case "Exit":
            exit()
