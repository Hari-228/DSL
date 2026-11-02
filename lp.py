class LinearProbeHashTable:

  def __init__(self, size=10):
    self.size = size
    self.table = [None] * size

  def insert(self, key):
    index = key % self.size
    original_index = index
    while self.table[index] is not None:
      index = (index + 1) % self.size
      if index == original_index:
        print("Hash Table is full!")
        return
    self.table[index] = key
    print(f"Inserted {key} at index {index}")

  def display(self):
    print("Hash Table:", self.table)


# Driver Code
ht = LinearProbeHashTable(5)
ht.insert(10)
ht.insert(15)
ht.display()