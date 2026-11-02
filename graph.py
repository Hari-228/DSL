# Graph Representation & Traversal (BFS using List, DFS using Matrix)


def bfs_list(graph, start):
  visited = set()
  queue = [start]
  visited.add(start)
  print("BFS Traversal:", end=" ")
  while queue:
    node = queue.pop(0)
    print(node, end=" ")
    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)
  print()


# Driver Code for Graph
graph_list = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": [], "F": []}
bfs_list(graph_list, "A")