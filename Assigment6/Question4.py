#Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.

print("enter two number: ")
a,b=int(input()),int(input())
print(a if a>b else b)
