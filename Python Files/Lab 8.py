#Problem 1 A
n = int(input("Please enter a number: "))
    
def fib(n):
    if(n <= 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print("The first",n,"numbers in Fibonacci sequence are: ")

fib_string = ""
for num in range(0,n):
    fib(num)
    fib_string = fib_string + str(fib(num)) + "  "
print(fib_string)   

#Problem 1 B

n = int(input("Please enter a number: "))
    
def fib(n):
    if(n <= 1):
        return 0
    elif (n == 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
fib(n)
print("The",n,"-th numbers is: ",fib(n))

#Problem 1 C

n = int(input("Please enter a number: "))
    
def fib(n):
    if(n <= 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print("The first",n,"numbers in Fibonacci sequence are: ")

for num in range(0,n):
    fib(num)
    print(fib(num))  

#problem 2 A

some_string = input("Please enter a DNA string: ")
sub_string = input("Please enter a DNA sub-string: ")

def find():
    n = 0
    length_sub_string = len(sub_string)
    length = len(some_string)
    while (n < length):
        if (length_sub_string + n <= length) and (some_string[n:length_sub_string + n] == sub_string):
            return n
        n += 1
    return -1
print(find())
                
#problem 2 B

some_string = input("Please enter a DNA string: ")
sub_string = input("Please enter a DNA sub-string: ")

def find_multi():
    n = 0
    location = ""
    length_sub_string = len(sub_string)
    length = len(some_string)
    while (n < length):
        if (length_sub_string + n <= length) and (some_string[n:length_sub_string + n] == sub_string):
            location = location + str(n) + " "
        n += 1

        return location
    
print(find_multi())
                
#problem 2 C    

def both():
    some_string = input("Please enter a DNA string: ")
    sub_string = input("Please enter a DNA sub-string: ")
    print(find())
    print(find_multi())
both()


