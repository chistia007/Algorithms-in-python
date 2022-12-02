def insertion_sorting(N,arr1,arr2):
      for i in range(N-1):
            temp=arr2[i+1]
            temp1=arr1[i+1]
            j=i
            while j>=0:
                  if temp>arr2[j]:
                        arr2[j+1]=arr2[j] #shift to the right side and creates hole
                        arr1[j+1]=arr1[j]
                  else:
                        break
                  j-=1
            arr2[j+1]=temp                #fill up the last hole
            arr1[j+1]=temp1
      return arr1
#file i/o:
f=open('input3.txt','r')
input_text=f.read().split('\n')
f.close()
a=[]
b=[]
list1=input_text[1].split(' ')
list2=input_text[2].split(' ')
for i in list1:
      a.append(int(i))
for j in list2:
      b.append(int(j))
final=insertion_sorting(5,a,b)
string=''
for i in final:
      string+= str(i) + ' '
f1=open('output3.txt','w')
f1.write(string)
f.close()
