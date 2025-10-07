#سازماندهی رسانه
import sys,os,time
if len(sys.argv) < 3:
    sys.exit()
else:
    inputs = sys.argv
    source = inputs[1]
    dest = inputs[2]
    if os.path.exists(source):
        suffix_photo = ["jpg", "jpeg", "png"]
        suffix_video = ["mp4", "avi", "3gp", "mpeg", "mkv", "wmv", "mov"]
        for root,dir,files in os.walk(source):
           for file in files:
                path_File = os.path.join(root,file)
                get_year = time.ctime(os.path.getmtime(path_File)).split()[-1]  
                l_File = file.lower()
                folder_name = ''
                if any (l_File.endswith(f".{sp}") for sp in suffix_photo):
                    folder_name = 'photos'
                elif any (l_File.endswith(f".{sv}") for sv in suffix_video):
                    folder_name = 'videos'
                else:
                    continue
                dest_path = os.path.join(dest,get_year,folder_name)
                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)
                dest_path = os.path.join(dest_path,file)
                with open(path_File,'rb') as src_file, open(dest_path,'wb') as dst_file:
                    dst_file.write(src_file.read())                                                                                
    else:
        print("this path is not exists")
    

