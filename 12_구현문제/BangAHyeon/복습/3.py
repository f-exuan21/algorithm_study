# 문자열 뒤집기

n = list(map(int, input()))

now = n[0]
count0 = 0
count1 = 0
if now == 1:
	count1 += 1
else:
	count0 += 1
for i in n:
	if now != i:
		if i == 1:
			count1 += 1
		else:
			count0 += 1
		now = i
print(min(count0, count1))
