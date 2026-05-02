vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
wordlist = ['apple', 'orange', 'kiwi', 'umbrella', 'egg', 'plum']

def filter_words(wordslist):
    for word in wordslist:
        if word[0] in vowels and word[-1] in vowels:
            yield word
filtered = list(filter_words(wordlist))
print("Words filtered:", filtered)
