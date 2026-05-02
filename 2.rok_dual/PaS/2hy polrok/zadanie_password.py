import random

def passwd_gen():
    znaky = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
    heslo = ""
    
    for i in range(12):
        heslo = heslo + random.choice(znaky)
    
    return heslo

print("Generator hesla")
print("Tvoje heslo je:", passwd_gen())