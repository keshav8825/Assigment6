# Write a python script to take the month value in numeric format and display the number of days in it.
a=int(input("Enter a month name: "))
if a in(1,3,5,7,8,10,12):
    print("31 days")
elif a in(4,6,9,11):
    print("30 days")
else:
    print("28 days")
    

