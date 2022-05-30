n = input()
menus = list(map(int, input().split()))
menus.sort(reverse=True)

candids = []
times = []
while menus:
    
    tmp = []
    sum = 10000
    t = 0
    for i in range(len(menus)):
        while sum > menus[i]:
            sum -= menus[i]
            t += 1
            tmp.append(menus[i])
        if sum == menus[i]:
            sum -= menus[i]
            t += 1
            tmp.append(menus[i])
            break
    if sum == 0:
        times.append(t)
        candids.append(tmp)
        
    menus.pop(0)
"""
for i in range(len(candids)):
    print("1인당 메뉴 개수: ", times[i], "  \n1인당 메뉴 분할\n")
    cur = candids[i][0]
    cnt = 1
    for j in range(1, len(candids[i])):
        cnt += 1
        if cur != candids[i][j] or j == (len(candids[i]) - 1):
            print(cur, " x ", cnt)
            cnt = 1
            cur = candids[i][j]
            
        
    print("--------------------")
"""
for candid in candids:
    print(candid, end='\n')
for time in times:
    print(time, end='\n')
