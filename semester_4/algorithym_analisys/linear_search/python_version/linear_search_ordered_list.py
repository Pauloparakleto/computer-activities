# The simple linear search it its worst case keep interacting with the list until reach the list end. However it is not necessary since the index movement to the right must stop as soon as it finds a number bigger than the searched one.
# This is the reason we need to break the intecation and return -1.
# Let us modify the simpl search with this new intention.

list = [-5, -3, 0, 10, 20, 30, 40, 100, 10000] # an ordered list
k = 20000 # what we are looking for. This is the worst case. It would walk though all the list until realize the number is not there.

n = 0
index = -1 # let us assume it is the default while the number is not found
# Take the k value and return its index with linear search.
while n < len(list) and k >= list[n]: # this is an invariant loop phrase
    print('n is: ' + str(n))
    if list[n] is k:
        index = n
        break
    n += 1 # increment by 1

print(index) # return the index anyway
