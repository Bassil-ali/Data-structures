#search in array element by element
def search(key,arr):
  for i in arr:
    if(i == key):
       print("in index " + str(i))


arr = [1,4,6,6,4,4,5,6,46,4,4]
key = 5

#call the search method
search(key, arr)

