import datetime
import random
import time

casy = []


def stopky():
    cas = datetime.datetime.now()
    casy.append(cas)


def pockaj(dlzka):
    time.sleep(dlzka)


def pockaj_chvilu():
    dlzka_2 = random.randint(1, 5)
    time.sleep(dlzka_2)


def ukaz_casy(vstup=""):
    vstup = str(vstup).strip()

    if vstup == "":
        for i, cas in enumerate(casy):
            print(f"{i}: {cas}")
        return

for _ in range(5):
    stopky()
    pockaj(1)
    pockaj_chvilu()

ukaz_casy()

nahodny_cas = random.choice(casy)
print(f"Nahodny cas: {nahodny_cas}")
