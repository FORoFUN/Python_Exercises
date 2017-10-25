size = int(input("Some number: "))

for i in range(1, size +1):
    line=""
    for j in range( 1, i +1):
        line = line + str(i *j) + "\t"
    print(line)
