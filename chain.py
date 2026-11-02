class ChainingHashTable:

  def __init__(self, size=10):
    self.size = size
    self.table = [[] for _ in range(size)]

  def insert(self, key):
    index = key % self.size
    self.table[index].append(key)
    print(f"Inserted {key} at index {index}")

  def search(self, key):
    index = key % self.size
    if key in self.table[index]:
      print(f"Key {key} found at hash index {index}")
      return True
    print(f"Key {key} not found")
    return False

  def delete(self, key):
    index = key % self.size
    if key in self.table[index]:
      self.table[index].remove(key)
      print(f"Deleted {key}")
    else:
      print(f"Key {key} not found for deletion")


# Driver Code
ht = ChainingHashTable()
ht.insert(15)
ht.insert(25)
ht.search(15)
ht.delete(15)