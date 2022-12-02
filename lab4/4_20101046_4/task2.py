import heapq

def graph_creation(V,E): # V for vertex and E for edges
    graph={}
    for i in range(1,int(V)+1):
        graph[i]={}
    for i in range(1,int(E)+1):
        line=f.readline().split(' ')
        graph[int(line[0])] [int(line[1])]= int(line[2])
    return graph

def Dijkstra(Graph,source):
    dist=[float('inf')]*(len(Graph)+1)
    prev=[0]*(len(Graph)+1)   #parent node
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
                prev[v]=u#parent node 
                heapq.heappush(priority_queue,[dist[v],v])
    n=len(graph)
    s=''
    while n!=source:
        s= ' ' + str(n) + s
        n= prev[n]
    s= str(source) + s
    return s
      
result=''
f=open('input2.txt','r')
T=f.readline()
for i in range(int(T)):
    x=f.readline().split()
    N=x[0]  #vertices/places
    M=x[1]  #edges
    graph=graph_creation(N,M)
    result+= str(Dijkstra(graph,1)) + '\n'
f.close()
f1=open('output2.txt','w')
f1.write(result)
f.close()