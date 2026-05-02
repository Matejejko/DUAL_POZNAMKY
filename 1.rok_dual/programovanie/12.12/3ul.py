wordlist = ['apple', 'cherry', 'kiwi', 'strawberry', 'plum']
n = input("slova dlhsie ako kolko chces? :\n")

finish =[]

for x in wordlist:
    if len(x) > int(n):
        finish.append(x)
print(finish)
    