class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # kmp 알고리즘 공부할 것
        n = len(s)
        rev = s[::-1]
        s_new = s + "#" + rev

        n_new = len(s_new)
        # 각 index를 끝으로 반복되는 구간의 길이
        # ex) cacac 이면 index 0에서 cac index 2에서 cac가 반복됨
        f = [0 for i in range(n_new)]
        
        for i in range(1, n_new):
            # 이전 인덱스(i-1) 의 반복되는 길이의 인덱스부터 확인하면 됨
            t = f[i-1]
            while t > 0 and s_new[i] != s_new[t]:
                t = f[t-1]
            if s_new[i] == s_new[t]:
                t += 1
            f[i] = t

        return rev[:n-f[n_new-1]] + s