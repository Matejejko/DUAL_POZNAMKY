input = input(str("Zadajte text: "))
dlzka = len(input)
if dlzka % 4 == 0:
    print(input[::-1])
else:
    print(input)