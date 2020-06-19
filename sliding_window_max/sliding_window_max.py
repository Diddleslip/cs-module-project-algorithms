'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
from collections import deque

def sliding_window_max(nums, n, k):
    # Your code here

    # newArr = []
    # start = 0

    # for _ in nums[k - 1:]:
    #     newArr.append(max(nums[start:k]))
    #     start += 1
    #     k += 1
    # # print(newArr)
    # # print(max(nums[:k])) ## This give us the max number!
    # return newArr

    """ Create a Double Ended Queue, Qi that  
    will store indexes of array elements.  
    The queue will store indexes of useful  
    elements in every window and it will 
    maintain decreasing order of values from 
    front to rear in Qi, i.e., arr[Qi.front[]] 
    to arr[Qi.rear()] are sorted in decreasing 
    order"""
    Qi = deque() 
      
    # Process first k (or first window)  
    # elements of array 
    for i in range(k): 
        
        # For every element, the previous  
        # smaller elements are useless 
        # so remove them from Qi 
        while Qi and arr[i] >= arr[Qi[-1]] : 
            Qi.pop() 
          
        # Add new element at rear of queue 
        Qi.append(i); 
          
    # Process rest of the elements, i.e.  
    # from arr[k] to arr[n-1] 
    for i in range(k, n): 
          
        # The element at the front of the 
        # queue is the largest element of 
        # previous window, so print it 
        print(str(arr[Qi[0]]) + " ", end = "") 
          
        # Remove the elements which are  
        # out of this window 
        while Qi and Qi[0] <= i-k: 
              
            # remove from front of deque 
            Qi.popleft()  
          
        # Remove all elements smaller than 
        # the currently being added element  
        # (Remove useless elements) 
        while Qi and arr[i] >= arr[Qi[-1]] : 
            Qi.pop() 
          
        # Add current element at the rear of Qi 
        Qi.append(i) 




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, len(arr), k)}")
