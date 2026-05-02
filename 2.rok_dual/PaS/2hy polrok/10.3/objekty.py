from random import choice, randint


class Auto:
    farba = "cervena"
    znacka = choice(['bmw','Subaru','Mazda'])

auto1 = Auto()

print(auto1.farba)
print(auto1.znacka)

farby = ("zelena", "cervena", "zlta", "modra", "biela", "siva", "cierna", "tyrkysova", "hneda")

mena = (
   "Peter", "Ján", "Marek", "Tomáš", "Martin", "Lukáš", "Michal", "Andrej", "Roman", "Daniel",
   "Anna", "Jana", "Petra", "Mária", "Zuzana", "Katarína", "Lucia", "Veronika", "Monika", "Natália"
)

class Person:
    def __init__(self,
                 name='John',
                 age=18,
                 height=150,
                 weight=150,
                 shoe_size=42,
                 skin_color='White',
                 eye_color='Brown',
                 hair_color='Black'
                 # not including as input in constructor
                 # diseases = []
                 ):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.shoe_size = shoe_size
        self.diseases = []
        self.hair_color = hair_color
        if not self.diseases:
            self.healthy = True
# self odkazuje na svoje premenne svoje funkcie
# dalsi dovod preco vyplnave tzv default veci je to ze ak budeme tvorit a neviplnime tie polia nech su defaultne vytvorene

    def predstavenie(self):
        if self.healthy:
            zdravie = "Som zdravvy clovek a aktualne nemam ziadne choroby"
        else:
            zdravie = f"Som chory clovek a pocet mojich dignoz je {len(self.diseases)}"

        return f"""
                Ahoj, volam sa {self.name}, mam {self.age} rokov, nosim cislo topanok {self.shoe_size}.
                Meriam {self.height} cm a vazim {self.weight} kg.
                farba mojej pleti je {self.skin_color}, fraba mojich oci je {self.eye_color} a mam farbu vlasou {self.hair_color}.
                {zdravie}
                """



#tu ale to bude nahradene udajmi kt sme specifikovali
peter = Person('Peter',20)
print(peter.age)

defaultny_clovek = Person()

nahodny_clovek = Person(
                    name= choice(mena),
                    age= randint(18,90),
                    weight= randint(40, 120),
                    height= randint(150, 190),
                    shoe_size= randint(26, 46),
                    hair_color= choice(farby),
                    skin_color= choice(farby),
                    eye_color= choice(farby),
                )

moji_ludia = []
moji_ludia.append(peter)
moji_ludia.append(defaultny_clovek)
moji_ludia.append(nahodny_clovek)

for clovek in moji_ludia:
    print(clovek.predstavenie())

class Motorka:
    def __init__(self, color= None):
        self.engine_HP = randint(150, 500)
        self.engine_volume = (randint(10,30) / 10)
        self.engine_takty = choice([2,4])
        if not color:
            self.color = choice(farby)

sklad = []

def naskladni_motorky(kusy):
    for i in range(0,int(kusy)):
        sklad.append(Motorka())
    print(f"Naskladneny pocet motoriek: {kusy}")

def prezri_sklad():
    print(f"v sklade mame {len(sklad)} motoriek")
    for index, motorka in enumerate(sklad):
        print(f"prehliadam si motorku cislo {index}")
        print(f"Motorka ma tuto farbu {motorka.color}")
        print(f"motorka ma pocet koni {motorka.engine_HP}")
        print(f"motorka ma objem motora {motorka.engine_volume}")
        print(" ")

    print("prehliadka motoriek dokoncena. dodavatel bude vyplateny")

naskladni_motorky(5)
prezri_sklad()

#zdedena nova classa
class MiniMotorka(Motorka):