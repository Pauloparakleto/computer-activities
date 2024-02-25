# Binary Search
# If the keys at list[1..n] are sorted, compare k to list[n/2] key.
# 1) k = list[n/2] key;
# 2) k < list[n/2] key then search in list[0..((n/2)-1)];
# 3) k > list[n/2] key then search in list[((n/2)+1)..n]
#
# Apply the loop invariant phrase concept
# 
list = [7]
length = len(list)
left = 0
right = int(length / 2)
k = 7

result = -1

while left <= right:
    if k is list[right]:
        print(str(k) + ' was found at index ' + str(right))
        result = right
        break


print(result)
