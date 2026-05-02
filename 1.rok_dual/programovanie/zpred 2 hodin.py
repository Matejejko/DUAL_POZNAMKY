meno = input("Zadaj svoje meno: ")
priezvisko = input("Zadaj svoje priezvisko: ")
den = int(input("Zadaj deň narodenia: "))
mesiac = int(input("Zadaj mesiac narodenia: "))
rok = int(input("Zadaj rok narodenia: "))

# Vypísanie dátumu narodenia vo formáte DD.MM.RRRR
print(f"Ahoj {meno} {priezvisko}, narodil si sa {den:02d}.{mesiac:02d}.{rok}")

# Výpočet a vypísanie súčtu čísel dátumu narodenia
sucet = den + mesiac + rok
print(f"Súčet číslic dátumu narodenia: {sucet}")


def chod(name):
    print("Ahoj", name)

def userInput():
    name = input("Zadaj svoje meno: ")
    
    # Potrebujeme si overit name ci su cislice cez .isdigit() pretoze funkcia input vzdy vracia string
    if name.isdigit():
        print("Zadali ste cislo. Prosim skuste znova.")
        userInput()
    elif name.isalpha():  # Kontrola, ci su len znaky
        chod(name) # Rovno volam funkciu chod a jej odovzdavam parameter name
    else:
        print("Zadali ste ine znaky. Prosim skuste znova.")
        userInput()

userInput()  



# Asking for user input
name = input("Zadaj meno: ")
surname = input("Zadaj priezvisko: ")

# Asking for date input and converting them to integers
day = int(input("Zadaj den narodenia (ako int): "))
month = int(input("Zadaj mesiac narodenia (ako int): "))
year = int(input("Zadaj rok narodenia (ako int): "))

# Using concatenation
print("Ahoj " + name + " " + surname + ", narodil si sa " + str(day).zfill(2) + "." + str(month).zfill(2) + "." + str(year))

# Using commas (comma-separated arguments automatically add spaces)
print("Ahoj", name, surname + ", narodil si sa", str(day).zfill(2) + "." + str(month).zfill(2) + "." + str(year))

# Using the % operator (Old-style String Formatting)
print("Ahoj %s %s, narodil si sa %02d.%02d.%d" % (name, surname, day, month, year))

# Using str.format()
print("Ahoj {}, {}, narodil si sa {:02}.{:02}.{}".format(name, surname, day, month, year))

# Using positional arguments in str.format()
print("Ahoj {0} {1}, narodil si sa {2:02}.{3:02}.{4}".format(name, surname, day, month, year))

# Using keyword arguments in str.format()
print("Ahoj {name} {surname}, narodil si sa {day:02}.{month:02}.{year}".format(name=name, surname=surname, day=day, month=month, year=year))

# Using f-strings (Python 3.6+)
print(f"Ahoj {name} {surname}, narodil si sa {day:02}.{month:02}.{year}")


pi = 3.14159
print("Pi je priblizne {:.2f}".format(pi))

age = 2024 - year

print(f"Buduci rok budem mat {age + 1} rokov") 