#سؤال کد پایتون
def count_executable_lines(file_path: str) -> int: 
    try:
        count = 0
        with open(file_path,'r+') as file:
            for row in file:
                strip_row = row.strip()
                if strip_row != "" and not strip_row.startswith("#"):
                     count += 1
        return count
    except FileNotFoundError:
        raise FileNotFoundError("this file is not exists in path")

path = './2/1.txt'
print(count_executable_lines(path))
