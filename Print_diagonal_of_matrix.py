def left_to_right_diagonal_for_loop(a):
    m=len(a)
    for i in range(m):
        print(a[i][i])
def left_to_right_diagonal_while_loop(a):
    r=len(a)
    i=0
    while(i<r):
        print("Using While Loop Diagonal Element --",a[i][i])
        i+=1

if __name__=="__main__":
    n=int(input("Please Enter Row and column value same :"))
    a=[]
    for _ in range(n):
        r=[]
        for _ in range(n):
            r.append(int(input()))
        a.append(r)
    print("Given Matrix is : ",a)
    left_to_right_diagonal_for_loop(a)
    left_to_right_diagonal_while_loop(a)