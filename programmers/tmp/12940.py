def solution(n, m):
    ans = []
    gcd = 0
    for i in range(1, n+1):
        if n % i  == 0 and m % i == 0:
            gcd = max(gcd, i)
    ans.append(gcd)
    
    lcm = max(n, m)
    
    while True:
        if lcm % n == 0 and lcm % m == 0:
            ans.append(lcm)
            break
        lcm += 1
    return ans