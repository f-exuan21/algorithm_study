# 인구 이동

from collections import deque

n, l, r = map(int, input().split())
graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, idx):
	# (x, y)의 위치와 연결된 나라 정보를 담는 리스트 (연합)
	united = []
	united.append((x, y))
	# 큐 라이브러리 활용
	q = deque()
	q.append((x, y))
	union[x][y] = idx
	summary = graph[x][y] # 연합 전체 인구수
	count = 1 # 현재 연합 국가의 수
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
				# 주변 국가와 인구 차이가 l 이상 r 이하라면
				if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
					q.append((nx, ny))
					summary += graph[nx][ny]
					count += 1
					united.append((nx, ny))
					union[nx][ny] = idx
	# 연합 국가끼리 인구 분배
	for i, j in united:
		graph[i][j] = summary // count

total_count = 0
while True:
	idx = 0
	union = [[-1] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			if union[i][j] == -1:
				dfs(i, j, idx)
				idx += 1
	if idx == n * n: # 인구 이동할 마을이 없으면 if union[i][j] == -1을 계속 타서 idx가 n * n 이랑 같아진다.
		break
	total_count += 1

print(total_count)
