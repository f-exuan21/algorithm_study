# 파이썬의 장점을 살린 퀵 정렬

array = [7, 5, 9, 0, 3, 1, 6, 4, 2, 8]

def quick_sort(array):
	# 리스트가 하나 이하의 원소만을 담고 있다면 종료
	if len(array) <= 1:
		return array

	pivot = array[0] # 피벗을 첫 번째 원소로 등록
	tail = array[1:] # 피벗을 제외한 리스트

	left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
	right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

	return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

# 파이썬의 장점을 살려 짧게 작성할 수 있다.
# 피벗과 데이터를 비교하는 연산 횟수가 증가하므로, 시간 면에서는 조금 비효율적이다.

# 퀵 정렬의 시간 복잡도 : O(NlogN)
