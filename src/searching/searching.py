def linear_search(arr, target):
  for i in range(0, len(arr)):
    if arr[i] == target:
      return i

  return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    newArr = selection_sort(arr)
    low = 0
    high = len(newArr) - 1

  # loop so long as low hasn't moved passed high
    while low <= high:
      mid = (low + high) // 2


      if arr[mid] == target: 
        return mid
      elif target < arr[mid]:
        # toss out rightside
          # set high to be mid - 1
      # Use selection_sort to sort input array

        high = mid - 1
      else:
        # toss out leftside
          # set low to be mid + 1
        low = mid + 1
      # # iterate over newArr
    # while newArr[half_index] != target:
    #   # target is less than half
    #   if int(len(newArr)/2) < target:
    #     # iterate over smaller half
    #     for i in range(0, int(len(newArr)/2)):
    #   # target is greater than half
    #   else: 
    #     # iterate over larger half 
    #     for i in range(int(len(newArr)/2), len(newArr)):


    # compare middle item to target

    return -1  # not found


def selection_sort(arr):
    # loop through n-1 elements -> the entire array
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # Swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr
