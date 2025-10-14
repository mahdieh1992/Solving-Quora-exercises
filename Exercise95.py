#بازی فولدر‌های خسته
import os
def extension_combat(salib_format: str, sajjad_format: str, path: str) -> str:
    title_files = {}
    salib_format = salib_format.lower()
    sajjad_format = sajjad_format.lower()
    count_salib = 0
    count_sajjad = 0
    for root,dir,files in os.walk(path):
        for file in files:
            file = file.lower()
            split_title = file.rsplit('.',1)
            key = split_title[0]
            suffix = split_title[1]
            if file.endswith(salib_format):
                count_salib +=1
            if file.endswith(sajjad_format):
                count_sajjad +=1
            if suffix != sajjad_format:
                if key not in title_files:
                    title_files[key] = {}
                    title_files[key]['count'] = 1
                    title_files[key]['suffix'] = [suffix]
                else:
                    title_files[key]['count'] += 1
                    title_files[key]['suffix'].append(suffix)
    if count_sajjad > count_salib:
        return "Win! Normally!"
    else:
        for key,val in title_files.items():
            check_salib = sum(1 for suffix in title_files[key]['suffix'] if suffix == salib_format)
            total_salib = count_salib - check_salib
            if title_files[key]['count'] + count_sajjad > total_salib:
                return f"Win! you can win if you cheat on '{key}'!"
        return "Lose! you can't win this game!"               
    
print(extension_combat('jpg','png',"G:\\files1"))
