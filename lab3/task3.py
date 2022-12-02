from task1 import *
visited=[]
def dfs_visit(graph,node):
    for m in graph[node]:
        if m not in visited:
            visited.append(m)
            dfs_visit(graph,m)
def dfs(graph,endpoint):
    for m in [*graph]:
        if m not in visited:
            visited.append(m)
            dfs_visit(graph,m)
a='12'
dfs(graph,a)
output = ""
for i in visited:
    output += i + ' '
    if i ==a:
        break
file = open("output3.txt",'w')
file.write(output)
file.close()
