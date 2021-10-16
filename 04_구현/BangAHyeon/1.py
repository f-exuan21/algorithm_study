# 상하좌우

n = int(input())
arr = list(input().split())
x, y = 1, 1

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
types = ['L', 'R', 'U', 'D']

for s in arr:
	for i in range(len(types)):
		if s == types[i]:
			tmp_x = x + dx[i]
			tmp_y = y + dy[i]
	if tmp_x < 1 or tmp_y < 1 or tmp_x > n or tmp_y > n:
		continue
	x, y = tmp_x, tmp_y

print(x, y)
