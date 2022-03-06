class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = [1 for i in range(N+1)]
        
        if s[0] == '0':
            return 0
        
        for i in range(1, len(s)):
            # i번째가 '0' 일경우
            if s[i] == '0':
                # i-1번째가 2보다 크면 나눌 수 없다 -> 0
                if int(s[i-1]) > 2 or int(s[i-1]) == 0:
                    return 0
                # i-1번째가 2보다 작으면 1가지 방법으로 나눌 수 있다.
                # s[i] = 0이고 s[i-1] < 2이니 이 두개를 붙여서 나눌 수 밖에 없다.
                # 두칸 앞에 것이랑 같아진다
                else:
                    dp[i+1] = dp[i-1]
            else:
                # s의 i-1 ~ i까지 가 26보다 크거나 i-1이 0이면 마지막에 한자리 숫자를 나누는 경우이다.
                if int(s[i-1:i+1]) > 26 or int(s[i-1]) == 0:
                    dp[i+1] = dp[i]
                # 나머지 경우는 끝에 숫자를 한자리 숫자로 나누거나 두자리 숫자로 나누는 경우이다.
                else:
                    dp[i+1] = dp[i] + dp[i-1]
        return dp[-1]
        