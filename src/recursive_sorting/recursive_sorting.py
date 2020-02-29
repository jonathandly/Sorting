# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # TO-DO
    merged_arr = []
    left_arr = 0
    right_arr = 0

    while left_arr < len(arrA) and right_arr < len(arrB):
        if arrA[left_arr] < arrB[right_arr]:
            merged_arr.append(arrA[left_arr])
            left_arr += 1
        else:
            merged_arr.append(arrB[right_arr])
            right_arr += 1

    merged_arr.extend(arrA[left_arr:])
    merged_arr.extend(arrB[right_arr:])
    
    return merged_arr

print(merge([1,2,3,4,5],[6,7,8,9,10]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
