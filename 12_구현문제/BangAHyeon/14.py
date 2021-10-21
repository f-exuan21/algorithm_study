# 외벽 점검

from itertools import permutations

def solution(n, weak, dist):
	# weak 길이를 2배로 늘려서 원형을 일자형태로 변경
	length = len(weak)
	for i in range(length):
		weak.append(weak[i] + n)
	# 투입할 친구의 최솟값을 구해야 하므로 len(dist) + 1 로 초기화
	answer = len(dist) + 1

	# 0 부터 length - 1 까지 시작점으로 지정
	for start in range(length):
		# 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
		for friends in list(permutations(dist, len(dist))):
			count = 1 # 투입할 친구 수
			# 해당 친구가 점검 할 수 있는 마지막 위치
			position = weak[start] + friends[count - 1]
			# 시작점부터 모든 취약 지점을 확인
			for index in range(start, start + length):
				# 점검할 수 있는 위치를 벗어나면
				if position < weak[index]:
					# 새로운 친구 투입
					count += 1
					# 친구가 다 할당되면
					if count > len(dist):
						break
					# 해당 친구가 점검 할 수 있는 마지막 위치
					position = weak[index] + friends[count - 1]
			answer = min(answer, count)

	if answer <= len(dist):
		return answer
	else:
		return -1
