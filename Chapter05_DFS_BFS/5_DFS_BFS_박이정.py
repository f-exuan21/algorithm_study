stack = []

#삽입(5)- 삽입(2) - 삽입(3) - 삽입(7)  - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) #최하단 원소부터 출력
print(stack[::-1]) #최상단 원소부터 출력

## 큐 예제
## 큐(Queue) 구현을 위해 deque 라이브러리 사용
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

def recursive_function():
    print('재귀 함수를 호출합니다')
    recursive_function()

recursive_function()

#재귀 함수 종료 조건
def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return

    print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다')
    recursive_function(i + 1)
    print(i, '번째 재귀 함수를 종료합니다')

recursive_function(1)

##2가지 방식으로 구현한 팩토리얼 예제

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print('반복적으로 구현 :', factorial_iterative(5))
print('반복적으로 구현 :', factorial_recursive(5))

##탐색 알고리즘 DFS/BFS
#인접 행렬 방식 예제

INF = 999999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

graph = [[] for _ in range(3)]

#노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

#노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0, 7))

#노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0, 5))

print(graph)

#DFS 메서드 정리
def dfs(graph, v, visited):
    visited[v] =  True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

dfs(graph, 1, visited)

## py BFS 예제
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)

#음료수 얼려 먹기
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x,  y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

return = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)

#미로탈출
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
       x, y = queue.popleft()
       for i in range(4):
           nx = x + dx[i]
           ny = y + dy[i]

           if nx < 0 or ny < 0 or nx >= n or ny >= m:
               continue
           if graph[nx][ny] == 0:
               continue
           if graph[nx][ny] == 1:
               graph[nx][ny] = graph[x][y] + 1
               queue.append((nx, ny))

    return graph[n - 1][m - 1]

print(bfs(0, 0))

