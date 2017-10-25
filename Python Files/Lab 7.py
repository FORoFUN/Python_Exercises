#Problem 1

##a_string = input("Please enter a string of 0s and 1s: ")
##
##for index in range(0, len(a_string)):
##    count = 0
##    previous = index - 1
##    while index <= len(a_string) - 1:
##        if (a_string[index] == a_string[previous]):
##            count += 1
##            index += 1
##            print(count, str(a_string[previous]) + "'s")
##            count = 0
##        else:
##            count += 1
##            index += 1
##            print(count, str(a_string[index]) + "'s")


##a_string = input("Please enter a string of 0s and 1s: ")
##
##count = 0
##index = 0
##index_next = 1
##while (index_next <= len(a_string)):
##    while (a_string[index_next] != a_string[index]):
##        count = 1
##        index += 1
##        index_next += 1
##        print(count, str(a_string[index - 1]) + "'s")
##    else:
##        count = count + 1
##        index += 1
##        index_next += 1
##        print(count, str(a_string[index - 1]) + "'s")
##    print(index)
##    print(index_next)
    
a_string = input("Please enter a string of 0s and 1s: ")

count = 1
index = 1
index_next = 0
last = -1
second_last = -2
while (index < len(a_string)):
    while (index < len(a_string)) and (a_string[index] == a_string[index_next]):
        count += 1
        #print(index, count, str(a_string[index_next]) + "'s")
        index += 1
        index_next += 1
    print(count, str(a_string[index_next]) + "'s")
    count = 1
    index += 1
    index_next += 1
if (a_string[second_last] != a_string[last]):
    print(count, str(a_string[last]) + "'s")
    
#Problem 2
from random import randint
rand_num = randint(1,100)
print("I thought of a number between 1 and 100! Try to guess it")
a = ("Try to guess what it is: ")

while True:
    guess = int(input(a))
    if (guess == rand_num):
        print("Congrats! You guessed my number")
        break
    else:
        if (guess < rand_num):
            print("Wrong guess. My number is bigger than yours.")
        elif (guess > rand_num):
            print("Wrong guess. My number is smaller than yours.")
