from task1 import * #importing graph from task1 
visited = []
queue = []
def bfs(visited, graph, node, endPoint):
    path=''
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        path += m + " "
        if m == endPoint:
            return path 
        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)   
output = bfs(visited, graph, '1', '12')
file = open("output2.txt",'w')
file.write(output)
file.close()