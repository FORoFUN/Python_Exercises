#Problem 1

kilograms = int(input("Please enter a number for kilogram amount: "))
pounds = kilograms * 2
ounces = kilograms * 0.2046 * 16
ounces_extra= ounces // 16
pounds_final = pounds + ounces_extra
ounces_final = kilograms * 0.2046 * 16 - (ounces_extra * 16)
print("%i fkilograms is "%(kilograms), "%i pounds and" %(pounds_final), " %.2f ounces" %(ounces_final))

#Problem 2

inches = int(input("Please enter a number for inch amount: "))
feet = inches // 12
inches_reminder = (inches - feet * 12) % 12

print(inches, "inches equals to %i" %(feet), "feet and %.2f inches" %(inches_reminder))

#Problem 3

import math
r = int(input("Please enter a number for radius amount: "))
circumference = r * math.pi * 2
area = r* r * math.pi
print("Circumference of the circle is %.2f" %(circumference), "and the area of the circle is %.2f" %(area))

#Problem 4

import turtle
#turtle.screen() a place to draw
wn = turtle.Screen()
#movement can be defined
tri = turtle.Turtle()
#movement: tri.foward//backward//upward//downward "unite"
tri.forward(100)
#.rt = rotate
tri.left(60)
#.left or .right, the arrow is turning to that direction with according to the original direction
tri.forward(100)
tri.left(60)
tri.forward(100)
tri.left(60)
tri.forward(100)
tri.left(60)
tri.forward(100)
tri.left(60)
tri.forward(100)
tri.left(60)

#Bonus Problem 1
print("Please enter the date in form of year month date (yyyymmdd")
birthday = int(input("Please enter a date of birth: "))
today = int(input("Please enter today's date: "))
birth_date = (birthday %100)
today_date = (today %100)

birth_month = (birthday // 100 %100) 
today_month = (today // 100 %100)

birth_year = (birthday // 10000)
today_year = (today // 10000)

days_in_total = today_date - birth_date + (today_month - birth_month) * 30 + (today_year - birth_year) * 365
years = days_in_total // 365
days_reminder_Y = days_in_total % 365
months = days_reminder_Y // 30
days = days_reminder_Y % 30

print("your are",str(years),"years, ",str(months),"months and", str(days),"days old")
#30 days in a month and 365 days in a year

#Bonus Problem 2
st_feet = int(input("Please enter the first length's feet: "))
st_inches = int(input("Please enter the first length's inches: "))
nd_feet = int(input("Please enter the second length's feet: "))
nd_inches = int(input("Please enter the second length's inches: "))
sub_feet = st_feet + nd_feet
sub_inches = st_inches + nd_inches
extra_feet = sub_inches // 12
inches = sub_inches % 12
Total_feet = sub_feet + extra_feet
print("Their sum is: ",Total_feet,"feet and", inches,"inches.")




