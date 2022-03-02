class Solution:
    def isMatch(self, s: str, p: str) -> bool:  
        # notes[i][j] = p에서 i-1까지랑 s에서 j-1까지가 일치하는가
        # 각각의 P가 S의 요소와 일치하는지를 boolean값으로 저장
        notes = []
        # 처음 값을 False로 초기화
        for i in range(len(p) + 1):
            notes.append([False] * (len(s) + 1))
        
        # 빈 string은 항상 true
        notes[0][0] = True
        
        # *는 빈 공간을 차지할 수 있다.
        # 그래서 이전 값을 계승(빈 공간이기 때문)
        for i in range(len(p)):
            if p[i] == "*":
                notes[i + 1][0] = notes[i + 1 - 1][0]

        for i in range(len(p)):
            for j in range(len(s)):
                # i번째 p가 *이면 현재 notes[i+1][j+1] 은 현재 p[i]까지랑 s[j-1]이 일치하거나
                # 이전 p[i-1]랑 s[j-1]이 일치하거나
                # 이전 p[i-1]랑 현재 s[j] 가 일치
                # 위 3개중 한 경우라도 일치하면 참
                if p[i] == '*':
                    notes[i + 1][j + 1] = notes[i + 1][j + 1 -1] or notes[i + 1 -1][j + 1 -1] or notes[i + 1 -1][j + 1]
                else:
                    # p가 ?이거나 정확히 s의 값이랑 일치하는 경우
                    # 이전까지의 p[i-1] s[j-1]가 true면 현재 p[i] s[j]도 일치
                    if p[i] == '?' or p[i] == s[j]:
                        notes[i + 1][j + 1] = notes[i + 1 - 1][j + 1 - 1]
                    # 나머지 경우는 false
                    else:
                        notes[i + 1][j + 1] = False

        return notes[len(p)][len(s)]