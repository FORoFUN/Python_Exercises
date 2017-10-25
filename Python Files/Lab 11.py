#Problem Part 1
my_file = open("input.txt", "r")
print(my_file.readline(),end = " ")
print("--something--")
for r in my_file:
    print(r, end = " ")
      
