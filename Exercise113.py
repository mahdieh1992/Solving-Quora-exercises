#مدیریت فایل‌ها
import os
from shutil import copyfile
list_temp = []
class FileManager:
    def find(self, name: str, address: str) -> list:
        list_file = []
        for dir,sub_dir,files in os.walk(address):
            for file in files:
                if file == name:
                    list_file.append(f"{dir}/{file}")
        return list_file
                    

    def create_file(self, name: str, address: str) -> None:
        path = os.path.join(address,name)
        if not os.path.isfile(path) :
            with open(path,'w') as file:
                pass
               
    def create_dir(self, name: str, address: str) -> None:
        path = os.path.join(address,name)
        if not os.path.isdir(path):
             os.mkdir(path)

    def delete(self, name: str, address: str) -> None:
        path = os.path.join(address,name)
        if os.path.isfile(path):
            path_temperary = os.path.join(address,name)
            list_temp.append(path_temperary)
            os.remove(path)
    def restore(self, name: str) -> None:
        ...


fm = FileManager()

# ساختار اولیه
fm.create_dir('test_fm', '.')
fm.create_dir('test1', 'test_fm')
fm.create_dir('test2', 'test_fm/test1')

# ایجاد فایل‌ها
fm.create_file('document.txt', 'test_fm')
fm.create_file('document.txt', 'test_fm/test1')
fm.create_file('document.txt', 'test_fm/test1/test2')
fm.create_file('another.txt', 'test_fm')
# ساختار اولیه
fm.delete('document.txt', 'test_fm')
fm.delete('document.txt', 'test_fm/test1/')
fm.delete('document.txt', 'test_fm/test1/test2')

print(list_temp)