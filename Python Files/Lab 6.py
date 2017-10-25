# Problem 1
phrase = input("What is the phrase? ")
phrase = phrase.lower()
length = len(phrase)

if (length % 2 == 1):
    middle = length // 2 + 1
    part_one = phrase[:middle - 1]
    part_two = phrase[middle:]
elif  (length % 2 == 0):
    middle = length // 2
    part_one = phrase[:middle]
    part_two = phrase[middle:]

for char in range(0,len(part_one)):
    first_half = part_one[char]
    
for char in range(len(part_two),0,-1):
    second_half = part_two[char - 1]
    
if (first_half == second_half):
    print("It is a palondrome")
else:
    print("It is not a palindrome")

#Problem 2
n = int(input("Enter a number: "))
symbol = "* "

for each in range(n):
    line = symbol * (each + 1)
    print(line)
for each in range(n - 1):
    line = symbol * (n - each -1)
    print(line)
    
