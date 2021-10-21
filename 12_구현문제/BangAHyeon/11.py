# 뱀

def solution():
	# 배열의 크기
	n = int(input())
	array = [[0] * n for _ in range(n)]

	# 사과 개수
	k = int(input())
	# 사과 위치 받기
	for _ in range(k):
		x, y = map(int, input().split())
		array[x - 1][y - 1] = 1

	# 방향 변환 횟수
	l = int(input())
	directionList = []
	# 방향 받기
	for _ in range(l):
		time, direction = input().split()
		directionList.append([int(time), direction])
	now_x = 0
	now_y = 0
	# 상, 우, 하, 좌
	lx = [-1, 0, 1, 0]
	ly = [0, 1, 0, -1]
	now_d = 1 # 오른쪽
	next = directionList.pop(0) # 방향을 바꿔야할 다음 시간과 방향을 배열로 갖고 있음
	bodyList = [[0, 0]] # 뱀의 몸이 있는 곳의 좌표
	array[0][0] = 2
	result = 0
	while True:

		now_x += lx[now_d]
		now_y += ly[now_d]

		if now_x < 0 or now_y < 0 or now_x >= n or now_y >= n or array[now_x][now_y] == 2:
			result += 1
			break

		# 사과가 없으면 꼬리를 줄인다.
		if array[now_x][now_y] == 0:
			tail = bodyList.pop(0)
			array[tail[0]][tail[1]] = 0

		bodyList.append([now_x, now_y])
		array[now_x][now_y] = 2

		result += 1

		# 방향을 바꿀 시간이 되었으면 방향을 바꾼다.
		if result == next[0]:
			if next[1] == 'D': #오른쪽
				now_d = (now_d + 1) % 4
			else: #왼쪽
				now_d = (now_d - 1) % 4
			if len(directionList) > 0:
				next = directionList.pop(0)

	return result

print(solution())
