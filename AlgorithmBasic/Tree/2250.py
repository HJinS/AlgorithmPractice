N = int(input())

tree = {}
MIN = [10000000 for i in range(10001)]
MAX = [0 for i in range(10001)]
pos = 1
max_level = 0
class Node:
    def __init__(self, item, lChild, rChild):
        self.par = -1
        self.item = item
        self.lChild = lChild
        self.rChild = rChild

def inOrder(node, level):
    global pos, max_level

    max_level = max(max_level, level)

    if node.lChild != -1:
        inOrder(tree[node.lChild], level + 1)

    MIN[level] = min(MIN[level], pos)
    MAX[level] = max(MAX[level], pos)
    pos += 1
    if node.rChild != -1:
        inOrder(tree[node.rChild], level + 1)

for i in range(1, N+1):
    tree[i] = Node(i, -1, -1)

for i in range(N):
    item, l, r = map(int, input().split())
    tree[item].lChild = l
    tree[item].rChild = r
    if l != -1:
        tree[l].par = item
    if r != -1:
        tree[r].par = item

root = 1
while tree[root].par != -1:
    root = tree[root].par

inOrder(tree[root], 1)

tmp = 1

for i in range(1, max_level + 1):
    if MAX[i] - MIN[i] > MAX[tmp] - MIN[tmp]:
        tmp = i

print(tmp, MAX[tmp] - MIN[tmp] + 1)