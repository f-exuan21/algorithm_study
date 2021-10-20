# 볼링공 고르기

# 볼링공 개수, 볼링공 최대 무개
n, m = map(int, input().split())
balls = list(map(int, input().split()))

x = [0] * (m + 1)

for b in balls:
	x[b] += 1

result = 0
for i in x:
	n -= i
	result += i * n

print(result)
