# 럭키 스트레이트

n = list(map(int, input()))
length = len(n)
half = length // 2

if sum(n[:half]) == sum(n[half:]):
	print("LUCKY")
else:
	print("READY")
