

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):

#         for i in range(n):

#             for j in range(0, n-1):
#                 if arr[j] > arr[j+1]:
#                    arr[j], arr[j+1] = arr[j+1], arr[j]
# arr = [64, 34, 25, 12, 22, 11,99]
# bubble_sort(arr)
# print("Sorted array is")
# for i in range(len(arr)):
#     print(arr[i])



# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
#     return arr


# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i -1 
#         while j >= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1
#             arr[j+1] = key
#         return arr
# arr = [64, 34, 25, 12, 22, 11, 99]
# sorted_arr = insertion_sort(arr)
# print(sorted_arr)


# def selectionSort(array, size):
#     for ind in range(size):
#         min_index = ind 
#         for j in range(ind + 1, size):
#             if array[j] < array[min_index]:
#                 min_index = j
#         (array[ind], array[min_index]) = (array[min_index], array[ind])
# arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
# size = len(arr)
# selectionSort(arr, size)
# print('The array after sorting in Ascending Order by seletion sort is:')
# print(arr)


def partition(array, low, high):
    # choose the rightmost element as pivot

    pivot = array [high]
# pointer for greater element 
    i = low-1
# traverse through all elements
#  compare each element with pivot 
    for j in range(low, high):
        if  array [j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pionted by i
            i = i + 1
            # Swap the pivot element with the greater element specified by i
            swap it with the greater element pionted by i
# function to perform quicksort
