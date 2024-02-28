# Binary Search
# If the keys at list[1..n] are sorted, compare k to list[n/2] key.
# 1) k = list[n/2] key;
# 2) k < list[n/2] key then search in list[0..((n/2)-1)];
# 3) k > list[n/2] key then search in list[((n/2)+1)..n]
#
# Apply the loop invariant phrase concept
# 
list = [6, 7]
length = len(list)
left = 0
right = int((length / 2) - 1)
k = 8

result = -1

while len(list) > 0:
    print('comparing ' + str(k) + ' to ' + str(list[right]))
    if k is list[right]:
        print(str(k) + ' was found at index ' + str(right))
        result = right
        break
    if k < list[right]:
        right = int((len(list) / 2) - 1)
        list = list[left:right]
        print(list)
        print(right)
    if k > list[right]:
        print(str(k) +  ' is greater than ' + str(list[right]))
        left = int((len(list) / 2) + 1)
        right = int((len(list) / 2) - 1)
        list = list[(left - 1):(right + 1)]
        print(right)
        print(list)
        


print(result)
