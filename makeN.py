# 정수 N, M을 입력 받기
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력 받기
array = []
menus = [[] for i in range(m + 1)]
for i in range(n):
    array.append(int(input()))
array.sort()
# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [20000] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 20000: # (i - k)원을 만드는 방법이 존재하는 경우
            if (d[j] > (d[j - array[i]] + 1)):
                menus[j].append(array[i])
            d[j] = min(d[j], d[j - array[i]] + 1)
            
            

# 계산된 결과 출력
if d[m] == 20000: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
    print(menus[m])