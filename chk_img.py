import os
import glob
from pathlib import Path

dir = input("Path to dir:")
fn = input("Name of file(will add ext .txt):")
txtl = glob.glob(dir+'/*.txt')
ok = 0
no = 0
nolist = []
with open(fn+".txt", "w") as text_file:
    for pp in txtl:
        imgp = os.path.join(dir,os.path.splitext(pp)[0]+".jpg")
        if(os.path.isfile(imgp)):
            print(imgp +".....Okay")
            ok = ok + 1
            train_path = os.path.join(os.path.basename(Path(dir).parent),os.path.basename(dir),os.path.basename(imgp))
            print("-->" + train_path)
            text_file.write(train_path+"\n")
        else:
            nolist.append(imgp)
            no = no + 1
print("Okay files:" + str(ok),"no files:" + str(no))
for n in nolist:
    print(n)