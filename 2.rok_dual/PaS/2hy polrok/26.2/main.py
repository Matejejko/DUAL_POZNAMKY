import os
import platform  # windows / linux
import random
import sys  # mozme si ukazat argumenty


def clearscreen():
    if platform.system() == "Linux":
        print("Linux")
        os.system("clear")
    elif platform.system() == "Windows":
        print("Windows")
        os.system("cls")


# alebo mozme pozret os.environ.get("OS") ale tato env var je len na windowse aj to nemusi byt vsade.

# hardcoded menu
# refactor menu

clearscreen()

print()
print("test")
print("last argument")
print(sys.argv[-1])
print()
print(os.getcwd())

