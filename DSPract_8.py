# Practical 8: Hash Table using Division Method and Chaining

size = 10
hash_table = [[] for _ in range(size)]  # Creating an empty hash table with 10 empty lists (for chaining)

def hash_function(key):
    return key % size

# Function to insert key-value pair in hash table
def insert(key, value):
    index = hash_function(key)
    for pair in hash_table[index]:
        if pair[0] == key:
            pair[1] = value
            return
    hash_table[index].append([key, value])

# Function to search value using key
def search(key):
    index = hash_function(key)
    for pair in hash_table[index]:
        if pair[0] == key:
            return pair[1]
    return None

# Function to delete a key-value pair
def delete(key):
    index = hash_function(key)
    for pair in hash_table[index]:
        if pair[0] == key:
            hash_table[index].remove(pair)
            return True
    return False

# Example
# Inserting key-value pairs
insert(11, "A")    # 11 % 10 = 1 -> goes to index 1
insert(21, "B")    # 21 % 10 = 1 -> same index (collision) -> added to chain
insert(31, "C")    # 31 % 10 = 1 -> same index again (shows chaining clearly)
insert(41, "D")
insert(51, "E")


print("Search 21:", search(21))
delete(21)
print("After deleting 21:", search(21))
print("Full Table:", hash_table)
