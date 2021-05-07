


#1Countdown

def countdown2 (N):
    arr=[]
    for i in range(N,-1,-1):
        arr.append(i)
    return arr 

print(countdown2(5))

print("_" * 30) 

#2Print and Return

def p_r (arr):
    print (arr[0])
    return arr[1]

print (p_r([5,2]))


print("_" * 30) 

#3First Plus Length

def f (arr):
    return(arr[0]+len(arr))
arr=[5,5,6,8,6]
print(f(arr))

print("_" * 30) 

#4Values Greater than Second

def greater_than_second (arr):
    arr2 =[]
    if((len(arr))<2):
        return False
    for i in arr :
        if i > arr[1]:
            arr2.append(i)
    return(arr2)        
print(greater_than_second([1,2,3,5,4,6]))
print(greater_than_second([1]))


print("_" * 30) 

#5This Length, That Value

def length_and_value (a,b):
    arr=[]
    for i in range (0,b):
        arr.append(a)
    return arr

print(length_and_value(5,6))