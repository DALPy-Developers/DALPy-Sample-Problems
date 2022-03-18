from dalpy.arrays import Array


# ************************** DO NOT MODIFY ABOVE THIS LINE ******************************

def duplicate_array_incorrect(arr):
    new_arr = Array(arr.length())
    for i in range(int(arr.length()/2)):
        new_arr[i+int(arr.length()/2)] = arr[i]
        new_arr[i] = arr[i]
    # Returning a new array is erroneous here and will trigger a warning.
    return arr


def duplicate_array(arr):
    for i in range(int(arr.length()/2)):
        arr[i+int(arr.length()/2)] = arr[i]
