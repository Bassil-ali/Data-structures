#selection sort take first element and second element and swap by condition
def selectionSort(array,size):
    for i in range(size):
        #get index to min
        min = i
        #get second index 
        for j in range(i+1,size):
            #compare second element with first element if smallest of them
            if array[j] < array[min]:
                #if condition true get second index to min
                min = j
        #swap by second index 
        if i != min:
            temp = array[i]
            array[i] = array[min]
            array[min] = temp

array = [1,4,5,3,2,6,7,5,9,8]
size = len(array)
selectionSort(array,size)

#print array after sorted
print(array)