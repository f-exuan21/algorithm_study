# 정수 삼각형

n = int(input())
graph = []
for i in range(n):
	graph.append(list(map(int, input().split())))

result = int(-1e9)
for i in range(1, n):
	for j in range(len(graph[i])):
		print(i,j)
		if j == 0:
			graph[i][j] = graph[i][j] + graph[i-1][j]
		elif j == len(graph[i])-1:
			graph[i][j] = graph[i][j] + graph[i-1][j-1]
		else:
			graph[i][j] = graph[i][j] + max(graph[i-1][j], graph[i-1][j-1])
		result = max(result, graph[i][j])

print(result)

