import time
def calcProd():
    # Calculate the product of the first 100,000 numbers
    product = 1
    for i in range(1,100000):
        product = product*i
    return product

start = time.time()
prod = calcProd()
end = time.time()
print(f'The result is {len(str(prod))} digits long.')
print(f'Runtime is {round((end-start)/60,2)} minutes')