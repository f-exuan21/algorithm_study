# 피보나치 함수 - 메모이제이션
d = [0] * 100

def fibo(x):
	if x == 1 or x == 2:
		return 1

	if d[x] != 0: # 이미 계산한적 있는 문제라면 그대로 반환
		return d[x]
	# 계산한 적 없는 문제라면 점화식에 따라서 피보나치 결과 반환
	d[x] = fibo(x - 1) + fibo(x - 2)
	return d[x]

print(fibo(99))
