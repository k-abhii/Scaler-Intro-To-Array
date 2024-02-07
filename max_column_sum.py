def max_column_sum(a):
    r=len(a)
    max_sum=float("-Inf")
    c=len(a[0])
    for j in range(c):
        sum=0
        for  i in range(r):
            sum+=a[i][j]
        print("Column wise Sum: ",sum)
        max_sum = max(sum,max_sum)
    print("Maximum Column Sum : ",max_sum)
if __name__ == "__main__":
    r= int(input("Please Enter Number of Rows: "))
    c= int(input("Please Enter Number of column:"))
    print("Please Enter Matrix Values Row wise: ")
    a=[]
    for _ in range(r):
        r=[]
        for _ in range(c):
            r.append(int(input()))
        a.append(r)
    print("Given Matrix is : ",a)
    max_column_sum(a)


