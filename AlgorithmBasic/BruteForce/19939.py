N, K = map(int, input().split())
oneToK = sum(list(range(1, K)))
if N - K < oneToK:
    print(-1)
else:
    diff = (N-K) - oneToK
    if diff // K >= 1:
        diff %= K
    
    if diff:
        print(K)
    else:
        print(K-1)