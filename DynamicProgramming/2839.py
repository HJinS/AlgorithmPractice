n = int(input())
dp = [-1,-1]

def init():

    dp.append(-1)
    dp.append(1)
    dp.append(-1)
    dp.append(1)

def dpSugar():
    for i in range(6,n+1):
        if dp[i-3] == -1 and dp[i-5] == -1:
            dp.insert(i,-1)
        else:
            if dp[i-3] == -1:
                dp.insert(i,dp[i-5] + 1)
                #dp[i] = dp[i-5] + 1
            elif dp[i-5] == -1:
                dp.insert(i,dp[i-3] + 1)
                #dp[i] = dp[i-3] + 1
            else:
                dp.insert(i,min(dp[i-3],dp[i-5]) + 1)
                #dp[i] = min(dp[i-3],dp[i-5]) + 1

init()
dpSugar()
print(dp[n])