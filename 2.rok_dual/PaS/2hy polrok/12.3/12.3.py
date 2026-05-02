import random

# class Bar(object):
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)

class Clovek:
    def __init__(self,name=None):
        if name is None:
            self.name = f"clovek{random.randint(0,500)}"
        else:
            self.name = name
        self.age = None
        self.height = None
        self.weight = None
        self.skin_color = None
        self.eye_color = None
        self.shoe_size = None
        self.diseases = []
        self.sins = []
        self.hair_color = None
        if not self.diseases:
            self.healthy = True

ludia = []

ludia.append(Clovek(name='Adam'))
ludia.append(Clovek(name='Eva'))

for p in ludia:
    print(p.name)

hriechy = ['Pycha','obzerstvo','lakomstvo','lenivost']


ine_choroby = ['uraz','zlomenina',]
infekcne_choroby = ['ebola','chripka','infekcia']
choroby = ine_choroby + infekcne_choroby

# ako vieme obmedzit input type z 'any' na konkretny datovy typ?
# ako vieme obmedzit input type z 'any' na konkretny typ objektu?
# aky je rozdiel medzi local,nonlocal, global variable ?

def nahodne_zlo(person):
    zlo = random.choice(
        [random.choice(choroby),random.choice(hriechy)]
                        )
    #choroba = choroby[random.randint(0,len(choroby)-1)]
    if zlo in choroby:
        person.diseases.append(zlo)
    elif zlo in hriechy:
        person.sins.append(zlo)

for i in range(1,6):
    nahodne_zlo(ludia[0])
    nahodne_zlo(ludia[1])

print("Dosledok nakazy:")
for c in ludia:
    print(f"{c.name} ma tieto choroby:")
    print(f"cely zoznam {c.diseases}")
    for choroba in c.diseases:
        print(choroba)


print("hriechy")
for c in ludia:
    print(f"zoznam hriechov {c.name} -  {c.sins}")

def infection_check(p):
    check = True
    for infekcna_choroba in infekcne_choroby:
        if infekcna_choroba in p.diseases:
            #check = not check # reverse boolean in python
            check = False
    return check


print("infekcna kontrola:")
for c in ludia:
    # if infection_check(c) == False:
    if not infection_check(c):
        print(f"{c.name} nepresiel infekcnou kontrolou")



class Doktor(Clovek):
    def odstran_zlo(self,p):
        p.diseases.remove(random.choice(p.diseases))


doktor = Doktor()

print("doktor lieci adama")

doktor.odstran_zlo(ludia[0])

print("adamove choroby")
for d in ludia[0].diseases:
    print(d)

class Farar(Doktor):
    def odstran_zlo(self,p):
        p.sins.remove(random.choice(p.sins))


farar = Farar()

print("farar odpusta jeden hriech Eve")
farar.odstran_zlo(ludia[1])

print("evine hriechy:")
print(ludia[1].sins)

 