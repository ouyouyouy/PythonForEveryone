from tkinter import * # import all function inside main package
from tkinter import ttk
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

E1 = ttk.Entry(GUI,font=('Angsana New',20),width=50) # grid , pack ,place
E1.pack()
#E1.place(x=300,y=300)

L2 = ttk.Label(GUI,text='รายละเอียด',font = ('Angsana New',18))
L2.pack()

T1 = Text(GUI,font=('Angsana New',18),height=8,width=56)
T1.pack()


B1 = ttk.Button(GUI,text='บันทึก')
B1.pack(pady=10,ipadx=20,ipady=10)

GUI.mainloop() # mainloop คือ การรันโปรแกรมโดยไม่ปิด คล้ายๆ while True







