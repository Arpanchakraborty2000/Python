lst = [1,2,3,4,5,6,7,8,9,10]

even_number=0
odd_number=0

for i in lst:
    if(i % 2 ==0):
        even_number = even_number+i
    else:
        odd_number=odd_number+i


print("Sum of Evennumber :{}".format(even_number))
print("Sum of ODD number : {}".format(odd_number))