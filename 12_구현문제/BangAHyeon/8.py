# 문자열 재정렬

s = list(input())
tmp_str = []
tmp_num = 0

for x in s:
	if x.isalpha():
		tmp_str.append(x)
	else:
		tmp_num += int(x)
tmp_str.sort()
print(''.join(tmp_str) + str(tmp_num))
