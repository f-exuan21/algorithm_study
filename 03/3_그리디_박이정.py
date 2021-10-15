##거스름돈

# n = int(input("거스름돈 : "))
# count = 0
#
# coins = [500, 100, 50, 10]
#
# for coin in coins:
#     count += n // coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
#     n %= coin
#
#     print(coin, count)

#-----------------------------------------------------
#큰 수의 법칙
#배열의 크기 : N
#숫자가 더해지는 횟수 : M
#연속적인 인덱스 사용 횟수 : K

# #N, M, K를 공백으로 구분하여 입력받기
# n, m, k = map(int, input().split())
#
# #N개의 수를 공백으로 구분하여 입력받기
# data = list(map(int, input().split()))
#
# data.sort() #입력받은 수들 정렬하기
# first = data[n - 1]
# second = data[n - 2]
#
# result = 0
#
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1 # 더할 때마다 1씩 빼기
#     if m == 0: #m이 0이라면 반복문 탈출
#         break
#     result += second
#     m -= 1 #더할 때마다 1씩 빼기
#
# print(result)
#
# # 답안
# # N, M, K를 공백으로 구분하여 입력받기
# n, m, k = map(int, input().split())
# # N개의 수를 공백으로 구분하여 입력 받기
# data = list(map(int, input().split()))
#
# data.sort() # 입력받은 수 정렬
# first = data[n - 1]
# second = data[n - 2]
#
# count = int(m/ (k +1)) * k
# count += m % (k + 1)
#
# result = 0
# result += (count) * first
# result += (m-count) * second
#
# print(result)
#
#숫자카드게임

# py min() 함수를 이용하는 답안 예시
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0

#한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

# N, M을 공백으로 구분하여 입력 받기
n, m = map(int, input(),split())

result = 0
#한줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))

    min_value = 10001
    for a in data:
        min_value = min(min_value, a)

    result = max(result, min_value)

print(result)

#1이 될 때까지
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while  n>=k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

#마지막으로 남은 수에 대하여 1씩 빼기
while n> 1:
    n -= 1
    result += 1

print(result)

##py 답안 예시
# N, K 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

while True :
    target = (n // k) * k
    result += ( n - target)
    n = target

    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)



