# 플로이드 워셜 알고리즘

INF = int(1e9)

n = int(input()) # 노드 개수
m = int(input()) # 간선 개수

# 2차원리스트를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신 -> 자기 자신 = 0
for a in range(1, n + 1):
	graph[a][a] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
	a, b, c = map(int, input().split()) # a->b 비용 c
	graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
	for a in range(1, n + 1):
		for b in range(1, n + 1):
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
	for b in range(1, n + 1):
		if graph[a][b] == INF:
			print("INFINITY", end=' ')
		else:
			print(graph[a][b], end=' ')
	print()
