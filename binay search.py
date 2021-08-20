def binarySearch (arr, l, r, x):
    print(arr,l,r,x)
    # Check base case
    if r >= l:
  
        mid = l + (r - l) // 2
  
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
          
        # If element is smaller than mid, then it 
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
  
        # Else the element can only be present 
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)
  
    else:
        # Element is not present in the array
        return -1
  

# Driver Code
list_number =[1,23,55,2,1,4,57,5,4,8,6]
list_number.sort()
num_input = 6
result = binarySearch(list_number, 0, len(list_number)-1, num_input)

if result !=-1:
    print(result)
else:
    print ("no in list binary search")
