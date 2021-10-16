# BFS (너비우선탐색)

from collections import deque

def bfs(graph, start, visited):
	quque = deque([start])
	visited[start] = True
	# 큐가 빌 때까지 반복
	while quque:
		v = quque.popleft()
		print(v, end=' ')
		for i in graph[v]:
			if not visited[i]:
				quque.append(i)
				visited[i] = True


graph = [
	[],
	[2, 3, 8],
	[1, 7],
	[1, 4, 5],
	[3, 5],
	[3, 4],
	[7],
	[2, 6, 8],
	[1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
