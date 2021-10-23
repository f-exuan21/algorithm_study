# 공유기 설치

# 집의 개수, 공유기 개수
n, c = list(map(int, input().split()))

array = []
for _ in range(n):
	array.append(int(input()))
array.sort()

start = array[1] - array[0] # 집 사이 거리가 가장 짧은 것
end = array[-1] - array[0] # 집 사이 거리가 가장 먼 것
result = 0

while start <= end:
	mid = (start + end) // 2
	value = array[0]
	count = 1
	for i in range(1, n): # 앞에서 부터 차근차근 설치
		if array[i] >= value + mid:
			value = array[i]
			count += 1
	if count >= c: # c개 이상 공유기를 설치할 수 있는 경우 거리 증가
		start = mid + 1
		result = mid # 최적의 결과를 저장
	else:
		end = mid - 1

print(result)
