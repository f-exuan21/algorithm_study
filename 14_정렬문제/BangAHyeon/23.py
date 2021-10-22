# 국영수

# 학생 수
n = int(input())

score = []
for _ in range(n):
	name, kor, eng, math = input().split()
	score.append([name, int(kor), int(eng), int(math)])


score = sorted(score, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for x in score:
	print(x[0])
