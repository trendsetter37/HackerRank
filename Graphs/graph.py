'''
    A -> B
    A -> C
    B -> C
    B -> D
    C -> D
    D -> C
    E -> F
    F -> C
'''

graph = {
    # Connected by a direct arc
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C']
}

def find_path(graph, start, end, path=[]):
    # Works so far
    path += start
    keys = graph.keys()
    if start == end:
        return path
    if start not in keys:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None
