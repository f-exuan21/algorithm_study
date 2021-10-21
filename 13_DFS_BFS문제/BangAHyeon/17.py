# 경쟁적 전염

from collections import deque

# 시험관 크기, 바이러스 종류 수
n, k = map(int, input().split())

graph = []

# n * n 만큼 graph 입력받기
for _ in range(n):
	graph.append(list(map(int, input().split())))

# s 초 뒤에 (x,y)에 존재하는 바이러스
s, x, y = map(int, input().split())

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

data = []
# 바이러스를 data에 담기
for i in range(n):
	for j in range(n):
		if graph[i][j] != 0:
			data.append([graph[i][j], 0, (i, j)])
data.sort() # 바이러스 번호 순으로 정렬

q = deque(data)

while q:
	virusNum, time, v = q.popleft()
	if time == s:
		break
	vx = v[0]; vy = v[1]
	for i in range(4):
		tmpx = vx + dx[i]
		tmpy = vy + dy[i]
		if tmpx >= 0 and tmpx < n and tmpy >= 0 and tmpy < n and graph[tmpx][tmpy] == 0:
			graph[tmpx][tmpy] = virusNum
			q.append([virusNum, time + 1, (tmpx, tmpy)])

print(graph[x - 1][y - 1])
