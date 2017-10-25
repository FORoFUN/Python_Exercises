#Problem 1

a = int(input("Please enter a non-zero number a : "))
b = int(input("Please enter a non-zero number b : "))

if (a>0) and (b>0):
    print("(",a,",",b,") is located in the first quadrant.")
elif (a<0) and (b>0):
    print("(",a,",",b,") is located in the second quadrant.")
elif (a<0) and (b<0):
    print("(",a,",",b,") is located in the third quadrant.")
elif (a>0) and (b<0):
    print("(",a,",",b,") is located in the forth quadrant.")
else:
    print("The two non-zero numbers, a and b, are not applicable.")
    
#Problem 2


#Problem 3

phone_number = input("Please enter the phone number (718-260-xxxx): ")
old_system = "718-260-"
new_system = "646-997-"

number_selection = phone_number[:8]

if (number_selection == old_system):
    phone_number = new_system + phone_number[8:]
    print("The new phone number is", phone_number)
else:
    print("That is not a valid old NYU SoE phone number.")
    
#Problem 4

import turtle
wn = turtle.Screen()
pic = turtle.Turtle()

color = input("Please enter a color: ")
shape = input("Please enter a shape: ")
size = int(input("Please enter a size: "))

pic.color(color)
pic.pensize(5)

if (shape == "triangle"):
    pic.forward(size)
    pic.left(120)
    pic.forward(size)
    pic.left(120)
    pic.forward(size)
    pic.left(120)
elif (shape == "square"):
    pic.forward(size)
    pic.left(90)
    pic.forward(size)
    pic.left(90)
    pic.forward(size)
    pic.left(90)
    pic.forward(size)
    pic.left(90)   
else:
    print("The shape entered is not supported.")

#Problem 5

three_word_phrase = input("Please enter a three-word phrase separated by one blank: ")

first_space = three_word_phrase.find(" ")
two_word_phrase = three_word_phrase[first_space + 1:]
second_space = two_word_phrase.find(" ")

first_word = three_word_phrase[0]
second_word = two_word_phrase[0]
third_word = two_word_phrase[second_space++1]

print(first_word, second_word, third_word)

word = input("Please enter a word: ")
print(str.upper(word))

three_letter_word = input("Please enter a three-letter word: ")


first_unicode = ord(three_letter_word[0])
second_unicode = ord(three_letter_word[1])
third_unicode = ord(three_letter_word[2])

print(first_unicode, second_unicode, third_unicode)

#Problem 6

password = input("Please enter a password: ")

password_upper = ""
for ch in password:
    if str.isupper(ch):
        password_upper = "true"
        
number_of_letters = len(password)
if (number_of_letters < 6):
    print("The password is not long enough.")
elif (password_upper == "false"):
    print("The password does not contain an uppercase letter.")
else:
    print("The password is valid.")
    
#Problem 7

s = input("Please enter two positive integers separated by one space: ")

break_point = s.find(" ")

first = int(s[:break_point])
second = int(s[break_point + 1:])

total = first + second
print(first,"+",second,"=",total)


#Problem 8

str_test = input("Please enter a string: ")

str_number = ""
for ch in str_test:
    if ("0" <= str_test <= "9"):
        str_number = "True"
    else:
        str_number = "False"
if (str_number == "True"):
    print("The string contains digits.")
else:
    print("The string does not contain digits.")
    
#Problem 9
import math
import turtle

x = int(input("Please enter a non-zero number x : "))
y = int(input("Please enter a non-zero number y : "))

angle_tri = math.degrees(math.atan(y/x))
angle_vec = math.degrees(math.atan2(y,x))
distance = math.sqrt(x**2 + y**2)

tangent = turtle.Screen()
tri = turtle.Turtle()

tri.pensize(5)

tri.forward(500)
tri.backward(1000)
tri.forward(500)
tri.left(90)
tri.forward(500)
tri.backward(1000)
tri.right(90)

tri.penup()
tri.setpos(0,0)
tri.pendown()

tri.pensize(2)

if (x>0) and (y>0):
    #first quadrant
    tri.left(angle_tri)
    tri.forward(distance)
elif (x<0) and (y>0):
    #second quadrant
    tri.left(180+angle_tri)
    tri.forward(distance)
elif (x<0) and (y<0):
    #third quadrant
    tri.right(180-angle_tri)
    tri.forward(distance)
elif (x>0) and (y<0):
    #fourth quadrant
    tri.right(-angle_tri)
    tri.forward(distance)
else:
    print("The two non-zero numbers, a and b, are not applicable.")
