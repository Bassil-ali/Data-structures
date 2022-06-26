
class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def deleteNode(self,key):
        node = self.head
       
        #search key in list
        while(node is not None):
            if node.item == key:
                break
            #set item to prev if exist
            prev = node
            #get the second element to node
            node = node.next
            if(node == None):
                return
            #set second item to node this is delete change next value
            prev.next = node.next
            #delete node content
            node = None
        
    def print(self):
        node = self.head
        while(node):
          print(node.item)
          node = node.next



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