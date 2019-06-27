from tkinter import *
from tkinter import filedialog

window =Tk()

global ImageFile
def mfileopen():
    ImageFile= filedialog.askopenfile()
    #label=Label(text=file1).pack()
    exec(open('final.py').read())
def about_proj():
    contentFile=open('about.txt').read()
    label=Label(window,text=str(contentFile))
    

l1=Label(window, text="Title:")
l1.grid(row=0,column=0)

l1=Label(window, text="About:")
l1.grid(row=1,column=0)

l1=Label(window, text="Interact:")
l1.grid(row=2,column=0)

l1=Label(window, text="Steps:")
l1.grid(row=3,column=0)

l1=Label(window, text="Contact:")
l1.grid(row=7,column=0)

title_text="Brain tumour Detection"
e1=Label(window,text=title_text)
e1.grid(row=0,column=1)

about_text="Brain tumour Detection from mri images"
e2=Label(window,text=about_text)
e2.grid(row=1,column=1)

inter_text="Select an image to detect Tumour"
e3=Label(window,text=inter_text)
e3.grid(row=2,column=1)

steps_text="1.Preprocess\n2.Segmentation\n3.Feature Extractio\n4.Detection"
e4=Label(window,text=steps_text)
e4.grid(row=3,column=1,rowspan=4)

contact_text="abcd@gmail.com"
e5=Label(window,text=contact_text)
e5.grid(row=7,column=1)

button1=Button(window,text="Browse to open file",width=20,command=mfileopen)
button1.grid(row=8,column=0)
button2=Button(window,text="About Project",width=12,command=about_proj)
button2.grid(row=8,column=1)
window.mainloop()
