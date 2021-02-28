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


print(sorted_items)

