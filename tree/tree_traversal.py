class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# in, pre, post are DFS
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)
        
def preorder(root):
    if root is None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)

from collections import deque
#BFS
def level_order(root):
    ans = []
    if root == None:
        return ans
    q=deque()
    q.append(root)
    while len(q)!=0:
        lvl=[]
        for i in range(len(q)):
            x=q[0]
            q.popleft()
            if x.left != None:
                q.append(x.left)
            if x.right != None:
                q.append(x.right)
            lvl.append(x.data)
        ans.append(lvl)
    return ans

def level_order_(root):
    ans = []
    if root == None:
        return ans
    q=deque()
    q.append(root)
    while len(q)!=0:
        lvl=[]
        for i in range(len(q)):
            x=q[0]
            q.popleft()
            if x is not None:
                if x.left != None:
                    q.append(x.left)
                else:
                    q.append(None)
                if x.right != None:
                    q.append(x.right)
                else:
                    q.append(None)
                lvl.append(x.data)
            else:
                lvl.append(None)
        ans.append(lvl)
    return ans
     
def level_order_1(root):
    ans = []
    if root == None:
        return ans
    q=deque()
    q.append(root)
    while len(q)!=0:
        for i in range(len(q)):
            x=q[0]
            q.popleft()
            
            if x is not None:
                if x.left != None:
                    q.append(x.left)
                else:
                    q.append(None)
                if x.right != None:
                    q.append(x.right)
                else:
                    q.append(None)
                ans.append(x.data)
            else:
                ans.append(None)
            
    return ans
    

def left_boundry(root, lb):
    if root.left is None and root.right is None:
        return
    lb.append(root.data)
    if root.left:
        left_boundry(root.left, lb)
    else:
        left_boundry(root.right, lb)

def right_boundry(root, rb):
    if root.left is None and root.right is None:
        return
    rb.append(root.data)
    if root.right:
        right_boundry(root.right, rb)
    else:
        right_boundry(root.left, rb)        

def leaf_boundry(root, lfb):
    if root is None:
        return
    leaf_boundry(root.left, lfb)
    if root.left is None and root.right is None:
        lfb.append(root.data)
    leaf_boundry(root.right, lfb)

a = Node(1)
a.left = Node(2)
a.right = Node(3)

a.left.left = Node(4)
a.left.right = Node(5)

a.right.left = Node(6)

#a.right.left.right = Node(7)

postorder(a)
'''
lb=[]
left_boundry(a.left,lb)
print(lb)

rb=[]
right_boundry(a.right, rb)
print(rb)

lfb=[]
leaf_boundry(a,lfb)
print(lfb)

print("Clock-wise boundry : ",a.data, rb,lfb[::-1],lb[::-1], a.data)
print("Anti-Clock-wise boundry : ",a.data, lb, lfb, rb[::-1], a.data)
'''
# print("inoredr = ")
# inorder(a)

# print("\npreoredr = ")
# preorder(a)

# print("\npostoredr = ")
# postorder(a)

# print("\n level order = ")
# print(level_order(a))

# print(level_order_(a))

# print(level_order_1(a))

