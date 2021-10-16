# 음료수 얼려 먹기

n, m = map(int, input().split())

# 맵 만들기
graph = []
for i in range(n):
	graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들 방문
def dfs(x, y):
	if x < 0 or x >= n or y < 0 or y >= m:
		return False
	if graph[x][y] == 0:
		# 해당 노드 방문 처리
		graph[x][y] = 1
		# 해당 노드의 상, 하, 좌, 우 모두 방문
		dfs(x - 1, y)
		dfs(x, y - 1)
		dfs(x + 1, y)
		dfs(x, y + 1)
		return True
	return False

# 모든 위치에 대하여 음료수 채우기
result = 0
for i in range(n):
	for j in range(m):
		if dfs(i, j):
			result += 1

print(result)
