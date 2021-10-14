# 큰 수의 법칙

# n : 배열의크기
# m : 숫자가 더해지는 횟수
# k : 최대 더할 수 있는 횟수
n, m, k = map(int, input().split())
arr = list(input().split())

arr.sort(reverse=True)
rst = m // k * k * int(arr[0])
rst += m % k * int(arr[1])
print(rst)
