#. Write a python script to check whether a given year is a leap year or not.
a=int(input("Enter a year "))
if a%400==0:
    print("year is leap year")
elif a%4==0:
    print("year is a leap year")
elif a%100!=0:
    print("year is a leap year")
else:
    print("not a leap year ")
    
