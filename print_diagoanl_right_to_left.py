def print_digonal_right_to_left_while_loop(a):
    r=len(a)
    i=0
    j=r-1

    while(i<r and j>=0):
        print("Diagonal Element From Right to Left : ",a[i][j])
        i+=1
        j-=1
def print_diagonal_element_right_To_Left_for_loop(a):
    r=len(a)
    j=r-1
    for i in range(r):
        print("Right To Left Diagonal Element :",a[i][j])
        j-=1
if __name__ == "__main__":
    n= int(input("Please Enter the row/coloumn value of diagonal matrix : "))
    a=[]
    print("Please Enter Matrix Element Row Wise : ")
    for _ in range(n):
        r=[]
        for _ in range(n):
            r.append(int(input()))
        a.append(r)
    print("Given Diagonal Matrix : ",a)
    # print_digonal_right_to_left_while_loop(a)
    print_diagonal_element_right_To_Left_for_loop(a)
