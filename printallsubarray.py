def printallsubarray(a):
    n= len(a)
    for i in range(n):
        for j in range(i,n):
            for k in range(i,j+1):
                print(a[k],end=" ")
            print()
if __name__ == "__main__":
    a = list(map(int,input().split()))
    printallsubarray(a)