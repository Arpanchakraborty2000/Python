even_number = 0
odd_number = 0
i = 0

while (i <= 10):
    if (i % 2 == 0):
        even_number = even_number + i   # add evens
    else:
        odd_number = odd_number + i     # add odds
    i = i + 1

print("Even number sum is: {} and ODD number sum is: {} ".format(even_number, odd_number))
