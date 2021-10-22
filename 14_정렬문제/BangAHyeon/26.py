# 카드 정렬하기

# 더할 때마다 생긴 숫자는 그 다음 숫자보다 클 수 있기 때문에
# 우선순위 큐를 이용하여 항상 배열이 숫자 크기 순으로 보장되도록 한다.

import heapq

n = int(input())

heap = []
for i in range(n):
	data = int(input())
	heapq.heappush(heap, data)

sum_value = 0
while len(heap) != 1:
	first = heapq.heappop(heap)
	second = heapq.heappop(heap)
	result = first + second
	sum_value += result
	heapq.heappush(heap, result)

print(sum_value)
