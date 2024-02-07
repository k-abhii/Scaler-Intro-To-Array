def matrix_row_sum(a):
    n= len(a)
    m=len(a[0])
    for i in range(n):
        sum=0
        for j in range(m):
            sum+=a[i][j]
        print(sum)
if __name__ =="__main__":
    r=int(input("Please Enter the Number of rows: "))
    c=int(input("Please Enter the Number of coloumns: "))
    a=[]
    print("Please Enter Matrix Values Row wise: ")
    for _ in range(r):
        r=[]
        for _ in range(c):
            r.append(int(input()))
        a.append(r)
    print(a)
    matrix_row_sum(a)



