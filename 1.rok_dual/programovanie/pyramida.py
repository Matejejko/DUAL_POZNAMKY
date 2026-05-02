
try:
    n = int(input('What size do u want mate?\n'))
    if n >= 1:
        for i in range(1, n + 1):
            # Calculate the number of spaces and stars
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            
            # Print the current level of the pyramid
            print(spaces + stars)
    else:
        print("Invalid input, number must be greater than or equal to 1")
except ValueError:
    print("Invalid input, that is not a number mate")
