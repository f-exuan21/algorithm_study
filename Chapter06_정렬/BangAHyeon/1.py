# 선택 정렬

array = [7, 5, 9, 0, 3, 1, 6, 4, 2]

for i in range(len(array)):
	min_index = i
	for j in range(i, len(array)):
		if array[j] < array[min_index]:
			min_index = j
	array[i], array[min_index] = array[min_index], array[i]

print(array)

# 선택 정렬의 시간복잡도 : O(N^2)
