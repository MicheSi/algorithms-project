'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n):
#     # Your code here
#     # Can eat 0, 1, 2, or 3 cookies at a time
#     # return should be 4
#     if n == 0 or n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 4
#     return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

# with cache
def eating_cookies(n, cache=None):
    # Your code here
    if cache is None:
        cache = {}
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    elif cache and cache[n]:
        return cache[n]
    else:
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

# Sean's code
# def eating_cookies(n, cache=None):
#     # Your code here
#     if n == 0:
#         return 1
#     elif n <= 0:
#         return 0
#     elif cache and cache[n] > 0:
#         return cache[n]
#     else:
#         if not cache:
#             cache= [0 for _ in range(n + 1)]
#         cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
#     return cache[n]