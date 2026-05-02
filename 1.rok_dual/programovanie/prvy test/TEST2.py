N = int(input("Zadaj cele cislo N (pocet vypisov): \n"))
INDEX = int(input("Zadaj cele cislo INDEX (inkrement): \n"))
INDEX2 = INDEX
M = 1
sucet = 0


for i in range(N):
    vysledok = M * INDEX2
    print("Sucin ("+str(M)+" * "+str(INDEX2)+") je: "+str(vysledok))
    sucet += vysledok

    M += INDEX
    INDEX2 += 1

print("Sucet cisel kazdej iteracie:",sucet)
