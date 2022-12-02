def bubbleSort(arr):
      for i in range(len(arr)-1):
            count=0
            for j in range(len(arr)-i-1): 
                  if arr[j] > arr[j+1]:
                        arr[j], arr[j+1]=arr[j+1], arr[j]
                        count+=1
            if count==0: 
                  break
      return arr
#file i/0
file=open('input1.txt', 'r')
inputted_file=file.read().split('\n')
list_input=inputted_file[1].split(' ')
a=[]
for i in list_input:
      a.append(int(i))
s=bubbleSort(a)
final_output=""
for i in s:
      final_output=final_output + str(i) + " "
f=open('output1.txt', 'w')
f.write(final_output)
f.close()
# comment: 
# if count is 0 then the array is already sorted and will break out of the loop.
# for already an sorted array the, the first for loop will run only 1 time and thus the time complexity for best case will be Theta(n).

