def response_checker(question: str) -> bool:
    ans = input(question)
    while ans != "y" and ans != "n":
        ans = input("Please enter 'y' or 'n': ")

    if ans == "y":
        return True
    else:
        return False
