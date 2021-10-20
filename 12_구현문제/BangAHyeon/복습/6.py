# 무지의 먹방 라이브
import heapq

def solution(food_times, k):
	if sum(food_times) <= k:
		return -1
	q = [] # 우선순위 큐
	for i in range(len(food_times)):
		heapq.heappush(q, (food_times[i], i + 1))

	sum_time = 0 # 지금까지 먹은 시간
	previous = 0 # 이전 시간
	length = len(food_times)
	while sum_time + (q[0][0] - previous) * length <= k:
		now = heapq.heappop(q)[0]
		sum_time += (now - previous) * length
		length -= 1
		previous = now

	result = sorted(q, key=lambda x: x[1])
	x = (k - sum_time) % length # 남은시간 % 남은음식
	return result[x][1]

print(solution([3, 1, 5], 5))
