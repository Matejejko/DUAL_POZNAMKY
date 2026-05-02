veta = input(str("Zadajte váš vstup (vetu s medzerou): "))
str1, str2 = veta.split()

vymena1 = str2[:2] + str1[2:]
vymena2 = str1[:2] + str2[2:]
print(vymena1, vymena2)