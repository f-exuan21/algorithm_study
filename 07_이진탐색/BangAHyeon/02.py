# 이진 탐색 (재귀함수)

def binary_search(array, target, start, end):
	if start > end:
		return None
	mid = (start + end) // 2
	if array[mid] == target:
		return mid
	elif array[mid] > target:
		return binary_search(array, target, start, mid - 1)
	else:
		return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split())) # 원소의 개수, 찾으려는 숫자
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
	print("원소가 존재하지 않습니다.")
else:
	print(result + 1)
