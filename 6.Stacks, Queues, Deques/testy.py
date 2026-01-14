class Node:
    def __init__(self, data):
        self.data = data
        self.next = None;
        
head = Node(3)
head.next = Node(6)
head.next.next = Node(9)
head.next.next.next = Node(12)
head.next.next.next.next = Node(15)

head.next.next.next.next.next = head.next

temp = head
count = 0


while temp and count < 6:
    print(temp.data, end=" ")
    
    if temp.data % 2 == 0:
        temp.next , temp = temp , temp.next.next
    else:
        temp = temp.next
    
    count += 1