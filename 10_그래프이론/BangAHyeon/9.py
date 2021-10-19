# 커리큘럼 (p.303)

from collections import deque
import copy

# 노드 개수
v = int(input())
# 진입차수
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보
graph = [[] for _ in range(v + 1)]
# 시간
time = [0] * (v + 1)

# 간선 정보 입력 받기
for i in range(1, v + 1):
	data = list(map(int, input().split()))
	time[i] = data[0]
	for x in data[1:-1]:
		indegree[i] += 1
		graph[x].append(i)

# 위상 정렬 함수
def topology_sort():
	result = copy.deepcopy(time)
	q = deque()

	# 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
	for i in range(1, v + 1):
		if indegree[i] == 0:
			q.append(i)

	# 큐가 빌 때까지 반복
	while q:
		now = q.popleft()
		for i in graph[now]:
			result[i] = max(result[i], result[now] + time[i])
			indegree[i] -= 1
			if indegree[i] == 0:
				q.append(i)

	# 위상정렬을 수행한 결과 출력
	for i in range(1, v + 1):
		print(result[i], end=' ')

topology_sort()
