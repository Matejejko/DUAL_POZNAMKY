user_input = input("Enter a string: ")  
print(user_input.upper())
print(user_input.lower())
print(user_input.title())
print(user_input.capitalize())

table = []
split_input = user_input.split()
for word in split_input:
    table.append(word)
print(table)

alphabetical_table = sorted(table)
print(alphabetical_table)