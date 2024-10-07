from rich.traceback import install

from mods.menu import menu

# Rich traceback support (better error messages)
install()


def main():
    menu()


if __name__ == "__main__":
    main()
