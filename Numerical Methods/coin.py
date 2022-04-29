from binomial import bino

temp = input('Hello user, please give a number of coin flips: ')
m = int(temp)
temp = input('Now please enter a number of times it comes up heads:')
n = int(temp)


q = int(bino(m,n))
p = q/(2**m)

print('Here is the probability that the coin comes up heads exactly',n,'times',"%.4f" % p)

r=0
for i in range(n,m+1):
    r += (bino(m,i))/(2**m)
    
print('Here is the probability that the coin comes up heads',n, 'times or more',"%.4f" %r)