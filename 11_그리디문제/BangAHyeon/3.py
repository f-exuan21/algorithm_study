# 문자열 뒤집기

number = input()
list_1 = number.split('0')
list_0 = number.split('1')

while '' in list_0:
	list_0.remove('')

while '' in list_1:
	list_1.remove('')

if len(list_0) < len(list_1):
	print(len(list_0))
else:
	print(len(list_1))
