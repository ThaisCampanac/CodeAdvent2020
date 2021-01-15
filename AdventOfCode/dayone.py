list = []
first_int = 0
second_int = 0
third_int = 0

def find_2000():
    global first_int
    global second_int
    global third_int
    for i in range(0, len(list)):
        for j in range(1, len(list)):
            for k in range(2, len(list)):
                sum = int(list[i]) + int(list[j]) + int(list[k])
                if sum == 2020:
                    print(str(sum))
                    print(str(list[i]))
                    print(str(list[j]))
                    print(str(list[k]))
                    first_int = int(list[i])
                    second_int = int(list[j])
                    third_int = int(list[k])
                    return first_int*second_int*third_int
        
    return first_int*second_int*third_int

def create_list():
    f = open("file.txt","r")
    for line in f:
        line = line.strip()
        list.append(int(line))
    f.close()
    print("List created and file closed")
    return 0
         

def main():
    print("Getting file with integers")
    create_list()
    print(list)
    mult = find_2000()
    print("The multiplication of both " + str(first_int) + " and " + str(second_int) + " and " + str(third_int) + " is " + str(mult))

if __name__ == "__main__":
    main()