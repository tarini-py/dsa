from datetime import datetime
print(datetime.now().strftime("%Y-%m-%d %I:%M:%S %p"),'\n')

class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None


class LinkedList:
    def __init__(self,head=None, tail=None):
        self.head = head
        self.tail = tail
        
    def reverse_ll(self):
        prev = next = None
        current = temp = self.head
        
        while current.next:
            next = current.next
            current.next = prev
            
            prev = current
            current = next
            next = next.next
        current.next = prev
        self.head = current
        self.tail = temp
    
    def pop_front(self):
        if self.head is None:
            print("Empty LL")
        elif self.head == self.tail:
            print(self.head.value,' popped from front')
            temp = self.head
            self.head = self.tail = None
            del temp
        else:
            print(self.head.value,' popped from front')
            temp = self.head
            self.head = self.head.next
            temp.next = None
            del temp
        return
    
    def pop_back(self):
        if self.tail is None:
            print("Empty LL")
        elif self.head == self.tail:
            print(self.tail.value, 'popped from back')
            temp = self.head
            self.head = self.tail = None
            del temp
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
                
            print(self.tail.value, 'popped from back')
            temp = self.tail
            current.next = None
            self.tail = current
            del temp
            
            
        
        
    def insert(self, value, pos=None):
        if pos is None:
            self.push_back(value)
            return
        elif pos == 0:
            self.push_front(value)
            return
        else:
            current = self.head
            temp = Node(value)
            c=0
            while c<pos-1:
                if current.next is None:
                    self.push_back(value)
                    return
                current = current.next
                c+=1
            temp.next = current.next
            current.next = temp
            print(value, " inserted at ",pos)
            del temp
            
    def push_front(self,value):
        temp = Node(value)
        if self.head is None:
            self.head = self.tail = temp
        else:
            temp.next = self.head
            self.head = temp
        del temp
        print(value," pushed at front")
    
    def push_back(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        '''# for only head
        if self.head is None:
            self.head = temp
            return
        current = self.head
        while True:
            if current.next is None:
                current.next = temp
                break
            current = current.next
        '''
        del temp
        print(value,' pushed at back')

    def print_linked_list(self,n= None):
        current = self.head
        print()
        if n is None:
            while True:
                if current is None:
                    print("None")
                    break
                print(current.value,' -> ',end='')
                current = current.next 
        else:
            if isinstance(n,int) is False or n<0:
                raise ValueError("n must be a non-negative integer or None")
            count=0
            while True:
                if count == n:
                    break
                if current is None:
                    print("None")
                    break
                print(current.value,' -> ',end='')
                current = current.next
                count+=1



x=LinkedList()
x.print_linked_list()

x.pop_back()
x.pop_front()

x.push_back(346)
x.print_linked_list()
x.pop_back()
x.pop_front()



x.insert("First")
x.push_back("TPS")
x.push_front("Prasad")
x.push_front("Tarini")
x.push_back("Samantray")

x.print_linked_list()

x.insert(1000,99)
x.push_back(12)
x.insert(199,100)
x.print_linked_list()


x.pop_back()
x.pop_front()
x.print_linked_list()


x.insert("First")
x.push_back("TPS")
x.push_front("Prasad")
x.push_front("Tarini")
x.push_back("Samantray")

x.print_linked_list()

x.insert(1000,99)
x.push_back(12)
x.insert(199,100)
x.print_linked_list()


x.reverse_ll()
x.print_linked_list()

x.reverse_ll()
x.print_linked_list()

del x

