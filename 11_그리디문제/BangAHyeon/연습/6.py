# 무지의 먹방 라이브

import heapq

def solution(food_times, k):

	if sum(food_times) <= k:
		return -1

	q = []
	for i in range(len(food_times)):
		heapq.heappush(q, (food_times[i], i + 1))

	sum_time = 0 # 음식 먹은 총 시간
	length = len(food_times)
	previous = 0 # 이전 음식 먹은 시간

	while sum_time + (q[0][0] - previous) * length <= k:
		now_time = heapq.heappop(q)[0]
		sum_time += (now_time - previous) * length
		previous = now_time
		length -= 1

	# 현재 남은 음식들 정렬
	result = sorted(q, key=lambda x:x[1])
	return result[(k - sum_time) % length][1]

food_times = [3, 1, 2]
k = 4
print(solution(food_times, k))

