# 개선된 다익스트라 알고리즘

## 시간복잡도 O(ElogV) (V:노드 개수, E:간선 개수)

## 힙 자료구조를 사용
## 우선순위 큐 : 우선순위가 가장 높은 데이터를 가장 먼저 삭제

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수
n, m = map(int, input().split())
# 시작 노드
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n + 1)]
# 최단 거리 리스트
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))

def dijkstra(start):

	q = []
	# 시작 노드로 가기 위한 최단 경로는 0으로 설정하며, 큐에 삽입
	heapq.heappush(q, (0, start))
	distance[start] = 0
	while q: # 큐가 비어 있지 않다면
		dist, now = heapq.heappop(q) # 힙에서 가장 최단 거리 꺼내기
		# 현재 노드가 이미 처리된 노드라면 무시
		if distance[now] < dist:
			continue
		# 현재 노드와 인접한 다른 노드들 확인
		for i in graph[now]:
			cost = dist + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
	if distance[i] == INF:
		print("INFINITY")
	else:
		print(distance[i])
