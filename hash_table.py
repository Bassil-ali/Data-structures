# hash table (nested list)
hashTable = [[] for _ in range(10)]

# hash function to return key for every value
def hashing(key):
    return key % len(hashTable)

def insert(hashTable,key,value):
    hashKey = hashing(key)
    hashTable[hashKey].append(value)

def displayHash(hashTable):
    for i in range(len(hashTable)):
        print(i,end = " ")
        #to get nested element by key
        for j in hashTable[i]:
            print("-->",end = " ")
            print(j,end = " ")
        # empty print set new line
        print()

#drive insert to the  great hash table
insert(hashTable, 30, "Bassil")
insert(hashTable, 30, "ali")
insert(hashTable, 23, "php")
insert(hashTable, 23, "js")
insert(hashTable, 23, "c")
insert(hashTable, 23, "java")
insert(hashTable, 23, "python")
insert(hashTable, 23, "dart")
insert(hashTable, 23, "git")
insert(hashTable, 23, "docker")
insert(hashTable, 23, "css")
insert(hashTable, 23, "sleep :)")

insert(hashTable, 25, "laravel")
insert(hashTable, 25, "flutter")
insert(hashTable, 25, "vue.js")
insert(hashTable, 25, "bootstrap")


displayHash(hashTable)