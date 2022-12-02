def LCS (X,Y):
    m = len(X)+1
    n = len(Y)+1
    global array_2d
    array_2d = []
    for i in range(m):
        c = [0]*n
        array_2d.append(c)
    for i in range(1,m):
        for j in range(1,n):
            if X[i-1] == Y[j-1]:
                array_2d[i][j] = array_2d[i-1][j-1] + 1
            else:
                array_2d[i][j] = max(array_2d[i-1][j],array_2d[i][j-1])
    maximum = array_2d[-1][-1]-1
    i,j = (-1,-1)
    zone_sequence_initial=X[i]
    while maximum is not 0:
        if array_2d[i-1][j-1] +1 == array_2d[i][j] and array_2d[i-1][j] < array_2d[i][j]:
            zone_sequence_initial = X[i-1] + zone_sequence_initial
            maximum-= 1
            i -= 1
            j -= 1
        else:
            i-=1
    return (zone_sequence_initial)

f=open('input2.txt','r')
s=f.read().split('\n')
first_two=LCS(s[0],s[1]) 
all_three=LCS(first_two,s[2])
f.close()
f1=open('output2.txt','w')
f1.write(str(array_2d[-1][-1]))
f1.close()









