#Problem 1a
def count(lst, item):
    counter = 0
    for element in lst:
        if (element == item):
            counter += 1
    return counter

#Problem 1b
def power_2():
    power = int(input("Please enter a number for nth power of 2: "))
    lst_2 = []
    for num in range(1,power + 1):
        lst_2.append(2 ** num)
    print(lst_2)
        
#Ptoblem 1c
def find_min_index(lst):
    min_so_far = lst[0]
    for element in lst:
        if (element < min_so_far):
            min_so_far = element
    return min_so_far

#Problem 1d
def circular_shift_list1(lst,k):
    new_lst = []
    change = k % len(lst)
    begin = lst[:change]
    end = lst[change:]
    new_lst.extend(end)
    new_lst.extend(begin)
    return new_lst

#Problem 1e
def circular_shift_list2(lst,k):
    k = k % len(lst)
    return lst[k:] + lst[:k]

#Problem 1
def main_list():
    k = int(input("Please enter a number for shift: "))
    lst = list(input("Please enter a list: "))
    item = input("Please enter a matching item: ")
    print(count(lst, item))
    print(find_min_index(lst))
    print(circular_shift_list1(lst,k))
    print(circular_shift_list2(lst,k))
    power_2()
    
#Problem 2
def get_Common_Ele(list1,list2):
    similar = []
    for element in list1:
        for matching in list2:
            if (element == matching):
                similar.append(element)
    return similar

def main_similar():
    list1 = list(input("Please enter a list: "))
    list2 = list(input("Please enter a list: "))
    print(get_Common_Ele(list1,list2))
    
#Problem 3
def sum_of_squares(list1):
    total = 0
    for element in list1:
        total += element ** 2
    return total

def main_sum():
    sequence = ("Please enter numbers to create a sequence: ")
    list1 = []
    while True:
        number = (input(sequence))
        if (number == "done"):
            break
        else:
            number = int(number)
            list1.append(number)
        print(list1)
    print(sum_of_squares(list1))

#Problem 4
def secret():
    from random import randint
    rand_num = randint(1000,9999)
    secret = [rand_num // 1000, rand_num // 100 % 10, rand_num // 10 % 10, rand_num % 10]
    return secret

def result(secret_list):
    guess_num_try = ("Try to guess what it is: ")
    while True:
        guess_num = int(input(guess_num_try))
        listG = guess(guess_num)
        if (listG == secret_list):
            print("Congrats! You have guessed my number")
            break
        else:
            print("There are",bulls(guess_num,secret_list),"bull(s) and",cows(guess_num,secret_list),"cow(s).")

def guess(guess_num):
    listG = [guess_num // 1000, guess_num // 100 % 10, guess_num // 10 % 10, guess_num % 10]
    return listG

def bulls(guess_num,secret_list):
    bulls = 0
    for position in range(4):
        if (secret_list[position] == guess(guess_num)[position]):
            bulls += 1
    return bulls

def cows(guess_num,secret_list):
    cows_num = 0
    for position in range(4):
        element = secret_list[position]
        for position2 in range(4):
            matching = guess(guess_num)[position2]
            if not(element == matching) and (secret_list[position] == guess(guess_num)[position]):
                cows_num += 1
    return cows_num

def main():
    secret_list = secret()
    print(secret_list)
    print("Welcome to the game of Bulls and Cows!") 
    print("I will generate a number, and you have to guess the numbers")
    result(secret_list)

main_list()
main_similar()
main_sum()
main()
