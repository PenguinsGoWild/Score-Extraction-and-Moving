import pymupdf
import os
from PIL import Image, ImageTk
from mkdict import GenDict
from tkinter import Tk, Label

# to view images
root = Tk()
root.title("Score Viewer")


filename = "reference.pdf"
inputfile = "input2.txt"
extract = "score name"
concert = "concert name"
cwd = os.getcwd()
path = os.path.join(cwd, "scores")

f = open(inputfile)
g = GenDict()

set1 = set() 
for line in f:
    set1.add(line.rstrip())
f.close()

#extract = filename

os.makedirs(path, exist_ok = True)
offset = 1 # skip pages

#foldersdict = g.generate(inputfile) old


doc = pymupdf.open(filename)

instruments = []

acc = 0
for page in doc:
    acc += 1
    instruments.append("")

blank_img = Image.new("RGB", (600, 800), color = "white")
tk_img = ImageTk.PhotoImage(blank_img)
label = Label(root, image = tk_img)
label.pack()
label.image = tk_img
root.update()

for i in range(0, acc, offset):
    test = doc[i].get_text()
    for j in set1:
        if (j in test):
            instruments[i] = j
    while(instruments[i] == ""):
        pix = doc[i].get_pixmap()
        pil_img = pix.pil_image()
        tk_img = ImageTk.PhotoImage(pil_img)

        label.configure(image=tk_img)
        label.image = tk_img
        root.update()
        my = input(f"page {i + 1} instrument cannot be found, manually input:")
        instruments[i] = my
    if offset > 1:
        for y in range(i+1, i + offset):
            if y < acc:
                instruments[y] = instruments[i]
    print(f"pages {i + 1} to {i + offset} " + instruments[i] + " done\n")
doc.close()
root.destroy()

foldersdict = g.generate(instruments)
#print(foldersdict)

#print(instruments)
instrumentset = list(set(instruments))

instruPages = []
'''
for i in range(0, len(instruments), offset):
    nls = []
    nls += list(range(i, i + instruments.count(instruments[i])))
    instruPages.append(nls)
'''

stillHave = len(instrumentset)
a = 0
while(a < stillHave):
    nls = [i for i, x in enumerate(instruments) if x == instrumentset[a]]
    instruPages.append(nls)
    a += 1


print(instruPages)
read = pymupdf.open(f"{extract}.pdf")

for instru in instruPages:
    new_doc = pymupdf.open()
    for pages in instru:
        page = read[pages]
        new_doc.insert_pdf(read, from_page=pages, to_page = pages)
    name = instruments[instru[0]]
    docname = f"{extract} {name}.pdf"
    pathfile = path + f"{foldersdict[name]}\\{concert}\\{extract}"
    os.makedirs(pathfile, exist_ok = True)
    save_path = os.path.join(pathfile, docname)
    new_doc.save(save_path)
    new_doc.close()
read.close()
print(f"created files at {pathfile}")

