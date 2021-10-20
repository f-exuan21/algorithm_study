n = int(input())
players = list(map(int, input().split()))

players.sort()

cnt = 0
result = 0
for i in players:
	cnt += 1
	if cnt >= i:
		result += 1
		cnt = 0

print(result)
