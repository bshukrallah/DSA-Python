## Hash table should have a prime number of keys, ex: 2, 3, 5, 7, 11, 13, 17, 19, 23

class HashTable:
    def __init__(self, size = 7): # 7 would be index 0-6
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)) % len(self.data_map) # Simple algorithm to make a deterministic hash for a key
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key) #Generate hash, this will be used as the index
        if self.data_map[index] == None:
            self.data_map[index] = [] #if index is empty generate an empty list
        self.data_map[index].append([key, value]) #append [key, value] as a list to the list

hashTable = HashTable()

hashTable.print_table()
hashTable.set_item("Dog", "Reishi")
hashTable.set_item("Dog", "Apple")
hashTable.set_item("Food", "Lemon")



hashTable.print_table()