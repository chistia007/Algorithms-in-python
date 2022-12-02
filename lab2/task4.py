def merge(A,p,q,r): # p=left, q=middle, r=right
      n1 =q - p + 1
      n2 = r - q
      L=[0]*(n1+2)
      R=[0]*(n2+2)
      for i in range(1,n1+1):
            L[i]=A[p +i- 1]
      for j in range(1,n2+1):
            R[j]=A[q + j]
      L[n1+1]=float('inf')
      R[n2+1]=float('inf')
      i=1
      j=1
      for k in range(p,r+1,+1):
            if L[i]<=R[j]:
                  A[k]=L[i]
                  i+=1
            else:
                  A[k]=R[j]
                  j+=1   
def merge_sort(A, p, r):
      if p<r:
            q=(p + r)//2  
            merge_sort(A, p, q)                        
            merge_sort(A, q+1, r)                         
            merge(A, p, q, r)
      else:
            return 0

f=open('input4.txt','r')
inputted_data=f.read().split('\n')     
f.close()
list_input=inputted_data[1].split(' ')
A=[]
for i in list_input:
      A.append(int(i))
x=merge_sort(A, 0, len(A)-1)
string=''
for i in A:
      string+=str(i) + ' '
f1=open('output4.txt', 'w')
f1.write(string)
f.close()







      

