def biggie_size(arr):
    for i in range ((len(arr))):
        if arr[i] > 0 :
            arr[i]="big"
    return arr
a= [-1,2,-5,4,-2,5]
print (biggie_size(a))

print("_"*30)

#----------------------------------------------------

def Count_Positives (arr):
    count = 0
    for i in range(len(arr)) :
        if arr[i] > 0:
            count+=1
    arr[len(arr)-1]=count
    return arr
print(Count_Positives([1,2,-1,4,5]))
print("_"*30)

#----------------------------------------------------
def summation (arr):
    sum=0
    for i in range (len(arr)):
        sum+=arr[i]
    return sum

print(summation([1,4,-5]))

print("_"*30)

#----------------------------------------------------

def average (arr):
    sum=0
    for i in range (len(arr)):
        sum+=arr[i]
    avge = sum/len(arr)
    return avge

print(average([1,2,3,4]))


print("_"*30)
# -----------------------------------------------


def length (arr):
    a=len(arr)
    return a
print(len([1,2,3,4]))

print("_"*30)
# -----------------------------------------------

def Minimum(arr):
    if (arr == []):
        return False
    else:
        min=arr[0]
        for i in range(len(arr)):
            if (arr[i]<min):
                min=arr[i]
        return min
print(Minimum([]))      
    

print("_"*30)

# -----------------------------------------------


def maximum(arr):
    if (arr == []):
        return False
    else:
        max=arr[0]
        for i in range(len(arr)):
            if (arr[i]>max):
                max=arr[i]
        return max
print(maximum([5,7,8,9]))      
    

print("_"*30)


# -----------------------------------------------

def Ultimate (arr):
    sum=0
    max=arr[0]
    min=arr[0]
    avg=0
    for i in arr:
        if(i>max):
            max=i
        if (i<min):
            min=i
        sum+=i
    avg=sum/len(arr)
    return {'sumTotal':sum , 'average':avg, 'minimum':min, 'maximum':max , 'length':len(arr)}

print(Ultimate([1,2,3]))


# -----------------------------------------------

def reverse (arr):
    
    return arr[::-1]
print (reverse([1,2,3,4,5,6,7]))

# or

def reverse1 (arr):
    arr[0],arr[2]=arr[2],arr[0]
    return arr
print (reverse([1,2,3,4,5,6,7,8,9,10,11]))

print("_"*30)
# -----------------------------------------------