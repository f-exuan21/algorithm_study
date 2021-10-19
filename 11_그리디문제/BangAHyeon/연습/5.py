# 볼링공 고르기

# 볼링공 개수, 볼링공 최대 무개
n, m = map(int, input().split())

weight = list(map(int, input().split()))

# 두 사람은 서로 무게가 다른 볼링공을 고르려함.

# 볼링공 무게마다 볼링공 개수 저장
ball = [0] * (m + 1)
for w in weight:
	ball[w] += 1

result = 0
for b in ball:
	result += b * (n - b)
	n = n - b

print(result)
