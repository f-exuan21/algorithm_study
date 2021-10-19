# 곱하기 혹은 더하기

number = list(map(int, input()))

for i in range(1, len(number)):
	number[i] = max(number[i - 1] + number[i], number[i - 1] * number[i])

print(number[len(number) - 1])
