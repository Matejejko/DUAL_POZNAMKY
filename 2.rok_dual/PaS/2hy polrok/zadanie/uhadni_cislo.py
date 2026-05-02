import random
import time

pokusy = 5
hladane_cislo = random.randint(1, 100)

zaciatok = time.time()

print("Uhadni cislo od 1 do 100")

while pokusy > 0:
	tip_text = input(f"Zadaj cislo (zostava {pokusy} pokusov): ")

	tip = int(tip_text)
	pokusy -= 1

	if tip < hladane_cislo:
		print("Moje cislo je vacsie")
	elif tip > hladane_cislo:
		print("Moje cislo je mensie")
	else:
		print("Uhadol si")
		break

koniec = time.time()
trvanie = koniec - zaciatok

print(f"Myslene cislo bolo: {hladane_cislo}")
print(f"Cas hadania: {trvanie:.2f} s")
