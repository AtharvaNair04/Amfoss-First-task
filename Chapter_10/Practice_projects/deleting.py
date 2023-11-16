import pathlib as Path
import os
for folderName,subfolders,filenames in os.walk('/home/atharva'):
    for filename in filenames:
        path=os.path.join(folderName,filename)
        size=os.path.getsize(path)
        og_size=size/(1024*1024)
        if og_size>=100:
            print(path,':',og_size)
        else:
            continue
