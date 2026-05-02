try:
    input = input(str("Aký text chceš upraviť: "))
    if len(input) < 3:
        print("I M P U T:", input, "   ti neupravim")
    else:
        print(input[:3])

except ValueError as e:
    print("Nezadal si správne vstup")