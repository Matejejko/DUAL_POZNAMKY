try:
    veta = str(input("Zadajte váš vstup (vetu): "))
    x = int(input("Zadajte ktorý znak chcete odstrániť: "))
    print (veta[0:x:], end="")
    print(veta[x+1:])
except ValueError as e:
    print("Nezadal si správne vstup")