#c1
def pozdravenie():
    print("Serbvus moj nestastny brat, ako sa mas?")
pozdravenie()

print("\n")
#c2
def pozdrav():
    text = input("Zadaj pozdrav: ")
    print(text)
pozdrav()

print("\n")
#c3
import random
random_cislo = random.randint(1, 10)
print(random_cislo)

mena = ["Jozef", "Martin", "Marek", "Lukas", "Tomas"]
meno = random.choice(mena)
print(meno)

random.shuffle(mena)
print(mena[-1])

print("\n")
#4 
from datetime import datetime 
teraz = datetime.now()
print(teraz)
print(teraz.strftime("%d-%m-%Y %H:%M:%S"))

print("\n")
#5
import time
def zadanie_5():
    start = datetime.now()
    print(f"Zaciatok: {start}")
    time.sleep(5)
    end = datetime.now()
    print(f"Koniec: {end}")
    rozdiel = end - start
    print(f"Rozdiel: {rozdiel}")

zadanie_5()

print("\n")
#6
import os
os.environ["POZDRAV"] = "AHOJ"
hodnota = os.environ.get("POZDRAV")
print(hodnota)


print("\n")
#7
#!/usr/bin/env python3
import sys
print(sys.version)
print("All args: ", sys.argv)
# print("First args: ", sys.argv[1])

print("\n")
#8
pyversion = sys.version_info
with open("python_version.txt", "w") as subor:
    subor.write(f"Python version: {pyversion}")

