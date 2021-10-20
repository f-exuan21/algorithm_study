# 곱하기 혹은 더하기

num = list(map(int, input()))

for n in range(1, len(num)):
	num[n] = max(num[n - 1] + num[n], num[n - 1] * num[n])

print(num[len(num) - 1])
