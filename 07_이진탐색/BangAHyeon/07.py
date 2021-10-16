# 부품 찾기 (집합 자료형 이용)

n = int(input()) # 부품 개수
array = list(map(int, input().split())) # 가게에 있는 부품들
array.sort()

m = int(input()) # 손님이 요구하는 부품 개수
x = list(map(int, input().split())) # 손님이 요구하는 부품들

for i in x:
	if i in array:
		print('yes', end=' ')
	else:
		print('no', end=' ')
