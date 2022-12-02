graph={}
f=open('input1.txt', 'r')
inputted_data=int(f.readline())
for i in range(inputted_data):
      n=f.readline().split('\n')
      n=n[0].split('\t')
      graph[n[0]]=n[1:]
f.close()
print(graph) #you may print the graph if you want



      

