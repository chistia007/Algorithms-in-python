def sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j][1] > sub_li[j + 1][1]):
                sub_li[j],sub_li[j + 1]= sub_li[j + 1],sub_li[j]               
    return sub_li
def assignment_selection(arr,N,M):
    count=0
    counter=1
    while (arr):
      if counter==M+1:
            break
      count+=1
      arr=sort(arr)
      f=arr[0][1] #finish time
      arr.pop(0)
      l=[]
      for c in range(len(arr)):
            if c==0:
                  continue
            else:
                  if arr[c][0]>=f:
                        
                        count+=1
                        f=arr[c][1]
                        l.append(c)
      for i in l:
            arr.pop(i)
      counter+=1
    return count

f=open('task2_input.txt','r')
n=f.readline().split(' ')
N,M=(int(n[0]), int(n[1]))
arr=[]
s=f.read().split('\n')
for i in range(N):
      lst=s[i].split(' ')
      arr.append(lst)
arr=[list( map(int,i) ) for i in arr]
count=assignment_selection(arr,N,M)
f.close()
f1=open('output2.txt','w')
f1.write(str(count))

