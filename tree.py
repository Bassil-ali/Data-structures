class Node:
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None


def sumTree(ele):
    if(ele == None):
        return 0
    return (ele.item + sumTree(ele.left) + sumTree(ele.right))

def printTree(ele):
    if(ele == None):
        return 0
    print(ele.item)
    printTree(ele.left)
    printTree(ele.right)

# add int to tree
one = Node(1)
tow = Node(2)
three = Node(3)
four = Node(4)
fife = Node(5)
six = Node(6)

#connect tree
one.left = tow
one.right = three
tow.left = four
tow.right = fife
three.right = six 

#print tree
print("tree item is: ")
printTree(one)

#sum tree
print("sum tree items is: ")
print(sumTree(one))