list = [16, 9, -3, 5, 4, 27, 46, 11, -5]
k = 2
n = 0
index = -1 # let us assume it is the default while the number is not found
# Take the k value and return its index with linear search.
while n < len(list):
    print('n is: ' + str(n))
    if list[n] is k:
        index = n
    n += 1 # increment by 1

print(index) # return the index anyway
