# 스택

import sys

input=sys.stdin.readline

n = int(input())

array = []
result = []
for _ in range(n):
	s = list(map(str, input().split()))
	if s[0] == "push":
		array.append(int(s[1]))
	elif s[0] == "top":
		result.append(array[len(array) - 1] if len(array) > 0 else -1)
	elif s[0] == "size":
		result.append(len(array))
	elif s[0] == "empty":
		result.append(0 if len(array) > 0 else 1)
	elif s[0] == "pop":
		result.append(array.pop() if len(array) > 0 else -1)

for r in result:
	print(r)
