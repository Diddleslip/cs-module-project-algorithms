'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here

    newArr = []
    start = 0

    for i in nums[k - 1:]:
        newArr.append(max(nums[start:k]))
        start += 1
        k += 1
    # print(newArr)
    # print(max(nums[:k])) ## This give us the max number!
    return newArr




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
