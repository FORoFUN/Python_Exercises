import turtle

#Problem 1, a
n = int(input("Please enter a positive integer: "))
pattern_symbol = "."
pattern_space = " "
for counter in range(n):
    line = pattern_space * (n- counter - 1) + pattern_symbol * (counter + 1) + pattern_symbol * counter
    print(counter," ", line)

#Problem 1, b
n = int(input("Please enter a positive integer: "))
pattern_diagonal = "%"
pattern_upper = "$"
pattern_lower = "#"
for counter in range(n):
    line = pattern_lower * counter + pattern_diagonal + pattern_upper * (n - counter - 1)
    print(counter," ", line)

#Problem 2
n = int(input("Please eneter a positive integer: "))
total = 0
for current_number in range(1,n+1):
    total = total + current_number**3
    
print("The result is", total)

#Problem 3, a
enter_string = input("Please enter a string: ")
find_character  = input("Please enter a character: ")
currence_number = 0
for char in enter_string:
    if (char == find_character):
        currence_number = currence_number + 1

print("The letter: ",find_character," appears", currence_number,"time(s) in the string.")

#Problem 3, b
enter_string = input("Please enter a string: ")
find_character  = input("Please enter a character: ")
currence_number = 0
string_length = 0
while string_length <= len(enter_string):
    if (find_character == enter_string[string_length]):
        currence_number = currence_number + 1
    string_length = string_length + 1

print("The letter: ",find_character," appears", currence_number,"time(s) in the string.")

#Problem 4, a
n = input("Please enter an interger: ")
odd_number = 0
even_number = 0
for each_num in n:
    if  (each_num == "1" or each_num == "3" or each_num == "5" or each_num == "7" or each_num == "9"):
        odd_number = odd_number + 1
    elif (each_num == "2" or each_num == "4" or each_num == "6" or each_num == "8"):
        even_number = even_number + 1

print("There are", odd_number,"of odd digit(s) and", even_number," of even digit(s) in the string")


#Problem 4, a
n = input("Please enter an interger: ")
odd_number = 0
even_number = 0
for each_num in n:
    if  (each_num == "1" or each_num == "3" or each_num == "5" or each_num == "7" or each_num == "9"):
        odd_number = odd_number + 1
    elif (each_num == "2" or each_num == "4" or each_num == "6" or each_num == "8"):
        even_number = even_number + 1

print("There are", odd_number,"of odd digit(s) and", even_number," of even digit(s) in the string")

#Problem 4, b
n = input("Please enter an interger: ")
odd_number = 0
even_number = 0

for each_num in n:
    each_num = int(each_num)
    if (each_num % 2 == 1):
        odd_number = odd_number + 1
    elif (each_num % 2 == 0):
        even_number = even_number + 1
        
print("There are", odd_number,"of odd digit(s) and", even_number," of even digit(s) in the string")

#Problem 5
wn = turtle.Screen()
gons = turtle.Turtle()

sides = int(input("Please enter a positive integer: "))
angle = 180 * (sides - 2) / sides
count = 0

while count < sides:
    gons.forward(50)
    gons.left(180 - angle)
    count += 1

#Problem 6
limit = int(input("Please enter a positive integer: "))
current_cube = 0
for num_to_cube in range(1, limit + 1):
    current_cube = num_to_cube**3
    if (current_cube <= limit):
        print(current_cube)





















    






