# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        # TO-DO: swap

    return arr

l = [41,22,9,65,104,13,5,99,0,10,22]
print(selection_sort(l))
l2 = ['e','Z','l','H','n','T','t','c','V']
print(selection_sort(l2))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    for i in range(len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


b = [801, 1111, 26, 924, 1, 0, 214, 43, 201]
print(bubble_sort(b))
b2 = ['e','X','h','N','a','A','w','R','q']
print(bubble_sort(b2))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr