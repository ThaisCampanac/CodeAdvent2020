trees = 0
number_of_columns = 0
tree_map = []

def traverseMap():
    global trees
    i = 0
    while i < len(tree_map):
        if tree_map[i] == '#':
            trees = trees + 1

        i = i + number_of_columns + 3


def getMap():
    f = open("treemapfile.txt", "r")
    global number_of_columns
    first_line = 1
    for line in f:
        line = line.strip()
        
        for character in line:
            tree_map.append(character)
            if first_line == 1:
                number_of_columns = number_of_columns + 1
        first_line = first_line + 1

    f.close()

def main():
    print("Getting file with map")
    getMap()
    print(number_of_columns)
    print("Got Map and now traversing")
    traverseMap()
    print("The number of trees are " + str(trees))


if __name__ == "__main__":
    main()