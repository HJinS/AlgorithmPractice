from itertools import permutations


def solution(k, dungeons):
    def check(dungeons, k):

        cnt = 0
        cur_k = k
        for dungeon in dungeons:
            req, use = dungeon
            if cur_k >= req:
                cur_k -= use
                cnt += 1
        return cnt

    ans = 0
    for item in permutations(dungeons, len(dungeons)):
        res = check(item, k)
        ans = max(ans, res)
    return ans
