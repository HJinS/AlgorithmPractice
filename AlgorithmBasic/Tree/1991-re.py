N = int(input())


def preOrder(node):
    print(node.element, end='')
    if node.lChild != '.':
        preOrder(tree[node.lChild])
    if node.rChild != '.':
        preOrder(tree[node.rChild])

def inOrder(node):
    if node.lChild != '.':
        inOrder(tree[node.lChild])
    print(node.element, end='')
    if node.rChild != '.':
        inOrder(tree[node.rChild])

def postOrder(node):
    if node.lChild != '.':
        postOrder(tree[node.lChild])
    if node.rChild != '.':
        postOrder(tree[node.rChild])
    print(node.element, end='')

class Node:
    def __init__(self, element, lChild, rChild):
        self.element = element
        self.lChild = lChild
        self.rChild = rChild

tree = {}

for i in range(N):
    data = input().split()
    tree[data[0]] = Node(data[0], data[1], data[2])

preOrder(tree['A'])
print()
inOrder(tree['A'])
print()
postOrder(tree['A'])
