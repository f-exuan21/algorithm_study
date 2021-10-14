# 숫자 카드 게임
n, m = map(int, input().split())

arr = []
for i in range(n):
	arr.append(min(list(input().split())))

print(max(arr))
