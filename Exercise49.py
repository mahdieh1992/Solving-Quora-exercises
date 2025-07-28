# تغییر فایل
with open("entry_file.txt","r+") as myFile:
    get_n = myFile.readline()
    myFile.seek(0)
    myFile.read(int(get_n))
    position = myFile.tell()
    myFile.seek(position)
    myFile.write("#\n")
    myFile.seek(0)
    print(myFile.read())
