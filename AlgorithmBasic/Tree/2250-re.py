N = int(input())

class Node:
    def __init__(self, item, lChild, rChild):
        self.par = -1
        self.item = item
        self.lChild = lChild
        self.rChild = rChild
Tree = {}
MIN = [9876543 for i in range(N+1)]
MAX = [0 for i in range(N+1)]
max_level = 0
pos = 1

for i in range(1, N+1):
    Tree[i] = Node(i, -1, -1)

for i in range(N):
    item, l, r = map(int, input().split())
    Tree[item].lChild = l
    Tree[item].rChild = r
    if l != -1:
        Tree[l].par = item
    if r != -1:
        Tree[r].par = item

def inOrder(node, level):
    global pos, max_level
    max_level = max(max_level, level)
    if node.lChild != -1:
        inOrder(Tree[node.lChild], level+1)
    
    MIN[level] = min(MIN[level], pos)
    MAX[level] = max(MAX[level], pos)
    pos += 1

    if node.rChild != -1:
        inOrder(Tree[node.rChild], level+1)

root = None
for i in range(1, N+1):
    if Tree[i].par == -1:
        root = i

inOrder(Tree[root], 1)

width_L = 1
for i in range(2, N+1):
    if MAX[i] - MIN[i] > MAX[width_L] - MIN[width_L]:
        width_L = i

print(width_L, MAX[width_L] - MIN[width_L] + 1)