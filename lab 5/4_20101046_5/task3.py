def house_chore_hours(N,H,S): #H for hours and S sor calling sequences
      jack=0
      jill=0
      jack_hours=[]
      jill_hours=[]
      overall=''
      H.sort() # Quick sort since IDE's default sort does quicsort
      for i in S:
            if i=='J':
                  jack_hours.append(H[0])
                  jack+=H[0]
                  overall+=str(H.pop(0))
            if i=='j':
                  if len(jill_hours)==0:
                        jill+=jack_hours[-1]
                        jill_hours.append(jack_hours[-1])
                        overall+=str(jack_hours[-1])
                  else:
                        for i in range(-1,-len(jack_hours)-1,-1):
                              if jack_hours[i] not in jill_hours:
                                    jill+=jack_hours[i]
                                    jill_hours.append(jack_hours[i])
                                    overall+=str(jack_hours[i])
                                    break
      return jack,jill,overall

f=open('task3_input.txt','r')
N=int(f.readline())
sub=f.read().split('\n')
H=sub[0].split(' ')
H=list(map(int,H))
S=sub[1]
jack,jill,overall=house_chore_hours(N,H,S)
string=overall+ '\n'+ 'Jack will work for '+str(jack) + ' hours'+ '\n'+ 'Jill will work for '+str(jill) + ' hours'
f.close()
f1=open('output3.txt','w')
f1.write(string)
f1.close()

