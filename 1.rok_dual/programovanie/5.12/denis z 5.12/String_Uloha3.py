try:
    veta = str(input("Zadajte váš vstup (vetu): "))
    if len(veta) <3:
        print("Vraciam späť originálny vstup:",veta)
    else:
        print (veta[0:3])
except ValueError as e:
    print("Nezadal si správne vstup")