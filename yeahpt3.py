arr = []
arrb = []

x = open("yeahdamn.txt", "r")
xprime = x.read()
for num in xprime.split():
    y = int(num)
    arr.append(y)
    
y = open("yeahdamn2.txt", "r")
yprime = y.read()
for num in yprime.split():
    z = int(num)
    arrb.append(z)


def binarySearch(arr,key,low,high):
    if low > high:
        print("-1", end=" ")
        return False

    else:
        mid = int((low + high) / 2)
        if key == arr[mid]:
            print(mid + 1, end=" ")
            return mid
            
        elif key > arr[mid]:
            return binarySearch(arr,key,mid+1,high)
        
        else:
            return binarySearch(arr,key,low,mid-1)
        
        
        

for x in arrb:
    binarySearch(arr, x, 0, len(arr)-1)
    


               
        
"""
def funct(arr,arrb):
    index = []
    for x in arrb:
        i = binarySearch(x,arr)
        index.append(i)
    return index          
"""


