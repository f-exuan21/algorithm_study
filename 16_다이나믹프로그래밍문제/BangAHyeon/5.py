# 못생긴 수

n = int(input())

numbers = [0] * 1001

numbers[1] = 1
for i in range(1, 200):
	if numbers[i] == 1:
		numbers[i * 2] = 1
		numbers[i * 3] = 1
		numbers[i * 5] = 1

cnt = 0
idx = 1
while cnt < n:
	if numbers[idx] == 1:
		cnt += 1
	idx += 1
print(idx-1)
