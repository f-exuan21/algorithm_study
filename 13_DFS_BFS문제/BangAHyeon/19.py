from itertools import permutations

# 숫자 개수
n = int(input())
numbers = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

signs = ['+'] * plus + ['-'] * minus + ['*'] * mul + ['/'] * div
comb = list(set(permutations(signs, n - 1)))

maxRst = int(-1e9)
minRst = int(1e9)
for sign in comb:
	rst = numbers[0]
	idx = 1
	for s in sign:
		if s == '+':
			rst += numbers[idx]
		elif s == '-':
			rst -= numbers[idx]
		elif s == '*':
			rst *= numbers[idx]
		else:
			rst = int(rst / numbers[idx])
		idx += 1
	maxRst = max(maxRst, rst)
	minRst = min(minRst, rst)

print(maxRst)
print(minRst)
