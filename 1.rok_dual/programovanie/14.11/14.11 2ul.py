inputuzivatela = input('zadaj vetu: ')

samohlasky = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
bez_samohlasok = ''
for znak in inputuzivatela:
    if znak not in samohlasky:
        bez_samohlasok += znak

print('Veta bez samohlások:', bez_samohlasok)