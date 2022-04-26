def solution(n,a,b):
    # 규칙 문제
    # 몫과 나머지를 더한 값이 다음 라운드에서 번호임
    cnt=0
    while True:
        a = (a//2)+(a%2)
        b = (b//2)+(b%2)
        cnt+=1
        if a==b:
            break
    return cnt