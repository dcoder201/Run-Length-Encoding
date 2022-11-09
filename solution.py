#Your task is to complete this function
#Function should return complete string
def encode(arr):
    # Code here
    i = 0
    count = 0
    res = ''
    while (i < len(arr)):
        if i + 1 < len(arr) and arr[i] == arr[i+1]:
            count += 1
        else:
            count += 1
            res += arr[i] + str(count)
            count = 0
        i+= 1
    return res


#{ 
 # Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends
