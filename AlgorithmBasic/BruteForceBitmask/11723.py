import sys
m = int(input())
set = 0b00000000000000000000
op = str()
n = int()

for i in range(m):
    inputStr = sys.stdin.readline()
    if inputStr.startswith('all') or inputStr.startswith('empty'):
        op, tmp = map(str, inputStr.split('\n'))
    else:
        op, num = map(str, inputStr.split())
        n = int(num)
    if op == 'add':
        mask = 1 << (n-1)
        set = set | mask
    elif op == 'remove':
        mask = 1 << (n-1)
        mask = ~mask
        set = set & mask

    elif op == 'check':
        mask = 1 << (n-1)
        if set & mask == mask:
            print("1")
        else:
            print("0")
    elif op == 'toggle':
        mask = 1 << (n-1)
        set = set ^ mask
    elif op == 'all':
        mask = (1 << 20) - 1
        set = set | mask
    elif op == 'empty':
        set = 0b00000000000000000000