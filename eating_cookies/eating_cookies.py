'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    # Way 1: eat 1 + 1 + 1 cookies
    # Way 2: eat 1 + 2 cookies 
    # Way 3: eat 3 cookies
    # Way 4: eat 2 + 1 cookie 
    # return should be 4
    if n == 0 or n == 1:
        return 1
    if n <= 2:
        return n
    return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
