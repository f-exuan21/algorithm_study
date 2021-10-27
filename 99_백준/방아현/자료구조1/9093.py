# 단어 뒤집기
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
	texts = list(map(str, input().split()))
	for text in texts:
		print(text[::-1], end=' ')
	print()
