import random
import time
import os
znova = 1
while znova == 1:
    obtiaznost = int(input("zvol si obtiaznost: \n1 - lahka - ty mas na konce +1 a viac zivotov \n2 - stredna - vyrovnane \n3 - tazka - protivnyk ma +1 na kocke a viac zivotov \n:  "))
    zivoty_hrac = 3
    zivoty_protivnik = 3
    cislo_kocky_hrac = 0
    cislo_kocky_protivnik = 0

    if obtiaznost == 1:
        zivoty_hrac += 1
        cislo_kocky_hrac += 1
    elif obtiaznost == 3:
        zivoty_protivnik += 1
        cislo_kocky_protivnik += 1

    while zivoty_hrac > 0 and zivoty_protivnik > 0:
        cislo_kocky_hrac_this_round = cislo_kocky_hrac
        cislo_kocky_protivnik_this_round = cislo_kocky_protivnik
        print(f"tvoje mnozstvo zivotov: {zivoty_hrac} || zivoty nepriatela: {zivoty_protivnik}")
        kocka = int(input("Vyber si kocku: \n1 - D4 \n 2 - D6 \n 3 - D8 \n 4 - D12 \n:  "))
        if kocka == 1:
            cislo_kocky_hrac_this_round += random.randint(1, 4)
        elif kocka == 2:
            cislo_kocky_hrac_this_round += random.randint(1, 6)
        elif kocka == 3:
            cislo_kocky_hrac_this_round += random.randint(1, 8)
        elif kocka == 4:
            cislo_kocky_hrac_this_round += random.randint(1, 12)
        else:
            print("Neplatna volba kocky, zkus to znovu.")
            continue
        print(f"hodil si: {cislo_kocky_hrac_this_round}")
        time.sleep(1)
        print("protivnik si vybera a sa chysta hodit kockou")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        kocka_protivnik = random.randint(1, 4)
        print(f"protivnik si vybral kocku: {kocka_protivnik}")
        time.sleep(2)
        if kocka_protivnik == 1:
            cislo_kocky_protivnik_this_round += random.randint(1, 4)
        elif kocka_protivnik == 2:
            cislo_kocky_protivnik_this_round += random.randint(1, 6)
        elif kocka_protivnik == 3:
            cislo_kocky_protivnik_this_round += random.randint(1, 8)
        elif kocka_protivnik == 4:
            cislo_kocky_protivnik_this_round += random.randint(1, 12)
        print(f"protivnik hodil: {cislo_kocky_protivnik_this_round}")
        time.sleep(1)
        if cislo_kocky_hrac_this_round > cislo_kocky_protivnik_this_round:
            print("vyhral si toto kolo \n")
            time.sleep(1)
            zivoty_protivnik -= 1
            os.system('cls' if os.name == 'nt' else 'clear')
        elif cislo_kocky_hrac_this_round < cislo_kocky_protivnik_this_round:
            print("protiinik vyhral toto kolo \n")
            time.sleep(1)
            zivoty_hrac -= 1
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("remiza, zivoty ostavaju rovnake \n")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')

    if zivoty_hrac > 0:
        znova = int(input("Gratulujem, vyhral si hru! Chces to skusit znovu? (1 - ano, 0 - nie): "))
        if znova == 0:
            print("Diky za hru, maj sa!")
    else:
        znova = int(input("Bohuzial, si prehral hru. Chces to skusit znovu? (1 - ano, 0 - nie): "))
        if znova == 0:
            print("Diky za hru, maj sa!")
