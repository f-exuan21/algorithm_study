# 계수 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in array:
	count[i] += 1

for i in range(len(count)):
	for j in range(count[i]):
		print(i, end=' ')

# 계수 정렬의 시간 복잡도 : O(N+K)
# 계수 정렬의 공간 복잡도 : O(N+K)
# 데이터가 0과 999999 단 2개만 존재해도 리스트 크기가 100만 개가 되도록 선언해야 한다.
# 따라서 계수 정렬은 항상 사용할 수 있는 정렬 알고리즘이 아니다.
# 동일한 값을 가지는 데이터가 여러 개 등잘할 때 적합하다.
