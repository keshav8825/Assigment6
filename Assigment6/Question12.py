#. Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part
a=complex(input("Enter a complex number"))
print(a.real) if a.real>a.imag else print(a.imag)
