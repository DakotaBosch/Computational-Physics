def bino(n,k):
    a=b=c=1
    for i in range(1,n+1):
        a = a*i

    for j in range(1,k+1):
        b = b*j

    for l in range(1,n-k+1):
        c = c*l
    f = int(a // b // c)    
    return f
if __name__ == "__main__":
    temp = input('gimme n: ')
    n = int(temp)
    temp = input('k: ')
    k=int(temp)

    l = int(bino(n,k))

    print('The binomial coefficient is:',l)

