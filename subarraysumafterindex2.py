def printingsubarraysumstartingatindex2(a):
    n= len(a)
    sum=0
    for i in range(2,n):
        sum+=a[i]
        print(sum)
if __name__ == "__main__":
    a= list(map(int,input().split()))
    printingsubarraysumstartingatindex2(a)