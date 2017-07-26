graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs(graph, start):
    visited, stack=set(), [start]
    while stack:
        vertex=stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)
    return visited



def dfs2(graph,start,visited=None):
    if visited is None:
        visited=set()
    visited.add(start)
    for nxt in graph[start]-visited:
        dfs2(graph,nxt,visited)
    return visited


def dfs_paths(graph,start ,goal):
    stack=[(start,[start])]
    while stack:
        (vertex,path)=stack.pop()
        for nxt in graph[vertex]-set(path):
            if nxt==goal:
                yield path+[nxt]
            else:
                stack.append((nxt,path+[nxt]))

# print(dfs2(graph,"A"))
# print(dfs2(graph,"B"))
# print(dfs2(graph,"C"))

print(list(dfs_paths(graph,"A","C")))
print(list(dfs_paths(graph,"A","D")))
