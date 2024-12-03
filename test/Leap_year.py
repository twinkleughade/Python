year=int(input("Enter Year \n"))
if (year % 4 == 0 & year % 100 != 0) or (year % 400 == 0 & year %100==0):
    print("It a leap year")
else:
    print("It a not leap year")

