from binomial import bino

n= int(input('Hello user, please enter the desired number of lines:'))
temp=[0]
for x in range(0,n+1):
    temp = [0]*(x+1)
    for y in range(0,x+1):       
        temp[y] = int(bino(x,y))       
    print(temp)
    
    