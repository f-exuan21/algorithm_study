# 네트워크

def solution(n, computers):
	answer = 0
	visited = [False] * n

	for com in range(n):
		if visited[com] == False:
			bfs(n, computers, com, visited)
			answer += 1
	return answer

def bfs(n, computers, com, visited):
	visited[com] = True
	queue = []
	queue.append(com)
	while queue:
		com = queue.pop(0)
		visited[com] = True
		for connect in range(n):
			if connect != com and computers[com][connect] == 1 and visited[connect] == False:
				queue.append(connect)

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 0, 1]]))
