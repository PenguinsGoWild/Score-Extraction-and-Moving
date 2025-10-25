import pymupdf
import os
from PIL import Image, ImageTk
from mkdict import GenDict
from tkinter import Tk, Label

# to view images
root = Tk()
root.title("Score Viewer")

extract = "filename here"
if (os.path.exists("reference.pdf")):
    filename = "reference.pdf"
else:
    filename = extract + ".pdf"
inputfile = "input2.txt"
concert = "concert name"
cwd = os.getcwd()
path = os.path.join(cwd, "scores\\")

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

blank_img = Image.new("RGB", (800, 600), color = "white")
tk_img = ImageTk.PhotoImage(blank_img)

label = Label(root, image = tk_img)
label.pack()
label.image = tk_img
root.geometry(f"{800}x{600}")
#root.resizable(False, False)
root.update()
scaling_factor = 0.8
window_width = root.winfo_width()
window_height = root.winfo_height()

mem = extract + "_name_storage.txt"
mem_path = os.path.join(cwd, "memory")
os.makedirs(mem_path, exist_ok = True)
mem_path = os.path.join(cwd, "memory", mem)
#mem_path = mem_path + mem
try:
    with open(mem_path, "x") as f:
        print(f"no memory exists, creating new one")
except FileExistsError: 
    print(f"memory exists, not creating new one")


with open(mem_path, "r+") as memo:
    for i in range(0, acc, offset):
        test = doc[i].get_text()
        line = memo.readline()
        if (line):
            print(f"using {line.strip()} from memory")
            instruments[i] = line.strip()
        else:
            for j in set1:
                if (j in test and j != ""):
                    instruments[i] = j
                    memo.write(j + "\n")
                    print(f"wrote {j} to memory successfully")
            while(instruments[i] == ""):
                pix = doc[i].get_pixmap(matrix = pymupdf.Matrix(scaling_factor, scaling_factor))
                pil_img = pix.pil_image()

                # Resize image
                resized_img = pil_img.resize((window_height, window_width), Image.Resampling.LANCZOS)

                # Convert the resized image to a format Tkinter can use
                tk_img = ImageTk.PhotoImage(resized_img)

                # Center the image in the window
                label.place(relx=0.5, rely=0.5, anchor="center")

                label.configure(image=tk_img)
                label.image = tk_img
                #root.geometry(f"{pil_img.width}x{pil_img.height}")
                root.geometry(f"{600}x{800}")
                root.update_idletasks()
                my = input(f"page {i + 1} instrument cannot be found, manually input:")
                if (my != ""):
                    memo.write(my + "\n")
                    print(f"wrote {my} to memory successfully")
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

