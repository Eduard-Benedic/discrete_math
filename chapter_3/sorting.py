from time import time

start = time()

items = [6, 3, 1, 2, 44442, 323,55, 331, 5, 32, 11, 33, 3444, 12393, 3945, 123]

def bubble_sort(arraySource):
    for i in range(len(arraySource)):
        shortened_list = len(arraySource) - 1
        for j in range(shortened_list):
            if arraySource[j] > arraySource[j + 1]:
                a = arraySource[j + 1]
                arraySource[j + 1] = arraySource[j]
                arraySource[j] = a
        shortened_list -= 1
    return arraySource

sorted_items = bubble_sort(items)

end = time()


def insertion_sort(items):
    for i in range(1, len(items)):
        for k in range(0, i+1):
            if items[i] < items[k] and not i == len(items):
                el = items[i]
                items.pop(i)
                items.insert(k, el)
    return items

                

arr_insertion = [3, 2, 4, 1, 5]
# arr_insertion.insert(1, 30)
# print(arr_insertion)

sorted_insert = insertion_sort(arr_insertion)

print(sorted_insert)