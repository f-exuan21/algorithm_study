# 금광

# 케이스 개수
t = int(input())

def search_graph(graph, n, m):
	for j in range(1, m):
		for i in range(n):
			if i == 0:
				graph[i][j] = graph[i][j] + max(graph[i][j-1], graph[i+1][j-1])
			elif i == n - 1:
				graph[i][j] = graph[i][j] + max(graph[i][j-1], graph[i-1][j-1])
			else:
				graph[i][j] = graph[i][j] + max(graph[i][j-1], graph[i+1][j-1], graph[i-1][j-1])
	result = int(-1e9)
	for i in range(n):
		result = max(result, graph[i][m-1])
	return result

for _ in range(t):
	n, m = map(int, input().split())
	nums = list(map(int, input().split()))
	graph = [[0] * m for _ in range(n)]
	idx = 0
	for i in range(n):
		for j in range(m):
			graph[i][j] = nums[idx]
			idx += 1
	result = search_graph(graph, n, m)
	print(result)
