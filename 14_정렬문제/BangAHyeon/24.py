# 안테나

# 중앙값들이 최소거리를 갖는다

n = int(input())

house = list(map(int, input().split()))
house.sort()

length = len(house)
center = int(length / 2) - 1 if length % 2 == 0 else int(length / 2)

print(house[center])
