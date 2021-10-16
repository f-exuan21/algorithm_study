n, k = map(int, input().split())
result = 0

while True:
	target = (n // k) * k # n보다 작은 k의 배수 중 가장 큰 값
	result += (n - target)
	n = target
	if n < k:
		break
	result += 1
	n //= k

result += (n - 1)
print(result)
