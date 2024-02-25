# Binary Search
# If the keys at list[1..n] are sorted, compare k to list[n/2] key.
# 1) k = list[n/2] key;
# 2) k < list[n/2] key then search in list[0..((n/2)-1)];
# 3) k > list[n/2] key then search in list[((n/2)+1)..n]
#
# Apply the loop invariant phrase concept
# 
list = [-5, -3, 0, 10, 20, 30, 40, 100, 10000]
length = len(list)
left = 0
right = length - 1
k = -5

result = -1

while left <= right:
    print('left is: ' + str(left))
    print('right is: ' + str(right))
    print('k is: ' + str(k))
    print('list number is: ' + str(list[right]))

    if k is list[right]:
        print(str(k) + ' was found at index ' + str(right))
        result = right
        break
    if k < list[right]:
        print(str(k) + ' is less than ' + str(list[right]))

        right = int(right / 2)
        print('the new middle right index is: ' + str(right))


print(result)
