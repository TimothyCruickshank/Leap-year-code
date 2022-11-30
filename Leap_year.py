year = int(input("Enter a year to check if it's a leap year or not? "))

# Divisible by 4 - leap year
# Exception is if it's divisble by 400 - leap year
# BUT exception if it's divisible by 400 - leap year

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("leap Year")
else:
    print("Not a Leap Year")
    