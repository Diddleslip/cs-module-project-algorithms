'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
from collections import Counter
def single_number(arr):
    # Your code here
    # Have all of the values ran through and keep track of how many were put for each value.
    list = dict(Counter(arr))
    # Now pick out the key/value pair that only was inputted once.
    for key, value in list.items():
        # if a value is set to 1, then return it's key
        if value == 1:
            return key


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")