# 자물쇠와 열쇠

def check(array, lock_len):
	# 자물쇠 가운데가 1로 맞춰졌는지 확인하기
	for i in range(lock_len, 2 * lock_len):
		for j in range(lock_len, 2 * lock_len):
			if array[i][j] != 1:
				return False
	return True

def rotate_key(key):
	key_len = len(key)
	rotated_key = [[0] * key_len for _ in range(key_len)]
	for i in range(key_len):
		for j in range(key_len):
			rotated_key[j][key_len - i - 1] = key[i][j]
	return rotated_key

def solution(key, lock):
	n = len(key)
	m = len(lock)
	length = 3 * m
	# 2차원 배열 만드는 법 기억하기
	array = [[0] * length for _ in range(length)]

	# 기존 자물쇠를 새로운 자물쇠에 넣기
	for i in range(m):
		for j in range(m):
			array[m + i][m + j] = lock[i][j]

	# 열쇠회전
	for _ in range(4): # 90도로 돌렸을 때 4가지 이므로
		key = rotate_key(key)

		# 커진 자물쇠에 열쇠 채우기
		for i in range(2 * m):
			for j in range(2 * m):
				for x in range(n):
					for y in range(n):
						array[i + x][j + y] += key[x][y]
				if check(array, m): # 자물쇠가 맞았을 경우 True 리턴
					return True
				# 자물쇠를 다 채워봤는데 맞지 않을 경우 자물쇠를 초기화 해준다.
				for x in range(n):
					for y in range(n):
						array[i + x][j + y] -= key[x][y]

	return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
