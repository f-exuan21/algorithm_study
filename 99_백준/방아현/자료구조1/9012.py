# 괄호

import sys
input = sys.stdin.readline

n = int(input())
result = []
for _ in range(n):
	text = input()
	count = 0
	for t in text:
		if t == '(':
			count += 1
		elif t == ')':
			count -= 1
		if count < 0:
			break
	if count == 0:
		result.append('YES')
	else:
		result.append('NO')

for r in result:
	print(r)
