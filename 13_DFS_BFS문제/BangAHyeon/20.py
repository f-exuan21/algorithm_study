# 감시 피하기

from itertools import combinations

# 복도 크기
n = int(input())

# 맵
graph = []
empty = []
teacher = []
for i in range(n):
	graph.append(list(map(str, input().split())))
	for j in range(n):
		if graph[i][j] == 'X':
			empty.append([i, j])
		elif graph[i][j] == 'T':
			teacher.append([i, j])

# 상, 하, 좌, 우
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
def find_student(graph, tx, ty, dx, dy):
	tmpx = tx + dx
	tmpy = ty + dy
	if tmpx >= 0 and tmpx < n and tmpy >= 0 and tmpy < n:
		if graph[tmpx][tmpy] == 'X':
			return find_student(graph, tmpx, tmpy, dx, dy)
		elif graph[tmpx][tmpy] == 'S':
			return False
	return True


comb = combinations(empty, 3)

flag = True
for obj in comb:
	flag = True
	for x, y in obj:
		graph[x][y] = 'O'

	for tx, ty in teacher:
		if find_student(graph, tx, ty, -1, 0) == False or find_student(graph, tx, ty, 1, 0) == False\
			or find_student(graph, tx, ty, 0, 1) == False or find_student(graph, tx, ty, 0, -1) == False:
			flag = False

	if flag == True:
		break

	for x, y in obj:
		graph[x][y] = 'X'

if flag:
	print("YES")
else:
	print("NO")
