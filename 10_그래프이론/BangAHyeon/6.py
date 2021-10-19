# 위상 정렬 (p.296)
# O(V + E)

from collections import deque

# 노드 개수, 간선 개수
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결리스트 (그래프) 초기화
graph = [[] for _ in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
	a, b = map(int, input().split())
	graph[a].append(b)
	# 진입차수를 1 증가
	indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
	result = []
	q = deque()

	# 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
	for i in range(1, v + 1):
		if indegree[i] == 0:
			q.append(i)

	# 큐가 빌 때까지 반복
	while q:
		now = q.popleft()
		result.append(now)
		for i in graph[now]:
			indegree[i] -= 1
			# 새롭게 진입차수가 0 이 되는 노드를 삽입
			if indegree[i] == 0:
				q.append(i)

	# 위상 정렬 결과를 출력
	for i in result:
		print(i, end=' ')

topology_sort()
