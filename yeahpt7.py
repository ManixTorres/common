import sys
arr = []

 
 
def coins(arr):
    array = []
    n = arr.length()
    array.resize(n,0)
    for i in range(2,n):
        array[i] = max(arr[i] + array[i-2], array[i-1])
    return array[n-1]



def main():
    n = 0
    lines = []    
    for line in sys.stdin:
        lines.append((line))

