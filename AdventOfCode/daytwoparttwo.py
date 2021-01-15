valid_passwords = 0
number_list = []
variable_list = []
passwords_list = []
#read each line of code -> find min and max -> variable required -> password

def checkPasswords():
    global valid_passwords
    counter = 0
    for i in range(0, len(passwords_list)):
        password = passwords_list[i]
        variable = variable_list[i]
        position1 = int(number_list[counter])
        position2 = int(number_list[counter+1])
        vaild1 = False
        valid2 = False
        position_counter = 1

        for letter in password:
            if letter == variable:
                if (position1 == position_counter):
                    vaild1 = True
                if (position2 == position_counter):
                    valid2 = True
            position_counter = position_counter + 1

        if (((vaild1 == True) and (valid2 == False)) or ((vaild1 == False) and (valid2 == True))):
            valid_passwords = valid_passwords + 1
        counter = counter + 2

def getFile():
    counter = 1
    var_counter = 0
    f = open("passwordsfile.txt", "r")
    for line in f:
        line = line.strip()
        for word in line.split():
            if counter == 1:
                item = word.split("-")
                for number in item:
                    number_list.append(number)
                counter = 2
            elif counter == 2:
                item2 = word.split(":")
                for var in item2:
                    if var_counter % 2 == 0:
                        var_counter = var_counter + 1
                        variable_list.append(var)
                    elif var_counter % 2 != 0:
                        var_counter = var_counter + 1
                counter = 3
            elif counter == 3:
                passwords_list.append(word)
                counter = 1
    print("Data of File gathered and file closed")

    f.close()

def main():
    print("Getting file with passwords")
    getFile()
    #fix the number list and fix the variable list
    print("Getting an estimation of the number of vaild Passwords")
    print()
    checkPasswords()
    print("The number of valid passwords are " + str(valid_passwords))
    

if __name__ == "__main__":
    main()