N = int(input())

tree = {}

class Node:
    def __init__(self, item, lChild, rChild):
        self.item = item
        self.lChild = lChild
        self.rChild = rChild

def preOrder(node):
    print(node.item, end='')
    if node.lChild != '.':
        preOrder(tree[node.lChild])
    if node.rChild != '.':
        preOrder(tree[node.rChild])

def inOrder(node):

    if node.lChild != '.':
        inOrder(tree[node.lChild])
        
    print(node.item, end='')

    if node.rChild != '.':
        inOrder(tree[node.rChild])

def postOrder(node):

    if node.lChild != '.':
        postOrder(tree[node.lChild])

    if node.rChild != '.':
        postOrder(tree[node.rChild])
        
    print(node.item, end='')

for i in range(N):
    data = input().split()
    tree[data[0]] = Node(item=data[0], lChild=data[1], rChild=data[2])

preOrder(tree['A'])
print()
inOrder(tree['A'])
print()
postOrder(tree['A'])
print()