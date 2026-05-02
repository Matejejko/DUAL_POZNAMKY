import random

dlzka = int(input("Zadaj dlzku aku chces na hesle: "))

def generuj_heslo():
        znaky = "abcdefghijklmnopqrstuvwxyz"
        velke_znaky = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cisla = "0123456789"
        specialne_znaky = "!@#$%^&*()_+-=~`|\\:;\"'<>,.?/"
        
        # Zaistit, ze heslo obsahuje vsechny typy znakov
        heslo = [
            random.choice(znaky),
            random.choice(velke_znaky),
            random.choice(cisla),
            random.choice(specialne_znaky)
        ]
        
        # Vypenit zvysok dlzky nahodnym vyberam zo vsetkych znakov
        vsetky_znaky = znaky + velke_znaky + cisla + specialne_znaky
        for i in range(dlzka - 4):
            heslo.append(random.choice(vsetky_znaky))
        
        # Nahodne premiestit znaky
        random.shuffle(heslo)
        
        return "".join(heslo)
    
heslo = generuj_heslo()
print("Vygenerovane heslo:", heslo)


    