'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    # make new array of products
    products = [0 for _ in range(len(arr))]
    # will need to get product of each integer before current
    # store product so far
    curr_prod = 1
    # loop through array and get new product
    for i in range(len(arr)):
        # set index
        products[i] = curr_prod
        # multiply numbers not including index
        curr_prod *= arr[i]
    # get product of each int after current
    # store product so far of other integers
    curr_prod = 1

    for i in range(len(arr) - 1, -1, -1):
        products[i] *= curr_prod
        curr_prod *= arr[i]
    
    return products

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
