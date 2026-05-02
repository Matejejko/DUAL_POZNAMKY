mix = ['jablko', 'oko', 'koleno', 1221, True, 59, 'AA', False, 'krk', '4354', 'kiwi', 53, 443, 'jablko',]
#1
filtered_mix = [i for i in mix if not isinstance(i, bool)]
print("1) Zoznam mix bez bool hodnot:", filtered_mix)

#2
x=0
for i in mix:
    if isinstance(i, str):
        x+=1
print("2) Pocet retazcov v zozname mix je:", x)

#3
nenumericke_retezcce = []
for x in mix:
    if isinstance(x, str) and not x.isdigit():
        nenumericke_retezcce.append(x)

if len(nenumericke_retezcce) > 0:
    najkratsi_retezec = nenumericke_retezcce[0]
    for retezec in nenumericke_retezcce:
        if len(retezec) < len(najkratsi_retezec):
            najkratsi_retezec = retezec
        elif len(retezec) == len(najkratsi_retezec) and retezec < najkratsi_retezec:
            najkratsi_retezec = retezec
else:
    najkratsi_retezec = None
print("3) Najkratsi, nie numericky retazec je:", najkratsi_retezec)

#4
numericke_hodnoty = []
for i in mix:
    if isinstance(i, (int, float)) and not isinstance(i, bool):
        numericke_hodnoty.append(i)
    elif isinstance(i, str):
        try:
            cislo = int(i) if '.' not in i else float(i)
            numericke_hodnoty.append(cislo)
        except ValueError:
            pass

sucet_numerickych = sum(numericke_hodnoty)
print("4) Sucet vsetkych cisel zoznamu mix je:", sucet_numerickych)

#5
vhodne_cisla = []
for x in mix:
    if isinstance(x, (int, float)):
        x_str = str(int(x))  
        if len(x_str) > 2 and x_str[0] == x_str[-1]:
            vhodne_cisla.append(int(x))
    elif isinstance(x, str):
        try:
            num_value = float(x) if '.' in x else int(x)
            num_str = str(int(num_value))
            if len(num_str) > 2 and num_str[0] == num_str[-1]:
                vhodne_cisla.append(int(num_value))
        except ValueError:
            pass

if vhodne_cisla:
    najmensie_cislo = min(vhodne_cisla)
    najvacsie_cislo = max(vhodne_cisla)
else:
    najmensie_cislo = None
    najvacsie_cislo = None
print("5) Najmensie cislo s rovnakou zaciatocnou a koncovou cislocou je:", najmensie_cislo, "a najvacsie je", najvacsie_cislo)