# Skript na ziskanie udajov o pouzivatelovi a vypis do konzoly

# Ziskanie udajov od pouzivatela
meno = input("Zadajte vase meno: ")
priezvisko = input("Zadajte vase priezvisko: ")
datum_narodenia = input("Zadajte datum narodenia (vo formáte dd.mm.yyyy): ")
den, mesiac, rok = map(int, datum_narodenia.split('.'))

# Vypis do konzoly
print(f"Ahoj {meno} {priezvisko}, narodil si sa {den:02d}.{mesiac:02d}.{rok:04d}")

# Scitanie datumu narodenia
sucet_cislic = den + mesiac + rok
print(f"Sucet cislic datumu narodenia: {sucet_cislic}")