#وارون‌پیما
class Reverse:
    def __init__(self,data):
        self._data = list(data)
        self.index = len(self._data) - 1
                
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= 0:
            get_value = self._data[self.index]
            self.index -= 1
            return get_value
        raise StopIteration
     
ls = [10, 20, 30]

print("Reverse iteration")
for it in Reverse(ls):
    print(it)

print("Original list:")
print(ls)