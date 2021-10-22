# 실패율

def solution(n, stages):
	failure = []
	length = len(stages)
	for i in range(1, n + 1):
		cnt = stages.count(i)
		if length == 0:
			fail = 0
		else:
			fail = cnt / length
		failure.append([i, fail])
		length -= cnt
	failure.sort(key=lambda x: (-x[1], x[0]))
	result = [i[0] for i in failure]
	return result


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4 ,4 ,4]))
