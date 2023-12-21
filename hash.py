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

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return (self.data_map[index][i][1])
        else:
            return None
        
    def get_keys(self):
        keys = []
        for each_hash in self.data_map:
            if(each_hash is not None):
                for each_key in each_hash:
                    keys.append(each_key[0])            
        return keys
    
    def check_if_key_exists(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for item in self.data_map[index]:
                if item[0] == key:
                    return True
        return False
    
def list_compare(list1, list2): #compare two lists, will return true if there is a duplicate key in the two lists
    dictionary = {}
    for item in list1:
        dictionary[item] = None
    for item in list2:
        if item in dictionary:
            return True
    return False

hashTable = HashTable()

hashTable.print_table()
hashTable.set_item("Dog", "Reishi")
hashTable.set_item("Dog", "Apple")
hashTable.set_item("Food", "Lemon")

hashTable.print_table()

print(hashTable.get_item("Dog"))
print(hashTable.get_keys())

list1 = ['dog', 'apple', 'orange']
list2 = ['cat', 'monkey', 'dog']
print(list_compare(list1, list2))

print(hashTable.check_if_key_exists("Cat"))
print(hashTable.check_if_key_exists("Dog"))