from random import randint
import csv
#Problem Part I
my_file = open("input.txt", "r")
print(my_file.readline(),end = "")
print("--something--")
for r in my_file:
    print(r, end = "")

print()

#Problem Part II 1
def writeName(filename, firstName, lastName):
    my_file = open(filename,"w")
    line = firstName + " " + lastName
    my_file.write(line)
    my_file.write("\n")
    my_file.close()

def main_1():
    filename = "lab11_q1.txt"
    firstName = input("Please enter the first name: ")
    lastName = input("Please enter the last name: ")
    writeName(filename, firstName, lastName)
    
main_1()

#Problem 2

def writeRandNumbers(filename,n):
    my_file_2 = open(filename,"w")
    for repeat in range(n):
        rand_num = str(randint(1,100))
        my_file_2.write(rand_num)
        my_file_2.write("\n")
    my_file_2.close()

def main_2():
    filename = "lab11_q2.txt"
    n= int(input("How many random integers do you wanna generate? "))
    writeRandNumbers(filename,n)

main_2()

#Problem 3

def sumColumn(filename):
    my_file_3 = open(filename,"r")
    total = 0
    for num in my_file_3:
        num = int(num)
        total += num
    my_file_3.close()
    with open("lab11_q3.txt","w") as my_file_sum:
        total = str(total)
        my_file_sum.write(total)
    return total

def main_3():
    filename = "lab11_q2.txt"
    print(sumColumn(filename))

main_3()

#Problem 4

def html_table_generator(filename):
    my_file_4 = open(filename,"r")
    csv_list = csv.reader(my_file_4)
    file_list = []
    for row in csv_list:
        file_list.append(row)
    length = len(file_list)
    lines = 1
    
    final_string = "<table>" + "\n" + "\t" + "<tr>" + "\n"
    for header in file_list[0]:
        final_string += "\t\t" + "<th>" + header + "</th>" + "\n"
    final_string += "\t" + "</tr>" + "\n"
    
    while (lines < length):
        final_string += "\t" + "<tr>" + "\n"
        for position in file_list[lines]:
            final_string += "\t\t" + "<td>" + position + "</td>" + "\n"
        final_string += "\t" + "</tr>" + "\n"
        lines += 1
        
    final_string += "</table>" + "\n" + "</html>"
    
    my_file_4.close()
    
    ending_file = open("lab11_q4.html","w")
    ending_file.write(final_string)
    ending_file.close()
    
def main_4():
    filename = input("lab11_q4_samplefile1-windows.csv or  lab11_q4_samplefile2-windows.csv?: ")
    html_table_generator(filename)

main_4()
