import os,re
def explore(extension: str,directory_path: str) -> dict[str, int]:
    pattern = r'w*\.\w+'
    result = {}
    for root,dirs,files in os.walk(directory_path):
        for file in files:
            sub_string = "".join(re.findall(pattern,file))
            if sub_string:
                new_sub = sub_string.lower()
                file = file.replace(sub_string,new_sub)
            if file.endswith(f".{extension}"):
                result[root] = result.get(root,0) + 1
    return result

extension = "png"
directory_path = "G:\Files"
print(explore(extension,directory_path))