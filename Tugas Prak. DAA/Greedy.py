def find_shortest_route(graph, start):
  visited = []
  queue = [start]
  path = []
  while queue:
   node = queue.pop(0)
   if node not in visited:
    visited.append(node)
    path.append(node)
    neighbours = graph[node]
    queue += neighbours
    return path

graph = {
 'A': ['B', 'C', 'D'],
 'B': ['E'],
 'C': ['F', 'G'],
 'D': ['H'],
 'E': ['I'],
 'F': ['J', 'K'],
 'G': ['L'],
 'H': ['M'],
 'I': [],
 'J': [],
 'K': [],
 'L': [],
 'M': []
}
start = 'A'
shortest_route = find_shortest_route(graph, start)
print("Rute perjalanan terpendek:", shortest_route)