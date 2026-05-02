import os
import platform # windows / linux
import random

def clearscreen():
    if platform.system() == "Linux":
        print("linux")
        os.system("clear")
    elif platform.system() == "Windows":
        print("Windows")
        os.system("cls")


# for key in os.environ.keys():
#     print(key)

print("removed message")
clearscreen()


class Vypln():
    def __init__(self):
        self.text = ' '
        self.writable = True

class HracskaVypln(Vypln):
    def __init__(self):
        self.text = random.choice(['X','O'])
        self.writable = False

rozmer_plochy = 3

herna_plocha = []

for i in range(0,(rozmer_plochy**2)):
    herna_plocha.append(Vypln())

# print(herna_plocha)

def vykresli_plochu(hp=herna_plocha, rozmer=rozmer_plochy):
    print("vykreslujem plochu")
    print("_______")
    if rozmer == 3:
        i=0
        for policko in hp:
            print("|",end='')
            print(policko.text,end='')
            if i == 2 or i == 5 or i == 8:
                print("|", end='')
                print()
                print("-------")

            i += 1

    else:
        print("neviem vykreslit takyto rozmer plochy")

hrac = HracskaVypln()

while True:
    vykresli_plochu()


    print("cislo policka")
    volba=int(input())
    volba = volba - 1

    print(volba)
    herna_plocha[volba] = hrac

 