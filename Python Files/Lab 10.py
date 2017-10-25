#Problem 1
def mycount(lst,item):
    count = 0
    for element in lst:
        if (str(element) == item):
            count += 1
    return count

#Problem 2
def myindex(lst,item):
    for position in range(0,len(lst)):
        if (str(lst[position]) == item):
            return position
        else:
            return -1

#Problem 3
def all_indices(lst,item):
    position_lst = []
    for position in range(0,len(lst)):
        if (str(lst[position]) == item):
            position_lst.append(position)
    if (position_lst == []):
        return -1
    else:
        return position_lst

#Problem 4
def remove_below_avg(lst_num):
    total = 0
    for element in lst_num:
        total += element
    average = total / len(lst_num)
    below_avg = []
    for element in lst_num:
        if (element >= average):
            below_avg.append(element)
    return below_avg

#Problem 1-4
def everything():
    lst = [123,'xyz','zara','abc',123]
    item = input("Please enter an item for different functions: ")
    lst_num = [2, 3, 5, 1, -4, 8, 0, -1]
    print(mycount(lst,item))
    print(myindex(lst,item))
    print(all_indices(lst,item))
    print(remove_below_avg(lst_num))

everything()

#Problem 5
from random import randint
def generate_computer():
    rand_num = randint(0,2)
    lst_of_inputs = ["rock","paper","scissor"]
    return lst_of_inputs[rand_num]

def decision(user,computer):
    if (user == "paper" and computer == "rock"):
        print("Paper beats rock, User won")
    if (user == "rock" and computer == "scissor"):
        print("Rock beats scissor, User won")
    if (user == "scissor" and computer == "paper"):
        print("Scissor beats paper, User won")
    if (user == "paper" and computer == "scissor"):
        print("Scissor beats paper, User lost")
    if (user == "rock" and computer == "paper"):
        print("Paper beats rock, User lost")
    if (user == "scissor" and computer == "rock"):
        print("Rock beats scissor, User lost")
    if (user ==  computer):
        print(user,"Ties")

def initial_input():
    user = input("Please enter 'rock','paper','scissor': ")
    print(generate_computer())
    computer = generate_computer()
    decision(user,computer)
    
def continue_read(user,computer):
    while True:
        if (user == "done"):
            break
        else:
            decision(user,computer)

def main():
    while True:
        user = input("Please enter 'rock','paper','scissor', or 'done': ")
        computer = generate_computer()
        if (user == "done"):
            break
        else:
            decision(user,computer)

main()
