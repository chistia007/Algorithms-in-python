def Multiply_matrix(A,B):
      n=len(A)
      C=[]
      for m in range(n):
          s=[0]*3
          C.append(s)
      for i in range(n):
            for j in range(n):
                  for k in range(n):
                        C[i][j]+= int(A[i][k])*int(B[k][j])
      return C

#file I/O:
f=open('input4.txt','r')
inputs=f.read().split('\n')
h=len(inputs)
A=[]
B=[]
a=[]
b=[]
l=h//2
for i in range(h):
      if i<(l):
            for j in inputs[i]:
                  if " " not in j:
                        a.append(int(j))
            A.append(a)
            a=[]
      else:
            for k in inputs[i]:
                  if " " not in k:
                        b.append(int(k))
            B.append(b)
            b=[]
strng=""
x=Multiply_matrix(A,B)
for i in x:
      for j in i:
            strng+=str(j) + " "
      strng+= '\n'
f=open('output4.txt', 'w')
f.write(strng)
f.close()





