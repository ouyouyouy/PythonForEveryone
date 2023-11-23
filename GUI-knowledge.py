from tkinter import * # import all function inside main package
from tkinter import ttk
import csv
import os

path = os.getcwd() # เมื่อรันคำสั่ง จะมีการแสดง path ที่ file นี้ตั้งอยู่ที่ไหน
print('PATH: ',path)

noteicon = os.path.join(path,'noteicon.ico')

def writecsv(data):
    # data = ['john',14,500]
    csvfile = os.path.join(path,'knowledge.csv') # การเปิดfile ด้วยวิธีนี้จะทำให้ ติด error น้อยกว่าวิธีอื่น ถ้าเรามีการย้าย path
    # ถ้าเรามีการเปิดที่เครื่องอื่น หรือ เปิดด้วย open file อาจจะมี error ได้ การใช้วิธีนี้ทำให้ ไม่มี error
    with open (csvfile,'a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)
#from tkinter import Button , Tk , Entry เราไม่อยากพิมพ์เยอะ จึงใช้ import *
# การ import tkinter เวลาเราเรียกใช้ จะต้องพิมพ์ คำว่า tkinter.Button() , tkinter.Entry() 
# แต่ถ้า ใช้ from tkinter import * เราจะเรียกใช้ Button() , Entry() ได้เลย ง่ายกว่า
# print(dir()) ใน idle เพื่อดูว่าสามารถใช้ function อะไรได้บ้าง ลองพิมพ์ from tkinter import * และ พิมพ์ print(dir())
# อยากรู้ว่าคำสั่งไหนทำงานอย่างไร ให้ใช้คำว่า help() เช่น help(Button) หรือ print(help(Button))พิมพ์ใน idle
GUI = Tk() # โปรแกรม software หลักดึงความสามารถของ Tk มา ส่วนใหญ่จะเรียก root แต่เราใช้ GUI เพื่อให้ง่าย
GUI.title('โปรแกรมบันทึกความรู้ by Loong')
GUI.geometry('500x500')
GUI.iconbitmap(noteicon)

F1 = Frame(GUI)
F1.place(x=20,y=50)

L1 = ttk.Label(F1,text='หัวข้อความรู้',font = ('Angsana New',18))
L1.pack()

v_title = StringVar()
E1 = ttk.Entry(F1, textvariable = v_title ,font=('Angsana New',20),width=50) # grid , pack ,place
E1.pack()
#E1.place(x=300,y=300)

L2 = ttk.Label(F1,text='รายละเอียด',font = ('Angsana New',18))
L2.pack()

T1 = Text(F1,font=('Angsana New',18),height=8,width=56)
T1.pack()

def save():
    title = v_title.get()
    textbox = T1.get(1.0,'end-1c')
    print('------')
    print(title)
    print('------')
    print(textbox)
    print('------')
    # print([textbox]) # การ print โดยใส่ [] เราจะเห็นสิ่งที่ซ่อนอยู่ภายใน
    data = [title,textbox]
    writecsv(data)
    v_title.set('') # clear data after save
    T1.delete('1.0',END) # clear text box



B1 = ttk.Button(F1,text='บันทึก',command=save)
B1.pack(pady=10,ipadx=20,ipady=10)
####################################################################
def readcsv():
    with open('knowledge.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        data = list(fr)
        return data
    
knowledgelist = readcsv()
print(knowledgelist)

global countindex 
countindex = 0
# random.choice จะเป็นการสุ่ม

def Flashcard():
    knowledgelist = readcsv()# เวลาเราเปิด flashcard จะมีการ update ทุกครั้ง
    
    GUI2 = Toplevel()
    GUI2.title('ทบทวนความรู้')
    GUI2.geometry('500x400')

    vtext_title = StringVar()
    vtext_detail = StringVar()
    title = ttk.Label(GUI2,textvariable=vtext_title,font=('Angsana New',20,'bold'))
    title.pack()
    vtext_title.set(knowledgelist[0][0])# จะเขียนใน .setให้โชว์เป็นตัวอักษรอย่างนี้ก็ได้('-------หัวข้อ--------')
    detail = ttk.Label(GUI2,textvariable=vtext_detail,font=('Angsana New',18))
    detail.pack()
    vtext_detail.set(knowledgelist[0][1].replace('\r',''))
    # .replace เป็นการแทนที่ตัวสัญญลักษณ์ \r ที่มีอยู่ในข้อความ ด้วย ''

    def Prev():
        global countindex # ที่ต้อง set ใน function Prev ด้วยเพราะเราต้องการให้ countindex ไปอยู่ด้านนอก function ด้วย
        if countindex == 0:
            countindex = countindex
        else:
            countindex = countindex - 1
        # set text
        print('COUNT: ',countindex)
        vtext_title.set(knowledgelist[countindex][0])
        vtext_detail.set(knowledgelist[countindex][1])

    def Next():
        global countindex # ที่ต้อง set ใน function Prev ด้วยเพราะเราต้องการให้ countindex ไปอยู่ด้านนอก function ด้วย
        if countindex == (len(knowledgelist)-1):
            countindex = len(knowledgelist)-1
        else:
            countindex = countindex + 1
        # set text
        print('COUNT: ',countindex)
        vtext_title.set(knowledgelist[countindex][0])
        vtext_detail.set(knowledgelist[countindex][1])



    BPrev = ttk.Button(GUI2,text = '<',command=Prev)
    BPrev.place(x=170,y=350)
    BNext = ttk.Button(GUI2,text = '>',command=Next)
    BNext.place(x=250,y=350)

    GUI2.mainloop()


notebutton = os.path.join(path,'note.png')
noteicon = PhotoImage(file=notebutton)

BFlashcard = ttk.Button(GUI,image=noteicon,command=Flashcard)
BFlashcard.place(x=440,y=20)

GUI.mainloop() # mainloop คือ การรันโปรแกรมโดยไม่ปิด คล้ายๆ while True







