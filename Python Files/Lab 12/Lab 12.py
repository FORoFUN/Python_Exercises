import math
#Problem 1
def add_entry(phonebook, name, phonenumber):
    phonebook[name] = phonenumber
    return phonebook

def check(number):
    status = True
    for char in number:
        if (char.isdigit() == False):
            status = False
    if (len(number) != 10):
        status = False
    return status

def lookup(phonebook, name):
    try:
        phone = phonebook[name]
        print(phone)
    except:
        print("This name:", name," does not exist in the phone book.")

def print_all(phonebook):
    for entry in phonebook:
        print(entry,phonebook[entry])
        
def main():
    raw_data = open("Lab12-phonebook.txt","r")
    phonebook = {}
    for entry in raw_data:
        entry_list = entry.split(" ")
        name = entry_list[0] + entry_list[1]
        number = entry_list[2]
        number = number.replace("\n","")
        check(number) 
        if (check(number) ==  False):
            print(name," has an invalid phone number")
        else:
            phonenumber = number
            add_entry(phonebook, name, phonenumber)
    print_all(phonebook)
    while True:
        name  = input("Who are you looking for: ")
        if (name.lower() == "done"):
            print("Thank you")
            break
        else:
            lookup(phonebook, name)
    myfunc()

#Problem 2
def myfunc():
    try:
        x = int(input("Please enter a number: "))
        y = int(input("Please enter a number: "))
        answer = x / y
        print(answer)
    except ValueError:
        print("Input must be numbers")
    except ZeroDivisionError:
        print("Infinity")

main()
