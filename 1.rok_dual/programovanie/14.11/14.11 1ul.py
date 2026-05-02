
vstupny_retazec = input("Zadajte reťazec: ")

# Inicializácia premennej pre dĺžku reťazca bez medzier
dlzka_bez_medzier = 0

# Prechádzanie každého znaku v reťazci
for znak in vstupny_retazec:
    # Ak znak nie je medzera, zvýšiť dĺžku
    if znak != " ":
        dlzka_bez_medzier += 1

# Vypísanie dĺžky reťazca bez medzier
print(f"Dĺžka zadaného reťazca bez medzier je: {dlzka_bez_medzier}")
