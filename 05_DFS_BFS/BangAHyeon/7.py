# 인접리스트

# 행이 3개인 2차원 리스트
graph = [[] for _ in range(3)]

# 노드 0 에 연결된 정보 저장
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1 에 연결된 정보 저장
graph[1].append((0, 7))

# 노드 2 에 연결된 정보 저장
graph[2].append((0, 5))

print(graph)
