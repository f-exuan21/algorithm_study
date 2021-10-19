# 만들 수 없는 금액

n = int(input())
money = list(map(int, input().split()))
money.sort()

result = 1

for m in money:
	if m <= result:
		result += m
	else:
		break

print(result)
