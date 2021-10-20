# 만들 수 없는 금액

n = int(input())
money = list(map(int, input().split()))
money.sort()

target = 1
for x in money:
	if x <= target:
		target += x
	else:
		break

print(target)
