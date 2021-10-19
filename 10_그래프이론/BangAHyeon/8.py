# 도시 분할 계획 (p.300)

def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
	parent[i] = i

edges = []
result = 0

# 모든 간선에 대한 정보 받기
for i in range(e):
	a, b, cost = map(int, input().split())
	# cost 순서로 sort하기 위해 맨 앞에 cost 위치
	edges.append((cost, a, b))

edges.sort()
last = 0 # 제일 큰 cost = 가장 마지막 cost
for edge in edges:
	cost, a, b = edge
	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent, a, b)
		result += cost
		last = cost

print(result - last)
