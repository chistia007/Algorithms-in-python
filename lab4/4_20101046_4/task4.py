import heapq
def graph_creation(V,E): # V for vertex and E for edges
    graph={}
    for i in range(1,int(V)+1):
        graph[i]={}
    for i in range(1,int(E)+1):
        line=f.readline().split(' ')
        graph[int(line[0])] [int(line[1])]= int(line[2])
    #print(graph)
    return graph

def Network(graph,source):
    dist = [float('-inf')]*(len(graph)+1)
    dist[source] = float('inf')
    visited = [False]*(len(graph)+1)
    priorityQueue = []
    for v in graph:
        heapq.heappush(priorityQueue,[dist[v]*-1,v])
    while (priorityQueue):
        u = heapq.heappop(priorityQueue)[1]
        if visited[u]:
            continue
        else:
            visited[u]=True
        for v in graph[u]:
            alt = min(dist[u],graph[u][v])
            if alt > dist[v]:
                dist[v] = alt
                heapq.heappush(priorityQueue,[dist[v]*-1,v])
    dist[source] = 0
    return dist

result=''
f=open('input4.txt','r')
T=f.readline()
for i in range(int(T)):
    x=f.readline().split()
    N=x[0]  #vertex/places
    M=x[1]  #edges
    graph=graph_creation(N,M)
    source=int(f.readline())
    output=Network(graph,source)
    for i in range(1,len(output)):
        if output[i] == float('-inf'):
                result += "-1 "
        else:
                result += str(output[i]) + " "
    if i!=int(T):
        result+= '\n' 
f.close()
f1=open('output4.txt','w')
f1.write(result)
f1.close()