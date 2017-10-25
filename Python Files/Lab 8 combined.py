#Problem 1
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
    fib_string = fib_string + str(fib(num)) + ", "
print(fib_string[:len(fib_string)-2])  

print("The",n,"-th numbers is: ",fib(n))

for num in range(0,n):
    fib(num)
    print(fib(num))  

#problem 2 

some_string = input("Please enter a DNA string: ")
sub_string = input("Please enter a DNA sub-string: ")
start = int(input("Please enter a start: "))
end = int(input("Please enter an end: "))

def find(some_string,sub_string,start,end):
    n = start
    length_sub_string = len(sub_string)
    length = end + 1
    while (n < length):
        if (length_sub_string + n <= length) and (some_string[n:length_sub_string + n] == sub_string):
            return n
        n += 1
    return -1
                
def find_multi(some_string,sub_string,start,end):
    n = start
    location = ""
    length_sub_string = len(sub_string)
    length = end + 1
    while (n < length):
        if (length_sub_string + n <= length) and (some_string[n:length_sub_string + n] == sub_string):
            location = location + str(n) + " "
        n += 1
    return location

def both():
    print(find(some_string,sub_string,start,end))
    print(find_multi(some_string,sub_string,start,end))
    
both()



