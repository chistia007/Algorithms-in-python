def sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j][1] > sub_li[j + 1][1]):
                sub_li[j],sub_li[j + 1]= sub_li[j + 1],sub_li[j]               
    return sub_li
def assignment_selection(arr,n):
    arr=sort(arr)
    selected=[]
    selected.append(arr[0])
    count=1
    f=selected[0][1] #finish time
    for c in range(n):
        if c==0:
            continue
        else:
            if arr[c][0]>=f:
                count+=1
                f=arr[c][1]
                selected.append(arr[c])
    return count,selected

f=open('task1_input.txt','r')
n=int(f.readline())
arr=[]
s=f.read().split('\n')
for i in range(n):
    lst=s[i].split(' ')
    arr.append(lst)
arr=[list( map(int,i) ) for i in arr]
count,selected=assignment_selection(arr,n)
f.close()
string=str(count) + '\n'
count1=0
for i in selected:
    if count1==len(selected)-1:
        string+=str(i[0]) + ' ' + str(i[1])
    else:
        string+=str(i[0]) + ' ' + str(i[1])+ '\n'
    count1+=1
f1=open('output1.txt','w')
f1.write(string)

