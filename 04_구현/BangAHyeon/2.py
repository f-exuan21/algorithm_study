# 왕실의 나이트

moves = [(2, 1), (1, 2), (-1, -2), (-2, -1), (1, -2), (-1, 2), (2, -1), (-2, 1)]

now_location = input()
row = int(now_location[1])
col = int(ord(now_location[0])) - int(ord('a')) + 1

result = 0
for move in moves:
	tmp_row = row + move[0]
	tmp_col = col + move[1]
	if tmp_row < 1 or tmp_row > 8 or tmp_col < 1 or tmp_col > 8:
		continue
	result += 1

print(result)
