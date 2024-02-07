def printsumofsubarraybruteforce(a):
    n= len(a)
    for i in range(n):
        for j in range(i,n):
            sum=0
            for k in range(i,j+1):
                sum+=a[k]
            print(sum)
if __name__ == "__main__":
    a= list(map(int,input().split()))
    printsumofsubarraybruteforce(a)
