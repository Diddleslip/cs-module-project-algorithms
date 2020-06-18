'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # array index counter
    counter = 0

    # we're gonna reverse array to avoid certain edge-cases.
    arr.reverse()
    # loop through whole reversed array
    for i in range(len(arr)):
        # check if value is equal to 0
        if arr[i] == 0:
            # swap value to left-most index available.
            arr[i], arr[counter] = arr[counter], arr[i]
            counter += 1
            
    # after we're done, revert the array to normal
    arr.reverse()

    return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2, 123, 32]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")