def funkcia():
        c2 = c + 1  
        print(n[:c],n[c2:])


try:
    n = input("Aký text chceš upraviť: ")
    try:
        c = int(input("Ktoré písmeno chceš upraviť [začína sa od 0 a nie 1]: "))
        funkcia()
    except ValueError:
        print("Chyba: Zadaj platné číslo!")
except ValueError as e:
    print('debil?')




