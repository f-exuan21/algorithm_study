# 부품 찾기 - 이진 탐색 이용

def binary_search(array, target, start, end):
	if start > end:
		return None
	mid = (start + end) // 2
	if target == array[mid]:
		return mid
	elif target < array[mid]:
		return binary_search(array, target, start, mid - 1)
	else:
		return binary_search(array, target, mid + 1, end)

n = int(input()) # 부품 개수
array = list(map(int, input().split())) # 가게에 있는 부품들
array.sort()

m = int(input()) # 손님이 요구하는 부품 개수
x = list(map(int, input().split())) # 손님이 요구하는 부품들

for i in x:
	find = binary_search(array, i, 0, len(array) - 1)
	if find != None:
		print('yes', end=' ')
	else:
		print('no', end=' ')
