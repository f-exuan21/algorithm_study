# 1이 될 때까지

n, k = map(int, input().split())
result = 0

while True:
	if n % k == 0:
		n /= k
		result += 1
	else:
		n -= 1 # 숫자가 커지면 반복문이 오래걸림
		result += 1
	if n == 1:
		break

print(result)
