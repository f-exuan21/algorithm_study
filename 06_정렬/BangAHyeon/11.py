# 성적이 낮은 순서로 학생 출력하기

num = int(input())

arr = []
for _ in range(num):
	input_data = input().split()
	arr.append((input_data[0], input_data[1]))

arr.sort(key=lambda x : x[1])

for val in arr:
	print(val[0], end=' ')
