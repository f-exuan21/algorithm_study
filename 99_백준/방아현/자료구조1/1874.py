# 스택 수열

import sys

input=sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
	numbers.append(int(input()))


result = []
left = []
right = []
now = 0
for number in numbers:
	for _ in range(now, number):
		result.append('+')
		now += 1
		left.append(now)
	result.append('-')
	right.append(left.pop())

if numbers == right:
	for r in result:
		print(r)
else:
	print('NO')
