# readline()

import sys
input_data = sys.stdin.readline().rstrip()
# readline()으로 입력하면 입력 후 엔터(\n)가 입력되는데,
# 이 공백 문자를 제거하기 위해 rstrip()을 꼭 사용하자.
print(input_data)
