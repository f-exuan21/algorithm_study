#  31번

for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(arrayh[index:index + m])
        index += m

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            if i ==  n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j + 1]
            left = dp[i][j -1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
        resutl = 0
        for i in range(n):
            result = max(result, dp[i][m - 1])

        print(result)

# 32번
n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))
    for i in range(1, n):
        for j in range(i + 1):
            if  j == 0:
                up_left = 0
            else:
                up_left = dp[i - 1][j - 1]
            if j == 1:
                up == 0
            else:
                up = dp[i - 1][j]
            dp[i][j] = d[i][j] + max(up_left, up)

print(max(dp[n - 1]))

# 33번 퇴사
n = int(input())
t = []
p = []
dp = [0] * (n + 1)
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n - 1, -1, -1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)

# 34번
n = int(input())
array = list(map(int, input().split()))
array.reverse()

dp = [1] * n
for i in range(1, n):
    for j in range(0, 1):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))

#35번 못생긴 수
n = int(input())

ugly = [0] * n
ugly[0] = 1

i2 = i3 = i5 = 0

next2, next3, next5 = 2,3,5

for l in range(1, n):
    ugly[l] = min(next2, next3, next5)
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = uply[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n - 1])

# 36번
def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = i

    for j in range(1, m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

str1 = input()
str2 = input()

print(edit_dist(str1, str2))

