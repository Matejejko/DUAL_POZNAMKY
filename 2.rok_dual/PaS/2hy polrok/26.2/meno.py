import os
import platform  # windows / linux
import time
import random
import datetime
import sys  # mozme si ukazat argumenty
start_time = datetime.datetime.now()

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

print("\tMENU \n \tverison: 0.1")
print("\tAuthor: Mpapaj")
time.sleep(2)

clearscreen()

menu_text = '''
1. vypis druh OS
2. Hod kockou
3. ukonci program
'''
volba = 0
while True:
    print(menu_text)
    volba = int(input("Volba: "))
    # print(type(volba))
    clearscreen()
    if volba == 1:
        print(platform.system())
    elif volba == 2:
        print(random.randint(1,6))
    elif volba == 3:
        break

end = datetime.datetime.now()
duration = end - start_time
print("koniec programu!")
print(f"trvanie: {duration}")



#iny sposob
menu_texty = [
    "vypis druh OS",
    "Hod kockou",
    "hod 20 hrannou kockou",
    "ukonci program"
]
while True:
    for idx, menutext in enumerate(menu_texty):
        menu_index = idx + 1
        print(f"{menu_index}. {menutext}")
    volba = int(input("Volba: "))
    # print(type(volba))
    clearscreen()
    if menu_texty[volba - 1] == "vypis druh OS":
        print(platform.system())
    elif menu_texty[volba - 1] == "Hod kockou":
        print(random.randint(1, 6))
    elif menu_texty[volba - 1] == "ukonci program":
        break

end = datetime.datetime.now()
duration = end - start_time
print("koniec programu!")
print(f"trvanie: {duration}")