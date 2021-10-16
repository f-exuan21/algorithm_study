# 게임 개발

n, m = map(int, input().split())

# 컴프리헨션 문법을 사용해 2차원 리스트 초기화
maps = [[0] * m for _ in range(n)]

x, y, d = map(int, input().split())
maps[x][y] = 1 # 현재 좌표 방문 처리

array = []
for i in range(n):
	array.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
	global d
	d -= 1
	if d == -1:
		d = 3

count = 1 # 밟은 땅 카운트
turn_time = 0

while True:
	turn_left()
	tmp_x = x + dx[d]
	tmp_y = y + dy[d]
	if maps[tmp_x][tmp_y] == 0 and array[tmp_x][tmp_y] == 0:
		x = tmp_x
		y = tmp_y
		count += 1
		maps[x][y] = 1
		turn_time = 0
		continue
	else:
		turn_time += 1

	if turn_time == 4:
		tmp_x = x - dx[d]
		tmp_y = y - dy[d]
		turn_time = 0
		if array[tmp_x][tmp_y] == 0:
			x = tmp_x
			y = tmp_y
		else:
			break

print(count)
