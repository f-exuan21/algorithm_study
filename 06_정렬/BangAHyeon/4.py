# 퀵 정렬

array = [7, 5, 9, 0, 3, 1, 6, 4, 2, 8]

def quick_sort(array, start, end):
	if start >= end: # 원소가 1개인 경우 종료
		return
	pivot = start
	left = start + 1
	right = end
	while left <= right:
		# 피벗보다 큰 데이터를 찾을 때까지 반복
		while left <= end and array[left] <= array[pivot]:
			left += 1
		while right > start and array[right] >= array[pivot]:
			right -= 1
		# left와 right가 교차했을 경우
		if left > right:
			# 작은 데이터와 피벗 데이터 교체
			array[right], array[pivot] = array[pivot], array[right]
		else:
			# 작은 데이터와 큰 데이터 교체
			array[right], array[left] = array[left], array[right]
	quick_sort(array, start, right - 1)
	quick_sort(array, left, end)

quick_sort(array, 0, len(array) - 1)
print(array)
