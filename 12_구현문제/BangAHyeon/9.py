def solution(s):
	answer = len(s)
	for step in range(1, len(s) // 2 + 1):
		compressed = ""
		prev = s[:step]
		count = 1
		# step만큼 증가시키며 이전 문자열과 비교
		for j in range(step, len(s), step):
			if prev == s[j:j + step]: # 이전 글자와 현재 글자가 같다면
				count += 1
			else:
				compressed += str(count) + prev if count >= 2 else prev
				prev = s[j:j + step]
				count = 1
		# 남아있는 문자열에 대해 처리
		compressed +=  str(count) + prev if count >= 2 else prev
		answer = min(answer, len(compressed))
	return answer

print(solution("ababcdcdababcdcd"))
