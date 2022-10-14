# Write a python script to print greater among three numbers. Print number only once even if the numbers are the same
print("enter three number ")
a=int(input())
b=int(input())
c=int(input())
print((a if a>c else c) if a>b else (b if b>c else c))
    

