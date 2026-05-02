vysledok = ""
input = input(str("zadaj text: "))
for i in range(1, len(input)): 
    if i % 2 == 0:
        vysledok += input[i]
print(vysledok)