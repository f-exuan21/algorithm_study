# 떡볶이 떡 만들기
# 절단기의 높이는 1부터 10억까지의 정수 중 하나이다.
# 이처럼 큰 수를 보면 당연하다는 듯이 가장 먼저 이진탐색을 떠올리자.

n, m = list(map(int, input().split())) #떡의 개수, 떡의 길이

# 각 떡의 길이
array = list(map(int, input().split()))

start = 0
end = max(array)
result = 0

def binary_search(array, target, start, end):
	global result
	if start > end:
		return
	mid = (start + end) // 2
	# 잘랐을 때 떡의 양 계산
	total = 0
	for n in array:
		if n > mid:
			total += (n - mid)
	if total == target: # 목표한 길이와 자른 길이가 같은 경우 result 기록
		result = mid
		return
	elif total < target:
		binary_search(array, target, start, mid - 1)
	else: # 최대한 덜 잘랐을 떄가 정답이므로, 여기서 result 한 번 기록
		result = mid
		binary_search(array, target, mid + 1, end)

binary_search(array, m, start, end)
print(result)
