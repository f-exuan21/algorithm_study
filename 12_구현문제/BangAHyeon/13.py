# 치킨 배달


from itertools import combinations

# 도시 크기, 폐업하지 않을 최대 치킨 집 개수
n, m = map(int, input().split())
# 지도 받기
array = []
for _ in range(n):
	array.append(list(map(int, input().split())))

# 치킨 집, 집 리스트 만들기
chicken = []
house = []
for i in range(n):
	for j in range(n):
		if array[i][j] == 2:
			chicken.append((i, j))
		elif array[i][j] == 1:
			house.append((i, j))

# 치킨 집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
	result = 0
	for hx, hy in house:
		tmp = int(1e9)
		for cx, cy in candidate:
			tmp = min(tmp, abs(hx - cx) + abs(hy - cy))
		result += tmp
	return result

result = int(1e9)
for candidate in candidates:
	result = min(result, get_sum(candidate))

print(result)
