import sys
from copy import deepcopy
from collections import deque

sys.setrecursionlimit(100000)


def count_change(money, coins):
    cnt = 0
    result_set = set()

    def count_coins(total_money, money, idx, res_deque):
        nonlocal cnt, result_set
        if total_money == money:
            result_set.add(''.join(sorted(list(res_deque))))
            return
        elif total_money < money:
            return

        for i in range(idx, len(coins)):
            count_coins(total_money, money, i + 1, res_deque)
            res_deque.append(str(coins[i]))
            count_coins(total_money, money + coins[i], i, res_deque)
            count_coins(total_money, money + coins[i], i + 1, res_deque)
            res_deque.pop()

    count_coins(money, 0, 0, deque())
    return len(result_set)


print(count_change(4, [1,2]))
