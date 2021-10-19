# 볼링공 고르기

# 공 개수, # 공의 최대 무게
n, m = map(int, input().split())
# 공의 무게 리스트
data = list(map(int, input().split()))

# 공의 무게 만큼 리스트 생성
array = [0] * (m + 1)
# 공 무게 당 개수
for i in data:
	array[i] += 1

result = 0

for i in range(1, m + 1):
	n -= array[i]
	result += (array[i] * n)

print(result)
