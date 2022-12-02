def LCS (X,Y):
    global zone_enters
    zone_centers = {'Y': "Yasnaya",
              'P': "Pochinki",
              'S': "School",
              'R': "Rozhok",
              'F': "Farm",
              'M': "Mylta",
              'H': "Shelter",
              'I': "Prison",
              }
    m = len(X)+1
    n = len(Y)+1
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
    matchedzone_sequence = zone_centers[X[i]]
    while maximum != 0:
        if array_2d[i-1][j-1] +1 == array_2d[i][j] and array_2d[i-1][j] < array_2d[i][j]:
            matchedzone_sequence = zone_centers[X[i-1]] + " " + matchedzone_sequence
            maximum-= 1
            i -= 1
            j -= 1
        else:
            i-=1
    return (matchedzone_sequence,int(100*array_2d[-1][-1]/(N)))

f=open('input1.txt','r')
N=int(f.readline())
s=f.read().split('\n')
actual_zone=s[0]
predicted_zone=s[1]
n,p=LCS(actual_zone,predicted_zone)
output= n + '\n' + 'Correctness of prediction: ' + str(p) +'%'
f.close()
f1=open('output1.txt','w')
f1.write(output)
f1.close()









