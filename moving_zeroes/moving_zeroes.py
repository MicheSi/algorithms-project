'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # number of non zero integers
    num = 0
    # loop through array
    for i in range(len(arr)):
        # if i is not zero, replace with num at arr[num]
        # increment num to change index of pointer
        if arr[i] != 0:
            arr[num] = arr[i]
            num += 1
    # set num to index of 1st 0
    # add remaining numbers from num to end of array
    while num < len(arr):
        arr[num] = 0
        num += 1
    return arr
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")