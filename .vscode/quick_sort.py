#quick sort get pivot and make tow part of array left that has smallest element 
#and right that has greatest element and compar beatwen pivot and element and swap by conditions
def quickSort(array,first,last):
    
    L = first
    R = last
   
    #any element of array
    pivot = array[last]
    while L <= R:

        #get left index greatest of pivot
        while array[L] < pivot:
            L  = L + 1
        #get left index smallest of pivot
        while array[R] > pivot:
            R  = R - 1

        #swap with pivot
        if L <= R:
            temp = array[L]
            array[L] = array[R]
            array[R] = temp
            L = L + 1
            R = R - 1
    #call method with new started right
    if first < R:
        quickSort(array, first, R)

    #call method with new started right    
    elif L < last:
        quickSort(array, L, last)
             
array = [2,7,3,4,6,9,1]
first = 0
last  = len(array) -1

quickSort(array, first, last)

print(array)

