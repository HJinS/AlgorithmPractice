t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    distance = y - x
    count = 0  # 이동 횟수
    move = 1  # count별 이동 가능한 거리
    move_plus = 0  # 이동한 거리의 합
    while move_plus < distance:
        count += 1
        move_plus += move  # count 수에 해당하는 move를 더함
        if count % 2 == 0 :  # count가 2의 배수일 때, 
            move += 1
    print(count)

'''
    틀림
    규칙 파악 문제
    총 distance별로 count, 마지막에 움직인 거리, route를 나열 하여 규칙을 찾아낸다.
'''