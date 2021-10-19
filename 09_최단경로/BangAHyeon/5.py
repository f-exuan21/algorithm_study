# 전보 (p.262)

import heapq
import sys

input = sys.stdin.readline
INF = int(1e6)

# 노드 개수, 간선 개수, 시작 노드
n, m, start = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
# [
# 	[],
# 	[],
# 	[]
# ]
graph = [[] for i in range(n + 1)]

# 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
	a, b, c = map(int, input().split()) # a->b 비용 c
	graph[a].append((b, c))

def dijkstra(start):
	q = []
	# 시작노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
	heapq.heappush(q, (0, start))
	distance[start] = 0
	while q: # 큐가 비어있지 않다면
		dist, now = heapq.heappop(q)
		if distance[now] < dist:
			continue
		# 현재 노드와 연결된 다른 인접한 노드들을 확인
		for i in graph[now]:
			cost = dist + i[1] # 현재 노드를 거쳐서 가는 거리
			if cost < distance[i[0]]: # 현재 노드를 거쳐서 가는 거리가 더 짧은 경우
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 도달할 수 있는 노드의 개수
count = 0
max_distance = 0
for i in distance:
	if i != INF:
		count += 1
		max_distance = max(max_distance, i)

# 시작 노드는 제외해야 하므로 제거
print(count - 1, max_distance)
