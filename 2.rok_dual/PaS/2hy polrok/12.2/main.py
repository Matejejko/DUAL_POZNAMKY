premenna = 'text'
print(type(premenna))

cislo = 174737
print(type(cislo))

#zmena datoveho typu
#su int(), float(), str(), bool(), ...
text_ako_cislo = (str(cislo))
print(type(text_ako_cislo))
print(cislo)


print("\n")
print( text_ako_cislo[1] ) #vypise 3ty znak v premennej zlava
print( text_ako_cislo[-3] ) #vypise 3ty znak zo zadu

print(type(bool(text_ako_cislo))) #ide to z vnutra vonku

zoznam = ["text1", 5, float(6), 'text2']
print("zoznam je typu:", type(zoznam))
for i in zoznam:
    print(i, "is", type(i))

#zmena listu ked je vytvoreny
#pomocou .append()
zoznam.append('pridany_text3')


print("\n")
print(zoznam[-1])

print("\n")
if 'text1' in zoznam:
    print("text1 sa nachadza v zozname")
elif '45' not in zoznam:
    print('45 nie je v zozname')


dvojrozmerny_zoznam = [
    [0,0,0,0],
    [0,1,0,0],
    [0,0,0,0],
]

entica = (3,4,5) #tuple = immutable var
#entica.append() - doent exist - tuple is immutable


#input od uzivatela: ->>
#meno = input("zadaj meno: ")


print('\n')
#dictionary
ages = {'peter': 45, 'Igor': 25, 'Sara': 19} # ta ":" tam je
print(ages)
print(ages["peter"])
print(ages.keys())
print(ages.values())
print(ages.items())

#zmena v dictionarty values
ages["peter"] = 99
print(ages["peter"])


print("\n")
#string manipulation
#.lower(), upper(), .capitalize(), .title()
print("hiiii".capitalize())
print("hiiii".upper())

#pozri .isdigit()
# .join()
# .format mas v idk
#   text("text" {})
#   a s text.format('adam') tak do text sa doplni adam