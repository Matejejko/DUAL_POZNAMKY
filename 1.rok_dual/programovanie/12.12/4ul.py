wordlist = ['apple', 'cherry', 'kiwi', 'apple', 'strawberry', 'plum', 'kiwi']
finish = []

for x in wordlist:
    if x not in finish:
        finish.append(x)
print(finish)