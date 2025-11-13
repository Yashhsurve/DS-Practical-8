# Practical 8: Hash Table using Chaining

# Function to create hash table
hash_table = [[] for _ in range(10)]

def hash_func(key):
    return key % 10  # division method

def insert(key, value):
    index = hash_func(key)
    hash_table[index].append((key, value))
    print("Inserted:", (key, value))

def search(key):
    index = hash_func(key)
    for pair in hash_table[index]:
        if pair[0] == key:
            print("Found:", pair[1])
            return
    print("Not found")

def delete(key):
    index = hash_func(key)
    for pair in hash_table[index]:
        if pair[0] == key:
            hash_table[index].remove(pair)
            print("Deleted:", key)
            return
    print("Key not found")

# Menu
while True:
    print("\n1.Insert  2.Search  3.Delete  4.Display  5.Exit")
    ch = int(input("Enter choice: "))
    
    if ch == 1:
        k = int(input("Enter key: "))
        v = input("Enter value: ")
        insert(k, v)
    elif ch == 2:
        k = int(input("Enter key: "))
        search(k)
    elif ch == 3:
        k = int(input("Enter key: "))
        delete(k)
    elif ch == 4:
        print("Hash Table:", hash_table)
    else:
        break

