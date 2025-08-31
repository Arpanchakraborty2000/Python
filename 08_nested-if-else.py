age = int(input("Enter the age : "))

if age < 18:
    print("Minor age")
    if age < 15:
        print("You are in school")
    else:
        print("You are in college.")
elif age >= 18 and age <= 45:
    print("Mid age")
elif age > 45 and age <= 60:
    print("Senior mid age")
else:
    print("Senior citizen")
