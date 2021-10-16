# sort(), sorted()를 사용할 때에는 매개변수로 key 를 받을 수 있다.
# key 값으로는 하나의 함수가 들어가야 하며 이는 "정렬 기준"이 된다.

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
	return data[1]

result = sorted(array, key=setting)
print(result)
