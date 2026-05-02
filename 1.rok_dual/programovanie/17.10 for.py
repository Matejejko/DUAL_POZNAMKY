car = ["audi", "bmw", "mercedes", "skoda", "toyota", "honda"]
for x in car:
    if x in ['mercedes', 'bmw', 'toyota']:
        continue
    print(x)
else:
    print("that's all.\n")

cars = ['audi', 'bmw', 'W', 'mercedes', 'honda', 'toyota', 'mitsubishi', 'lexus']
german = ['audi', 'bmw', 'W', 'mercedes']
japanese = ['honda', 'toyota', 'mitsubishi', 'lexus']
for y in cars:
    if y in japanese:
        continue
    print(y)
else:
    print('finished...\n')