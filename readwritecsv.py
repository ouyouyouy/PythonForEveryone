import csv

def writecsv(data):
    # data = ['john',14,500]
    with open ('knowledge.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)

    # ถ้า error
    # ให้สร้าง filename = "C:\\Users\\ouyna\\Desktop\\python for everyone\\knowledge.csv" ใส่ \\ 2ตัว
    # with open (filename,'a',newline='',encoding='utf-8') as file:
def readcsv():
    with open('knowledge.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        data = list(fr)
        print(data)

readcsv()

# d = ['lisa',14,500]
# writecsv(d)




