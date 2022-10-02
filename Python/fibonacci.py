#WAP to print fibonacci series till a range given by the user


print("fibonacci series!")

# 'rang' here is the range 
rang = int(input("enter a range: "))

# fibonacci series = 0,1,1,2,3,5,8...

a = 0
b = 1
print(a,b, end = '')
print(" ", end = '') #this line gives a space after printing b

for i in range (1, rang-1, 1): 
    c = a + b
    print(c, end = '')
    a = b
    b = c
    print(" ", end = '') #this line gives a space after entering a character (number) in the loop
    