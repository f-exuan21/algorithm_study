# 국영수
n = int(input())
students = []

for _ in range(n):
    students.append(input().split())

students.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])

# 안테나
n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n - 1) // 2])

# 실패율
def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N + 1):
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count/length

        answer.append((i, fail))
        length -= count
    answer = sorted(answer, key=lambda t: t[1], reverse=True)

    answer = [i[0] for i in answer]
    return answer

# 카드 정렬하기
import heapq

n = int(input())

heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)