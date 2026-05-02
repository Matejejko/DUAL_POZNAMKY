import datetime
import re
# Skript na ziskanie udajov o pouzivatelovi a vypis do konzoly

# Ziskanie udajov od pouzivatela
meno = input("Zadajte vase meno: \n")
priezvisko = input("Zadajte vase priezvisko: \n")

pattern = re.compile(r'^[a-zA-Z\s]+$')

if not pattern.match(meno) or not pattern.match(priezvisko):
    print('mas glupe meno')
else:
    datum_narodenia = input("Zadajte datum narodenia (vo formáte dd.mm.yyyy): \n")
    dnes = datetime.datetime.now()
try:
    den, mesiac, rok = map(int, datum_narodenia.split('.'))
    datum = datetime.datetime(rok, mesiac, den)
except ValueError:
    print("error")
else:
    if datum > dnes:
        print('u from the future mate?')
    else:
        # Vypis do konzoly
        print(f"Ahoj {meno} {priezvisko}, narodil si sa {den:02d}.{mesiac:02d}.{rok:04d}")

        # Scitanie datumu narodenia
        sucet_cislic = den + mesiac + rok
        print(f"Sucet cislic datumu narodenia: {sucet_cislic}")
        # Vypis znamenia zverokruhu
