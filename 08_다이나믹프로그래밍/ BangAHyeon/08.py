# 효율적인 화폐 구성

# 화폐 개수, 목표 돈
n, m = map(int, input().split())
array = []
for _ in range(n):
	array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
	for j in range(array[i], m + 1):
		if d[j - array[i]] != 10001:
			d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] != 10001:
	print(d[m])
else:
	print(-1)
