#Problem 1
twoDnum = int(input("Please enter an integer less than 100: "))

negative = ( twoDnum < 0)
fail = (twoDnum >= 100) or ( twoDnum <= -100)
zero = (twoDnum == 0)

roman_twoDnum = ""

if (fail == True):
    print("Please enter an integer LESS than 100")
    
if (negative == True):
    twoDnum = -twoDnum

if (zero == True):
    roman_twoDnum = roman_twoDnum + "0"

while( twoDnum >= 50):
    roman_twoDnum = roman_twoDnum + "L"
    twoDnum = twoDnum - 50
    if ( twoDnum < 50):
        break

while( twoDnum >= 10):
    roman_twoDnum = roman_twoDnum + "X"
    twoDnum = twoDnum - 10
    if ( twoDnum <  10):
        break

while( twoDnum >= 5):
    roman_twoDnum = roman_twoDnum + "V"
    twoDnum = twoDnum - 5
    if ( twoDnum < 0):
        break

while( twoDnum >= 1):
    roman_twoDnum = roman_twoDnum + "I"
    twoDnum = twoDnum - 1
    if ( twoDnum == 0):
        break

if negative:
    print("-", roman_twoDnum)

else:
    print(roman_twoDnum)



#Problem 2
a = int(input("Pleasse enter the first length: "))
b = int(input("Pleasse enter the second length: "))
c = int(input("Pleasse enter the third length: "))


if (a**2 + b**2 == c**2):
    print(a,b,c,"form a right triangle.")

elif (b**2 + c**2 == a**2):
    print(a,b,c,"form a right triangle.")

elif (c**2 + a**2 == b**2):
    print(a,b,c,"form a right triangle.")

else:
    print(a,b,c,"does not form a right triangle.")

#Problem 3
"""import turtle
#0
tri.forward(50)
tri.right(90)
tri.forward(100)
tri.right(90)
tri.forward(50)
tri.right(90)
tri.forward(100)
tri.right(90)
#1
tri.right(90)
tri.forward(100)
tri.left(90)
#2
tri.forward(50)
tri.right(90)
tri.forward(50)
tri.right(90)
tri.forward(50)
tri.left(90)
tri.forward(50)
tri.left(90)
tri.forward(50)
#3
tri.forward(50)
tri.right(90)
tri.forward(50)
tri.right(90)
tri.forward(50)
tri.backward(50)
tri.left(90)
tri.forward(50)
tri.right(90)
tri.forward(50)
tri.right(180)
#4
tri.right(90)
tri.forward(50)
tri.left(90)
tri.forward(50)
tri.left(90)
tri.forward(50)
tri.backward(100)
tri.right(90)
#5
tri.backward(50)
tri.right(90)
tri.forward(50)
tri.left(90)
tri.forward(50)
tri.right(90)
tri.forward(50)
tri.right(90)
tri.forward(50)
tri.right(180)
#6
tri.backward(50)
tri.right(90)
tri.forward(100)
tri.left(90)
tri.forward(50)
tri.left(90)
tri.forward(50)
tri.left(90)
tri.forward(50)
tri.left(180)
#7
tri.forward(50)
tri.right(90)
tri.forward(100)
tri.left(90)
#8
tri.forward(50)
tri.right(90)
tri.forward(100)
tri.right(90)
tri.forward(50)
tri.right(90)
tri.forward(100)
tri.backward(50)
tri.right(90)
tri.forward(50)
#9
tri.forward(50)
tri.right(90)
tri.forward(100)
tri.right(90)
tri.forward(50)
tri.right(180)
tri.forward(50)
tri.left(90)
tri.forward(50)
tri.left(90)
tri.forward (50)
tri.right(90)
tri.forward(50)
tri.right(90)"""

import turtle
wn = turtle.Screen()
tri = turtle.Turtle()

twoDs = int(input("Please enter a two digit integer: "))
if (twoDs < 10) or (twoDs > 99):
    print("ingeter is less than 10 or bigger than 99")
oneth = twoDs % 10
tenth = (twoDs // 10)

if (oneth == 0):
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.right(90)

if (oneth == 1):
    tri.right(90)
    tri.forward(100)
    tri.left(90)

if (oneth == 2):
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)

if (oneth == 3):
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.backward(50)
    tri.left(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.right(180)

if (oneth == 4):
    tri.right(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.backward(100)
    tri.right(90)

if (oneth == 5):
    tri.backward(50)
    tri.right(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.right(180)

if (oneth == 6):
    tri.backward(50)
    tri.right(90)
    tri.forward(100)
    tri.left(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.left(180)

if (oneth == 7):
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.left(90)

if (oneth == 8):
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.backward(50)
    tri.right(90)
    tri.forward(50)

if (oneth == 9):
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.right(90)
    tri.forward(50)
    tri.right(180)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.left(90)
    tri.forward (50)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    
tri.penup()
tri.setpos(-110,0)
tri.pendown()

if (tenth == 0):
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.left(90)

if (tenth == 1):
    tri.right(90)
    tri.forward(100)
    tri.left(90)

if (tenth == 2):
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)

if (tenth == 3):
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.backward(50)
    tri.left(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.right(180)

if (tenth == 4):
    tri.right(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.backward(100)
    tri.right(90)

if (tenth == 5):
    tri.backward(50)
    tri.right(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.right(180)

if (tenth == 6):
    tri.backward(50)
    tri.right(90)
    tri.forward(100)
    tri.left(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.left(180)

if (tenth == 7):
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.left(90)

if (tenth == 8):
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.backward(50)
    tri.right(90)
    tri.forward(50)

if (tenth == 9):
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.right(90)
    tri.forward(50)
    tri.right(180)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.left(90)
    tri.forward (50)
    tri.right(90)
    tri.forward(50)
    tri.right(90)

    
#Problem 4

import math
a = int(input("Please enter a: "))
b = int(input("Please enter b: "))

if ( a == 0 ):
    print("The equation has no solutions")

elif( b == 0 ):
    print("The equation has one solution, and x = 0")

else:
    if ( a == 0 ):
        print("The equation has no solutions")
    else:
        x = - b / a
        print("The equation has one solution, and x = ", x )


#Problem 5
name = str(input("Please enter your name: "))
gyear = int(input("Please enter your graduation year: "))
cyear = int(input("Please enter your current year: "))

different = gyear - cyear
no_college = (different > 4)
Freshman = (different == 4)
Sophomore = (different == 3)
Junior = (different == 2)
Senior = (different == 1)
graduated = (different < 1)

if (no_college == True):
    print(name,"is not in college yet")

if (Freshman == True):
    print(name,"is a Freshman")

if (Sophomore == True):
    print(name,"is a Sophomore")

if (Junior == True):
    print(name,"is a Junior")

if (Senior == True):
    print(name,"is a Senior")

if (graduated == True):
    print(name,"is graduated")


#Problem 6
    
import math
print("a cannot equal to b")
a = int(input("Please enter a positive integer a between 50 and 500: "))
b = int(input("Please enter a positive integer b between 50 and 500: "))

if (a <= 50) or ( a >= 500):
    print("False integer for a")
if (b <= 50) or ( b >= 500):
    print("False integer for b")
if (a == b):
    print("a cannot equal to b")

side_a = a / 2
side_b = b / 2
x = (side_a / side_b)
angle = math.degrees(math.atan(x))

sideH = math.sqrt(side_a*side_a + side_b*side_b)
Cangle = 90 - angle

import turtle
wn = turtle.Screen()
tri = turtle.Turtle()

tri.forward(a)
tri.left(90)
tri.forward(b)
tri.left(90)
tri.forward(a)
tri.left(90)
tri.forward(b)
tri.left(90)
tri.forward(side_a)
tri.left(Cangle)
tri.forward(sideH)
tri.left(2*angle)
tri.forward(sideH)
tri.left(2*Cangle)
tri.forward(sideH)
tri.left(2*angle)
tri.forward(sideH)

#Problem 7

month = int(input("Please enter an integer between 1 and 12: "))

if (month < 1) or (month > 12):
    print("Falst integer")

if (month == 1):
    print("The entered month is Jan., and the number of days in Jan. is 31.")
elif(month == 2):
    print("The entered month is Feb., and the number of days in Feb. is 28.")
elif(month == 3):
    print("The entered month is Mar., and the number of days in Mar. is 31.")
elif(month == 4):
    print("The entered month is Apr., and the number of days in Apr. is 30.")
elif(month == 5):
    print("The entered month is May, and the number of days in May is 31.")
elif(month == 6):
    print("The entered month is June, and the number of days in June is 30.")
elif(month == 7):
    print("The entered month is July, and the number of days in July is 31.")
elif(month == 8):
    print("The entered month is Aug., and the number of days in Aug. is 31.")
elif(month == 9):
    print("The entered month is Sept., and the number of days in Sept. is 30.")
elif(month == 10):
    print("The entered month is Oct., and the number of days in Oct. is 31.")
elif(month == 11):
    print("The entered month is Nov., and the number of days in Nov. is 30.")
elif(month == 12):
    print("The entered month is Dec., and the number of days in Dec. is 31.")


#Problem 8
import turtle
wn = turtle.Screen()
tri = turtle.Turtle()

twoDs = int(input("Please enter a two digit integer: "))
if (twoDs < 10) or (twoDs > 99):
    print("Integer is less than 10 or bigger than 99")
oneth = twoDs % 10
tenth = (twoDs // 10)

tri.pensize(5)

if (twoDs % 2 == 0):
    tri.color("red")
else:
    tri.color("black")

if (oneth == 0):
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.right(90)

if (oneth == 1):
    tri.right(90)
    tri.forward(100)
    tri.left(90)

if (oneth == 2):
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)

if (oneth == 3):
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.backward(50)
    tri.left(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.right(180)

if (oneth == 4):
    tri.right(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.backward(100)
    tri.right(90)

if (oneth == 5):
    tri.backward(50)
    tri.right(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.right(180)

if (oneth == 6):
    tri.backward(50)
    tri.right(90)
    tri.forward(100)
    tri.left(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.left(180)

if (oneth == 7):
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.left(90)

if (oneth == 8):
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.backward(50)
    tri.right(90)
    tri.forward(50)

if (oneth == 9):
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.right(90)
    tri.forward(50)
    tri.right(180)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.left(90)
    tri.forward (50)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    
tri.penup()
tri.setpos(-110,0)
tri.pendown()

if (tenth == 0):
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.right(90)

if (tenth == 1):
    tri.right(90)
    tri.forward(100)
    tri.left(90)

if (tenth == 2):
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)

if (tenth == 3):
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.backward(50)
    tri.left(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.right(180)

if (tenth == 4):
    tri.right(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.backward(100)
    tri.right(90)

if (tenth == 5):
    tri.backward(50)
    tri.right(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(50)
    tri.right(180)

if (tenth == 6):
    tri.backward(50)
    tri.right(90)
    tri.forward(100)
    tri.left(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.left(180)

if (tenth == 7):
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.left(90)

if (tenth == 8):
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.backward(50)
    tri.right(90)
    tri.forward(50)

if (tenth == 9):
    tri.forward(50)
    tri.right(90)
    tri.forward(100)
    tri.right(90)
    tri.forward(50)
    tri.right(180)
    tri.forward(50)
    tri.left(90)
    tri.forward(50)
    tri.left(90)
    tri.forward (50)
    tri.right(90)
    tri.forward(50)
    tri.right(90)
