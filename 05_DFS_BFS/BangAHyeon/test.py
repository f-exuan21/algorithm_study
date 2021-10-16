# 여행경로

import collections

answer = []
graph = {}


def dfs(s):
	while graph[s]:
		if graph[s][-1] in graph and len(graph[graph[s][-1]]) > 0:
			dfs(graph[s].pop())
		else:
			answer.append(graph[s].pop())
	answer.append(s)

def solution(tickets):

	for a, b in tickets:
		if a in graph:
			graph[a].append(b)
		else:
			graph[a] = [b]
	for a, b in graph.items():
		graph[a].sort(reverse=True)
	print(graph)
	dfs("ICN")
	return answer[::-1]


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# print(solution([["ICN", "AAA"], ["ICN", "BBB"], ["BBB", "ICN"]]))
