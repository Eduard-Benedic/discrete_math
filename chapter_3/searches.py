
def max(arr):
    maxEl = arr[0]
    for el in arr:
        if el > maxEl:
            maxEl = el
    return maxEl

print(max([1,2,3, 200, 10, 300]))


num_sequence = [1,4,5,6,12,20,200]

def linear_search(arr, num):
    arr_length = len(arr)
    location = 0
    for x in range(len(arr)):
        if arr[x] == num:
            location = x
    return location
        

loc_num = linear_search(num_sequence, 20)


binary_arr_search = [1, 2, 3, 5, 6, 7, 8, 10, 12, 13, 20, 22]


def binary_search(arr, num):
    half = len(arr) // 2
    if arr[half] == num:
        return True
    if  num < arr[half]:
        return binary_search(arr[0:half], num)
    else:
        return binary_search(arr[half:], num)

founded = binary_search(binary_arr_search, 2)

print(founded)


