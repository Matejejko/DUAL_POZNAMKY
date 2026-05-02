veta = input(str("Zadajte váš vstup (vetu s medzerou): "))
str1, str2 = veta.split()

vymeneny1 = str2[:2] + str1[2:]
vymeneny2 = str1[:2] + str2[2:]
print(vymeneny1, vymeneny2)
