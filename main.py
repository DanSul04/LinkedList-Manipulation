class Node:
  def __init__(self, d):
    self.Data = d
    self.Next = None

class LinkedList:
  def __init__(self, d=None):
    if (d == None): # an empty list
      self.Header = None
      self.Current = None
    else:
      self.Header = Node(d)
    self.Current = self.Header

def nextCurrent(self):
  if (self.Current.Next is not None):
    self.Current = self.Current.Next
  else:
    self.Current = self.Header

def resetCurrent(self):
  self.Current = self.Header

def getCurrent(self):
  if (self.Current is not None):
    return self.Current.Data
  else:
    return None

def insertBeginning(self, d):
  if (self.Header is None): # if list is empty
    self.Header = Node(d)
    self.Current = self.Header
  else: # if list not empty
    Tmp = Node(d)
    Tmp.Next = self.Header
    self.Header = Tmp

def insertCurrentNext(self, d):
  if (self.Header is None): # if list is empty
    self.Header = Node(d)
    self.Current = self.Header
  else: # if list not empty
    Tmp = Node(d)
    Tmp.Next = self.Current.Next
    self.Current.Next = Tmp

def removeBeginning(self):
  if (self.Header is None): # if list is empty
    return None
  else: # if list not empty
    ans = self.Header.Data
    self.Header = self.Header.Next
    self.Current = self.Header
    return ans

def removeCurrentNext(self):
  if (self.Current.Next is None): # if there is no node
    return None # after Current
  else: # if there is
    ans = self.Current.Next.Data
    self.Current.Next = self.Current.Next.Next
    return ans

def printList(self,msg="====="):
  p = self.Header
  print("====",msg)
  while (p is not None):
    print(p.Data, end=" ")
    p = p.Next
  if (self.Current is not None):
    print("Current:", self.Current.Data)
  else:
    print("Empty Linked List")

# Create list
linkedlist = LinkedList()

# Insert Numbers
numbers = [76, 88, 11, 34, 56, 91]
for num in numbers:
linkedlist.insertBeginning(num)

# Print current status of list
print("Current Status of List: ")
linkedlist.printList()

# Push The Current to the third element of the list
linkedlist.nextCurrent()
linkedlist.nextCurrent()
linkedlist.nextCurrent()

# Remove the next to the Current element
linkedlist.removeCurrentNext()

# Insert 23 after Current
linkedlist.insertCurrentNext(23)

# Print Final List
print("Final List: ")
linkedlist.printList()

