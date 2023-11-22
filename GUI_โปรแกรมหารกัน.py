from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.title('โปรแกรมหารกัน')
GUI.geometry('700x500')

L = Label(GUI,text=('โปรแกรมหารกัน'),font=('Angsana New',30))
L.pack(pady = 20)
########################################################
L = ttk.Label(GUI,text=('ราคาอาหาร'),font=('Angsana New',30))
L.pack(pady=5)

v_total = StringVar()
E1 = ttk.Entry(GUI,textvariable=v_total,font=('Angsana New',20))
E1.pack(pady=10)
########################################################
L = Label(GUI,text='มากันกี่คน',font=('Angsana New',20))
L.pack()

v_person = StringVar()
E2 = ttk.Entry(GUI,textvariable=v_person,font=('Angsana New',20))
E2.pack(pady=10)
###########################################################
def Calculate():
    total = float(v_total.get())
    person = int(v_person.get())
    calc = total / person
    print('Splite (bath/person): ',calc)
    text = 'รวมทั้งหมด {:,.2f} บาท จำนวน {} ({:.2f}บาทต่อคน)'.format(total,person,calc)
    v_result.set(text)

B1 = ttk.Button(GUI,text='Calculator',command=Calculate)
B1.pack(pady=10,ipadx=20,ipady=10)

v_result = StringVar()
result = ttk.Label(GUI,textvariable=v_result,font=('Angsana New',25,'bold'),foreground='green')
result.pack(pady=20)



GUI.mainloop()