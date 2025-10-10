import os
import shutil
from mkdict import GenDict

inputfile = "names.txt"
extract = "name here"
concert = "concert here"
cwd = os.getcwd()
path = os.path.join(cwd, "scores\\")
files = os.path.join(cwd, "unsorted")

f = open(inputfile)
g = GenDict()

dir_list = os.listdir(files)

#print(dir_list)

set1 = set() 
for line in f:
    set1.add(line.rstrip())
f.close()
    
#os.makedirs(path, exist_ok = True)
foldersdict = g.generate(dir_list)
#print(foldersdict)

for part in dir_list:
    docname = f"{extract} {part}.pdf"
    pathfile = path + f"{foldersdict[part]}\\{concert}\\{extract}"
    os.makedirs(pathfile, exist_ok = True)
    shutil.move(f"{files}\\{part}", f"{pathfile}\\{part}")
    print(f"moved {part}")

print("done")
    


