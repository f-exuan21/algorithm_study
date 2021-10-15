# 큐


# 큐(Queue) 구현을 위해 deque 라이브러리 사용
from collections import deque

# deque는 스택과 큐의 장점을 모두 채택한 것
# 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이다.
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse()
print(queue) # 나중에 들어온 순서대로 출력

# deque 자료형을 list 자료형으로 반환할 수 있다.
print(list(queue))
