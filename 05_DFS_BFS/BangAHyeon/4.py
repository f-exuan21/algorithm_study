# 재귀함수가 100번 호출되었을 때 종료

def recursive_function(i):
	print(f'{i}번째 재귀함수')
	if i == 100:
		return
	recursive_function(i + 1)
recursive_function(1)
