veta = input(str("Zadajte váš vstup (vetu): "))
bez_neparnych = ""
for i in range (len(veta)):
    if i % 2 == 0:
        bez_neparnych += veta[i]
print (bez_neparnych)