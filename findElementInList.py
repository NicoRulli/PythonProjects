#Find in list 

ls1 = [1,2,3,4,5,6]
i = int(input("Enter a number"))

def findElement(list, int):
    element = int
    ls = list
    if element in ls: 
        return True
    else: 
        return False



boo = findElement(ls1, i)

if boo == True: 
    print("True")
else: 
    print("False")