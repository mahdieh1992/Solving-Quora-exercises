#Factory Method
from abc import ABC,abstractmethod

class File(ABC):
    def __init__(self,file):
        self.file = file
        
    @abstractmethod
    def make(self):
        pass
    
    def call_edit(self):
        product = self.make()
        result = product.edit(self.file)
        return result
        
class JsonFile(File):
    def make(self):
        return Json()
    
class XmlFile(File):
    def make(self):
        return Xml()


class Json:
    def edit(self,file):
        return f"working {file} "
    
class Xml:
    def edit(self,file):
        return f"working {file} "
    
    
def client(file,format):
    formats= {
        'json':JsonFile,
        'xml':Xml
    }
    
    result = formats[format](file)
    return result.call_edit()
    
print(client("show","json"))