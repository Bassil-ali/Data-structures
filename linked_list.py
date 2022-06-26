
class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def deleteNode(self,key):
        temp = self.head
       
        #search key in list
        while(temp is not None):
            if temp.item == key:
                break
            #set item to prev if exist
            prev = temp
            #get the second element to temp
            temp = temp.next
            if(temp == None):
                return
            #set second item to temp this is delete change next value
            prev.next = temp.next
            #delete temp content
            temp = None
        
    def print(self):
        temp = self.head
        while(temp):
          print(temp.item)
          temp = temp.next



if __name__ == '__main__':

    linked_list = LinkedList()

    # Assign item values
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    # Connect nodes
    linked_list.head.next = second
    second.next = third
    third.next = fourth


     # Print the linked list item
    linked_list.print()
    
    linked_list.deleteNode(2)

    # Print the linked list item
    print("\nafter delete: ")
    linked_list.print()