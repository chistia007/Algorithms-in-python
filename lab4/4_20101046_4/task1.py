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

def Dijkstra(Graph,source):
    dist=[float('inf')]*(len(Graph)+1)
    prev=[None]*(len(Graph)+1)
    visited=[False]*(len(Graph)+1)
    dist[source]=0
    priority_queue=[]
    for v in Graph:
        heapq.heappush(priority_queue,[dist[v],v])
    while (priority_queue):
        u=heapq.heappop(priority_queue)[1]
        if visited[u]:
            continue
        else:
            visited[u]=True
        for v in Graph[u]:
            alt= dist[u]+ Graph[u][v]
            if alt<dist[v]:
                dist[v]=alt
                prev[v]=u
                heapq.heappush(priority_queue,[dist[v],v])
    return dist[-1]  #the last distance value
result=''
f=open('input1.txt','r')
T=f.readline()
for i in range(int(T)):
    x=f.readline().split()
    N=x[0]  #vertices/places
    M=x[1]  #edges
    graph=graph_creation(N,M)
    result+= str(Dijkstra(graph,1)) + '\n'
f.close()
f1=open('output1.txt','w')
f1.write(result)
f.close()