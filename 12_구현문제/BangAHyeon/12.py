# 기둥과 보 설치

# 현재 구조물이 가능한 구조물인지 확인하는 함수
def possible(answer):
	# 0 : 기둥, 1 : 보
	for x, y, stuff in answer:
		if stuff == 0:
			if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
				continue
			return False
		elif stuff == 1:
			if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
				continue
			return False
	return True

def solution(n, build_frame):
	answer = []

	for frame in build_frame:
		x, y, stuff, operate = frame
		if operate == 0: # 삭제
			answer.remove([x, y, stuff])
			if not possible(answer):
				answer.append([x, y, stuff])
		elif operate == 1: # 추가
			answer.append([x, y, stuff])
			if not possible(answer):
				answer.remove([x, y, stuff])
	return sorted(answer)
