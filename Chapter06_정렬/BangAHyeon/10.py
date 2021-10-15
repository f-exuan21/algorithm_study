# 위에서 아래로

num = int(input())

arr = []
for _ in range(num):
	arr.append(int(input()))

arr.sort(reverse=True)
print(arr)
