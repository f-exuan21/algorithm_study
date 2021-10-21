# 연구소

import copy
from itertools import combinations
from collections import deque

# 연구소 크기
n, m = map(int, input().split())
graph = []

for i in range(n):
	graph.append(list(map(int, input().split())))

# 빈 칸을 배열에 담기
empty = []
for i in range(n):
	for j in range(m):
		if graph[i][j] == 0:
			empty.append((i, j))

def check_virus(graph):

	# 바이러스 위치 담은 배열
	virus = []
	for i in range(len(graph)):
		for j in range(len(graph[0])):
			if graph[i][j] == 2:
				virus.append((i, j))
	# 상, 하, 좌, 우
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]
	# 바이러스로가 퍼진 후 맵 생성
	for v in virus:
		q = deque([(v[0], v[1])])
		while q:
			nowx, nowy = q.popleft()
			for i in range(4):
				lx = nowx + dx[i]
				ly = nowy + dy[i]
				if lx >= 0 and lx < n and ly >= 0 and ly < m and graph[lx][ly] == 0:
					graph[lx][ly] = 2
					q.append((lx, ly))

	# 빈 방 개수 체크
	cnt = 0
	for i in range(n):
		for j in range(m):
			if graph[i][j] == 0:
				cnt += 1
	return cnt


result = 0
# 빈 칸으로 벽 3개를 세울 수 있는 조합 만들기
for walls in list(combinations(empty, 3)):
	copy_graph = copy.deepcopy(graph)
	# 3개 벽 세우기
	for x, y in walls:
		copy_graph[x][y] = 1
	# 바이러스 퍼지고 난 후 남은 방 개수 출력
	result = max(result, check_virus(copy_graph))

print(result)
