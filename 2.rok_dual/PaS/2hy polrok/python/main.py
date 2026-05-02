print('hello world!')
print('di kule mule')
# single line comment
# there are no multi-line comments in py


# variable
vek = 25
meno = "Jakub"
# option 2 of declaring string
meno2 = 'Adam'

# multiline string
my_multiline_string = '''
toto je
viacriadkovy
text
'''

my_multiline_string_2 = """
toto je druhy
viacriadkovy
text
"""

# f-stng pre vypis premennych v texte
# napriklad f"abc" alebo f'abc'
# v f-stringu volame premennu cez {}
print(f"moje meno je {meno} a moj vek je {vek}")

# printing only variable doesnt need quotes(",') or fstring
# print(f'{my_multiline_string}') same but unnecessary
# if we dont add custom text, f-string is not necessary
print(my_multiline_string)

# other methods of printing variables in text
print("Hello, {}!".format(meno2))
#print("Hello, {}!".)
# %d - intiger placeholder (data type celych cisel)
# %s - string placeholder (data type of string/text)
print("Hello, {}!".format("Johnson"))
print("I'm %d years old" % 42)

priezvisko = "Kuko"

cele_meno = meno + " " + priezvisko
print(cele_meno)
#alebo
print(meno2 + ' ' + priezvisko)

print("Ha" * 4)
smiech = "Ha" * 4

print(cele_meno.lower())
print(cele_meno.find("k"))
# alebo zkombinovane spolu
# find -1 znamena ze to nenaslo a nasledne to ide od 0 hore podla toho kde sa nachadza najdene pismeno
print(smiech.lower().find('h'))

#zalomeny text
print("zalomeny \n text")

# data types

# types of numbers
#   intigers: 1,2,3
#   floats: 1.3, 1.34
#   este nieco idk

print(4 + 4)
print(4 - 4)
print(4 * 4)
print(4 ** 4)
print(4 / 4)
print(4 // 4) #cele cislo bez zvysku
print(4 % 4) # je zvysok ci neni cele cislo vysledok nam da 0 a opak 1