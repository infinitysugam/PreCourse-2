#Time Complexity = O(n)
#Space Complexity = O(1)

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data
        self.next = None  
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data):
        new_node = Node(new_data)

        curr = self.head
        if not curr:
            self.head = new_node
            return

        while curr.next:
            curr=curr.next
        curr.next = new_node

        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            fast=fast.next.next
            slow = slow.next
        print(slow.data)



# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
