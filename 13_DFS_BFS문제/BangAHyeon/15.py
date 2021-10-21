# 특정 거리의 도시 찾기

from collections import deque

# 도시개수, 도로개수, 거리정보, 출발 도시 번호
n, m, k, x = map(int, input().split())

cities = [0] * n

graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력받기
for _ in range(m):
	i, j = map(int, input().split())
	graph[i].append(j)

distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시

q = deque([x])
while q:
	now = q.popleft()
	# 현재 도시에서 이동할 수 있는 모든 도시를 확인
	for next_node in graph[now]:
		# 아직 방문하지 않은 도시라면
		if distance[next_node] == -1:
			# 최단 거리 갱신
			distance[next_node] = distance[now] + 1
			q.append(next_node)

# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
	if distance[i] == k:
		print(i)
		check = True
if check == False:
	print(-1)
