'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
        
    a = 1
    b = 0
    c = 0
    
    for _ in range(n):
        # Line below swaps the variables, avoiding having to make temp variables.
        a, b, c = a+b+c, a, b


        # This is the same as Line 13, but it helped understand the problem better.
        # tempA = a
        # tempB = b

        # a = a+b+c
        # b = tempA
        # c = tempB
    return a


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
