from rich_menu import Menu
import os


def menu():
    menu = Menu(
        "Option 1",
        "Option 2",
        "Option 3",
        "Exit",
    )
    match menu.ask():
        case "Option 1":
            print(os.getcwd())
        case "Option 2":
            print("second option selected")
        case "Option 3":
            print("third option selected")
        case "Exit":
            print("Bye!")
            quit()
