def Selection_sort(N,M,arr):
      min_numbers=[] # M numbers will be stored here
      for i in range(M):
            min_index=i
            for j in range(i+1,N):
                  if arr[min_index]>arr[j]:
                        min_index=j                    
            arr[i],arr[min_index]=arr[min_index],arr[i]
            min_numbers.append(arr[i])
      return min_numbers
#file i/0
file=open('input2.txt', 'r')
inputted_file=file.read().split('\n')
list_input=inputted_file[1].split(' ')
a=[]
for i in list_input:
       a.append(int(i))
final_input=inputted_file[0].split(' ')
sorted_array=Selection_sort(int(final_input[0]),int(final_input[1]),a)
print(sorted_array)
string=''
for i in sorted_array:
      string+=str(i) + ' '
file1=open('output2.txt', 'w')
file1.write(string)

