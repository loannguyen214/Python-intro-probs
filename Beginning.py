'''import math
a = math.ceil(2.678)
print(a)
print(math.copysign(5, -10))
print(math.fabs(-8))
x = 6
print(math.factorial(x))
print(math.floor(4.874387))
from fractions import Fraction
print(Fraction(2, 18))
print(Fraction(47674, 7642))
print(Fraction(2.48754))'''
'''name = "Harsh"
print(name[2])
print(len(name))
print(name[len(name)-1])
name_1 = name + "arsh"
print(name_1)
name_2 = 3 * name
print(name_2)
print(name_2[len(name_2)-1-2])'''''

'''name = "toloan"
print(name[:4])
print(name[2:])
name = "thi " + name
print(name)'''

'''name = "toloan"
print(name[:-2])
name[2] = "i"'''''

'''author = ['Harsh Bhasin', 'Mark Lutz', "Shiv"]
print(author)
combined = [1, 'Harsh', 23.4, 'a']
print(combined)
list_3 = []
print(list_3)
list_of_list = [1, [1, 2], 3]
print(list_of_list)
print(list_of_list[-1])
author[0] = 'Jane Austin'
print(author)'''''


'''a=2
b=3
tup = (a,b)
(a, b) = (b, a)
print(tup)
print(a, ",", b)'''

'''tup1 = (1, 2)
tup2 = ("a", "b")
print(tup1 + tup2)'''

'''a = 5
b = 2
c = float ((a)/b)
print(c)

a = 'A'
b = 'B'
print(a + b)'''

'''a = 5
b = 2
a= a + b
b = a - b
a = a - b
print(a)'''

'''a = 5
b * b = a
print(b)'''

'''(a, b) = (2, 3)
(c, d) = (4, 5)
print((a, b) * (c, d))'''

'''b
a = 'tar'
b = 'rat'
print(2*(a+b))'''

# Program #1: Write a program to swab two numbers:
'''print("Enter the first number:\t")
a = float(input())
print("Enter the second number:\t")
b = float(input())
(a, b) = (b, a)
print("Now, the first number is: ", a, "and the second number is: ", b)'''

# Program #2: Calculate the distance from one point to the origin
'''import math as mt
print("Enter the coordinates of point A(x,y)")
print('x = ')
x = float(input())
print('y = ')
y= float(input())
a = x**2 + y**2
distance = mt.sqrt(a)
print("The distance of point A from the origin is:", distance)'''

# Program #3: Calculate distance between two point with coordinates (x, y):
('import math as mt\n'
 'x1 = float(input("Enter A\'s x value: "))\n'
 'y1 = float(input("Enter A\'s y value: "))\n'
 'x2 = float(input("Enter B\'s x value: "))\n'
 'y2 = float(input("Enter B\'s y value: "))\n'
 'distance_squared = (x1 - x2)**2 + (y1 - y2)**2\n'
 'distance = mt.sqrt(distance_squared)\n'
 'print("Distance between A and B is: ", distance)')

#Program #3: Find out whether 3 points are collinear
'''import math as mt
x1 = float(input("Enter A's x value: "))
y1 = float(input("Enter A's y value: "))
x2 = float(input("Enter B's x value: "))
y2 = float(input("Enter B's y value: "))
x3 = float(input("Enter C's x value: "))
y3 = float(input("Enter C's y value: "))
AB_squared = (x1 - x2)**2 + (y1 - y2)**2
BC_squared = (x2 - x3)**2 + (y2 - y3)**2
AC_squared = (x1 - x3)**2 + (y1 - y3)**2
AB = mt.sqrt(AB_squared)
BC = mt.sqrt(BC_squared)
AC = mt.sqrt(AC_squared)
if AB + BC == AC or AB + AC == BC or AC + BC == AB:
    print("collinear")
else:
    print("not collinear1")'''

# another solution to problem #3 with more lines
'''if AB + BC == AC: #if adding"is True to if statement, testing turned out wrong output, WHY???"
    print("A, B, C are Collinear")
elif AB + AC == BC:
    print("A, B, C are Collinear")
elif AC + BC == AB:
    print("A, B, C are Collinear")
else:
    print("A, B, C are not Collinear")'''

# Find the type of triangle formed by three points if those three points are not collinear
'''import math as mt
x1 = float(input("Enter A's x value: "))
y1 = float(input("Enter A's y value: "))
x2 = float(input("Enter B's x value: "))
y2 = float(input("Enter B's y value: "))
x3 = float(input("Enter C's x value: "))
y3 = float(input("Enter C's y value: "))
AB_squared = (x1 - x2)**2 + (y1 - y2)**2
BC_squared = (x2 - x3)**2 + (y2 - y3)**2
AC_squared = (x1 - x3)**2 + (y1 - y3)**2
AB = mt.sqrt(AB_squared)
BC = mt.sqrt(BC_squared)
AC = mt.sqrt(AC_squared)
if AB + BC != AC and AB + AC != BC and AC + BC != AB:
    if AB == BC  == AC:
        print("ABC is an equilateral triangle")
    elif AB==AC or AB==BC or AC==BC:
        print("ABC is an isosceles triangle")
    else:
        print("ABC is a scalene triangle")
else:
    print("A, B, C are collinear")'''

# Find the greatest number of the 3 numbers entered:

'''a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number"))
print("The greatest number is: ", max(float(a), float(b), float(c)))'''

'''x = int(input("Enter value of x: "))
if x >2:
    f = (pow(x, 2)) + 5*x + 3
else:
    f = x + 3
print("Value of function f(x) = %d" %f)'''

''''a = 8
i =1
while a
    print(a)
    i = i+1
    a = a-i
print(i)'''

# find whether a number is a prime number:
'''n = int(input("Enter a number: "))
if n == 1:
    print(n, "is a prime number")
elif n > 1:
    k = 0
    for i in range(2,n):
        if n%i==0:
            k+=1

    if k >= 1 :
        print(n, " is not a prime number")
    else:
        print(n, "is a prime number")'''
# Find all the factors of a number
'''n = int(input("Enter a number: "))
list_of_factor = []
for i in range(1,n+1):
    if n%i == 0:
        list_of_factor += [i]
print("The factors of {} are".format(n), list_of_factor)'''

# Find out if a number is a perfect square:
'''n = int(input("Enter a number: "))
if n == 0 or n==1:
    print(n, " is a perfect square")
else:
    k = 0
    for i in range(1,n):
        if i**2 == n:
            k += 1
    if k ==1:
        print(n, " is a perfect square")
    else:
        print(n, " is not a perfect square")'''


