# 모험가 길드

n = int(input())
scared = list(map(int, input().split()))

scared.sort()

count = 0
result = 0

for i in scared:
	count += 1
	if count >= i:
		result += 1
		count = 0

print(count)
