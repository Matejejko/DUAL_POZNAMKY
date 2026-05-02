# if ,elif, else
# pass = nic nerob
from html.parser import endtagfind

text = "1 2 3 4 5 6 7 8 9"
cisla = text.split()
print(cisla)

for i in cisla:
#    print(type(cisla))
    cislo = int(i)
    if cislo %2 == 0:
        pass
    else:
        print(i)

# while loop
print("\n")
i = 1
while i < 3:
    print(f"i je {i}")
    i += 1 # i = i + 1

print("\n")
ludia = {"peter": 20, "ondrej": 30,}
for meno, vek in ludia.items():
    print(f"{meno.capitalize()} ma {vek} rokov")

print("\n")
veci = ["taska", "stol", "jablko", "hruska", "Pohar"]
for index,vec in enumerate(veci):
    print(f"cislo {index} je {vec}")

ovocie = ["jablko", "hruska", "banan"]
for i in veci:
    if i == "stol":
        print("vec je drevena")
    elif i in ovocie:
        print("vec sa da zjest")

print("\n")
#vypis len ovocie
# continue skipny code a pokracuj alebo daco take
for i in veci:
    if i not in ovocie:
        continue
    print(i)


#ukonci loop ak vec je ovocie
for i in veci:
    if i in ovocie:
        break
    else:                   # nemusi tu byt lebo break nam to ukonci a ide dalej takze moze a nemusi
        print(f"vec je {i}")

print("\n")
for i in range(10): # tiez mozeme (1, 10) od 1 po 10 ...
    print(i)

