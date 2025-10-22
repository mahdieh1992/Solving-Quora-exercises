#عدد جادویی
class Strint(int):
    def __lt__(self, other):
        number = self % 10
        other = other % 10
        return number < other
    
    def __gt__(self, other):
        number = self % 10
        other = other % 10
        return number > other

    def __le__(self, other):
        number = self % 10
        other = other % 10
        return number <= other

    def __ge__(self, other):
        number = self % 10
        other = other % 10
        return number >= other

    def __eq__(self, other):
        number = self % 10
        other = other % 10
        return number == other

    def __ne__(self, other):
        number = self % 10
        other = other % 10
        return number != other      

    def __add__(self, other): 
        concat = str(self) + str(other)   
        return int(concat)
    
    def __sub__(self, other):
        self = str(self)
        other = str(other)
        if self.endswith(other):
            self = self.rstrip(other)
            if self == "":
                self = 0
            return int(self)
        raise ValueError("The subtraction is not valid!")

    def __len__(self):
        self = str(self)
        return len(self)

    def __call__(self):
        self = str(self)
        dict_number = {
            '0' : '۰',
            '1': '۱',
            '2': '۲',
            '3': '۳',
            '4': '۴',
            '5': '۵',
            '6': '۶',
            '7': '۷',
            '8': '۸',
            '9': '۹'
        }
        result = "".join([dict_number[num] for num in self])
        return result

      

strint1 = Strint(232425)
print(strint1.__call__())
