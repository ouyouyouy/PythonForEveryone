from tkinter import * # import all function inside main package
from tkinter import ttk
import csv

def writecsv(data):
    # data = ['john',14,500]
    with open ('knowledge.csv','a',newline='',encoding='utf-8') as file:
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

L1 = ttk.Label(GUI,text='หัวข้อความรู้',font = ('Angsana New',18))
L1.pack()

v_title = StringVar()
E1 = ttk.Entry(GUI, textvariable = v_title ,font=('Angsana New',20),width=50) # grid , pack ,place
E1.pack()
#E1.place(x=300,y=300)

L2 = ttk.Label(GUI,text='รายละเอียด',font = ('Angsana New',18))
L2.pack()

T1 = Text(GUI,font=('Angsana New',18),height=8,width=56)
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



B1 = ttk.Button(GUI,text='บันทึก',command=save)
B1.pack(pady=10,ipadx=20,ipady=10)

GUI.mainloop() # mainloop คือ การรันโปรแกรมโดยไม่ปิด คล้ายๆ while True







