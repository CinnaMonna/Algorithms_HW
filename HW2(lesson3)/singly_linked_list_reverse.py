class Node:
  def __init__(self, value = None, next = None): 
    self.value = value
    self.next = next

class LinkedList:
  def __init__(self):  
    self.head = None
  
  def add_last(self, value):
    newNode = Node(value)
    if self.head is not None:
      current = self.head
      while current.next is not None:
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  def printList(self):
    current = self.head
    while current is not None:
      print(current.value)
      current = current.next

def reverseList(list):
  previous = None        
  current = list.head    
  following = current.next    

  while current is not None:
      current.next = previous 
      previous = current      
      current = following         
      if following is not None:            
          following = following.next  
  list.head = previous

lst = LinkedList()
for i in range(5):
    lst.add_last(i)

print("Linked List:")
lst.printList()
print("Reversed Linked List:")
reverseList(lst)
lst.printList()