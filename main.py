from pathlib import Path
import os
def readfileandfolder():
    path=Path("File-Handling")
    items=list(path.rglob('*'))
    for i,item in enumerate(items):
        print(f"{i+1} : {item}")

def createfile():
    try:
        readfileandfolder()
        name=input("tell ur file name:")
        folder=Path("File-Handling")
        p=folder/name
        if not p.exists():
            with open(p,"w") as fs:
                data=input("what u want to write in the file:")
                fs.write(data)
            print(f"file created successfully")
        else:
            print("file already exists")
    except Exception as err:
        print(f"Error is as {err}")


def readfile():
    try:
        readfileandfolder()
        name=input("which file u want to read:")
        folder=Path("File-Handling")
        p=folder/name
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data=fs.read()
                print(data)
            print("file readed successfully")
        else:
            print("file does not exists")
    except Exception as err:
        print(f"error as {err}")




def updatefile():
    try:
        readfileandfolder()
        name=input("tell which file u want to update")
        folder=Path("File-Handling")
        p=folder/name
        if p.exists() and p.is_file():
            print("press 1 for changing the name of file")
            print("press 2 for overwriting the data in the file")
            print("press 3 for appending some content")
            res=int(input("tell ur response"))
        if(res==1):
            name2 =input("enter ur new file name")
            p2=folder/name2
            p.rename(p2)
        if(res==2):
            with open(p,'w') as fs:
                data=input("tell what u wnt to overwrite")
                fs.write(data)
        if(res==3):
            with open(p,'a') as fs:
                data=input("tell what u wnt to append")
                fs.write(data)
    except Exception as err:
        print(f"error as {err}")



def delfile():
    try:
        readfileandfolder()
        name=input("which file u ant todel")
        folder=Path("File-handling")
        p=folder/name
        if p.exists() and p.is_file:
            os.remove(p)
        else:
            print("no such file exists")
    except Exception as err:
        print("error as ",err)
print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")
check=int(input("Please tell ur response"))
if check==1:
    createfile()
if check==2:
    readfile()
if check==3:
    updatefile()
if check==4:
    delfile()