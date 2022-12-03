import array as ar 
myarr = ar.array('l' , [] )

def Lsearch(arr):
    v = int(input("Enter Value to search : "))
    t = -1
    for i in range(len(arr)):
        if v == arr[i] :
            print("Element is found at " , i)
            t = i
    if t == -1:
        print("Element is not found")

def show(myarr):
        print("Array is : ")
        for i in myarr:
            print(i , end=' ')
        print()

def BubbleSort(myarr):
    l = len(myarr)
    for i in range(l-1):
        for j in range(l-i-1):
            if myarr[j]>myarr[j+1]:
                myarr[j] , myarr[j+1] = myarr[j+1] , myarr[j]
    show(myarr)
    return myarr

while True:
    print()
    print("---------------------------------------------")
    print("1.Insert \n2.Delete \n3.Display\n4.Search\n5.Sort \n6.Quit")
    ch = int(input("Enter Choice : "))
    if ch == 1:
        print("\t1.Insert at Start\n\t2.Insert at Last \n\t3.Insert at specific location ")
        a = int(input("Enter choice : "))
        if a == 1:
            temp = int(input("Enter value(Start) : "))
            myarr.insert(0 , temp)
        elif a  == 2:
            temp = int(input("Enter value(Last) : "))
            myarr.append(temp)
        elif a  == 3:
            temp = int(input("Enter value : "))
            v = int(input("Enter index value : "))
            myarr.insert(v , temp)
        else:
            print("Incorrect input")
        show(myarr)
    elif ch == 2:
        print("\t4.Delete front \n\t5.Delete last \n\t6.Delete by Index \n\t7.Delete by value")
        a= 0
        a = int(input("Enter choice : "))
        if a == 4:
            myarr.pop(0)
        elif a == 5:
            myarr.pop()
        elif a == 6 :
            v = int(input("Enter index : "))
            myarr.pop(v)
        elif a == 7:
            v = int(input("Enter value : "))
            myarr.remove(v)
        else:
            print("Incorrect Input")
        show(myarr)
    elif ch == 3:
        show(myarr)
    elif  ch == 4:
        show(myarr)
        Lsearch(myarr)
    elif ch == 5:
        show(myarr)
        print("After Sorting")
        BubbleSort(myarr)
    elif ch == 6:
        break
    else:
        print("!!!!!!!!!!!Enter correct option!!!!!!!!!!!")