import time
import random
import os

stopka = 0
x = input("zadaj prvé číslo: ")
os.system('cls')
y = input ("zadaj druhé číslo: ")
os.system('cls')
operand = input("zadaj operand(+,-,x,:): ")
os.system('cls')
delay = 0

while stopka < (random.randrange(5,10)):
    print(".")
    time.sleep(0.2)
    os.system('cls')
    print("..")
    time.sleep(0.2)
    os.system('cls')
    print("....")
    time.sleep(0.2)
    os.system('cls')
    print("..... ")
    time.sleep(0.2)
    os.system('cls')
    stopka = stopka + 1
#time.sleep(random.randrange(5,10))

print("Hello World!")

time.sleep(3)

input("Press any key to exit: ")