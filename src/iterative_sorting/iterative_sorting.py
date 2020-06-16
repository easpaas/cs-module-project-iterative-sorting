# TO-DO: Complete the selection_sort() function below
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



def bubble_sort(arr):
    # n = len(arr)
    # while not n <= 1:
    #     newn = 0
    #     for i in range(1, (n-1)):
    #         if arr[i-1] > arr[i]:
    #             arr[i-1], arr[i] = arr[i], arr[i-1]
    #             newn = i 
    #     n = newn
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr


# example code from guided lecture for insertion sort
'''
class Book:
    def __init__(self, title, author, genre):
        self.title = title 
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"{self.title}"

def insert_sort():
    for i in range(1, len(arr_of_books)):
        curr_book = arr_of_books[i]
        book_index = i

        while book_index > 0 and curr_book.title < arr_of_books[book_index -1].title:
            arr_of_books[book_index], arr_of_books[book_index -1] = arr_of_books[book_index]

        # Always decrement index when doing a swap
            book_index -= 1

    return arr_of_books
'''