# 정렬된 배열에서 특정 수의 개수 구하기

def count_by_value(array, x):
    n = len(array)

    a = first(array, x, 0, n - 1)

    if a == None:
        return 0

    b = last(array, x, 0, n - 1)

    return b - a + 1

def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return first(array, target, start, mid - 1)
    else:
        return first(array, target, mid + 1, end)

def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif array[mid]> target:
        return last(array, target, mid + 1, end)

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x)

if count ==  0:
    print(-1)

else:
    print(count)

#2

from bisect import bisect_lift, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)

#고정점 찾기
def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    else:
        return binary_search(array, mid + 1, end)

n = int(input())
array = list(map(int, input.split()))

index = binary_search(array, 0, n - 1)

if index ==  None:
    print(-1)
else:
    print(index)

#공유기 설치
n, c = list(map(int, input().split(' ')))

array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

start = 1 ################
end = array[-1] - array[0]
result = 0

while(start <= end):
    mid = (start + end) // 2
    value = array[0]
    count = 1
    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid -1

print(result)

#가사 검색
#프로그래머스

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:
        if q[0] != '?':
            res = count_by_range(array[len(q)], q.replace('?','a'), q.replace('?','z'))
        else:
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?','z'))
        answer.append(res)
    return answer

