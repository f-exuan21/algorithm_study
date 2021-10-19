# 미래 도시 (p.259)

INF = int(1e9)

# 노드 개수, 간선 개수
n, m = map(int, input().split())

# 2차원 리스트 생성 + 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신 -> 자기 자신 비용 0
for i in range(1, n + 1):
	graph[i][i] = 0

# 각 가선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
	a, b = map(int, input().split()) # a->b 비용 1
	graph[a][b] = 1
	graph[b][a] = 1 # 양방향이므로 둘 다 설정

# 최종 목적지 노드 X와 거쳐갈 노드 K를 입력받기
x, k = map(int, input().split())

for c in range(1, n + 1):
	for a in range(1, n + 1):
		for b in range(1, n + 1):
			graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
	print("-1")
else:
	print(distance)
