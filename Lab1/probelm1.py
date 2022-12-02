# parity checker:
even=odd=na=0
def isParity(num):
      global even,odd,na
      if '.' in str(num):
            na+=1
            return '{} cannot have parity'.format(num)
      else:
            if int(num) & 1==0:
                  even+=1
                  return '{} has even parity'.format(num)
            else:
                  odd+=1
                  return '{} has odd parity'.format(num)
#palindrome checker:
palindrome=total=0
def isPalindrome(word):
      global palindrome,total
      total+=1
      if len(word)==0:
            return '{} is not a palindrome\n'.format(word)
      n=len(word)
      for i in range(n//2):
            if word[i]!=word[n-1-i]:
                  return '{} is not a palindrome\n'.format(word)
      palindrome+=1
      return '{} is a palindrome\n'.format(word) 
#File I/O:
file=open('input1.txt', 'r') #to read
inputted_date=file.read().split('\n')
output_text=''
for lines in inputted_date:
      sequence=lines.split()
      output_text+= isParity(sequence[0])+ ' and ' + isPalindrome(sequence[1])
file.close()
file1=open('output1.txt', 'w') #to write
file1.write(output_text)
file1.close()
file2=open('record1.txt', 'w')
file2.write('percentage of odd parity: {} % \npercentage of even parity: {} % \npercentage of no parity: {} % \npercentage of palindrome: {} % \npercentage of non-palindrome: {} % '.format(int((odd/(odd+na+even))*100),int((even/(odd+na+even))*100),int((na/(odd+na+even))*100),int((palindrome/total)*100),int(((total-palindrome)/total)*100) ))
file2.close()