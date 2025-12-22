class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


a = Node(1)
a.left = Node(2)
a.right = Node(3)

a.left.left = Node(4)
a.left.right = Node(5)

a.right.left = Node(6)

a.right.left.right = Node(7)

a.right.left.right.right = Node(8)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorder(root, v, l, arr):
    if root is None:
        return
    inorder(root.left,v-1,l+1,arr)
    if v in arr:
        arr[v].append((root.val,l))
    else:
        arr[v]=[(root.val,l)]
    inorder(root.right,v+1,l+1,arr)
        

def verticalTraversal(root, ans, ans2):
    arr = dict()
    inorder(root, 0, 0, arr)
    print(arr)

    for k in arr:
        arr[k].sort(key=lambda x: x[1])
    print(arr)
    for k in (arr):
        ans.append(arr[k][0][0])
        ans2.append(arr[k][-1][0])

top_view=[]
bottom_view=[]
verticalTraversal(a,top_view,bottom_view)
print(top_view,'\n',bottom_view)

        