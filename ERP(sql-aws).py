#user Brain Shi
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import *
from tkcalendar import Calendar
import matplotlib.pyplot as plt         # 匯入 matplotlib 的 pyplot 類別,並設定為 plt
# //注意這裡用的不是'SimHei'
import pymysql as MySQLdb                #  pip install MySQLdb    # MySQL
# import pymssql as MySQLdb                #  pip install pymssql    # MS-SQL

import sys
from PIL import Image, ImageTk

if sys.platform.startswith("linux"):  # could be "linux", "linux2", "linux3", ...
    print("linux")  # linux
elif sys.platform == "darwin":  # MAC OS X
    from matplotlib.font_manager import FontProperties      # 中文字體
    plt.rcParams['font.sans-serif'] = 'Arial Unicode MS'
    plt.rcParams['axes.unicode_minus'] = False
    fonchartX= ("Helvetica", 12)
elif sys.platform == "win32":
    # Windows (either 32-bit or 64-bit)
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 換成中文的字體
    plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）
    fonchartX= ("Helvetica", 12)

def createNewWindow():       # 建立新視窗 日曆
    global newWindow
    newWindow = Toplevel(win)
    cal = Calendar(newWindow, selectmode='day',date_pattern="y-mm-dd")

    cal.pack(pady=5)
    def grad_date():
        global newWindow
        date.config(text=cal.get_date())
        labelDateRes['text'] = cal.get_date()



        newWindow.destroy()



    date = Label(newWindow, text="")
    date.pack(pady=5)
    # Add Button and Label
    Button(newWindow, text="date choose",
           command=grad_date).pack(pady=5)
class product(object):  # 繼承Python 最上層的object 類別
    def __init__(self,ID,Date,Name,Years,Weight,Exhaust,Engine,Variable,Color,Amount,Store,Salese,Price,Check): # 類別初始化的函數 initialize 一開始要做的函數
       self.productID=ID
       self.productDate = Date
       self.productName  = Name
       self.productYears = Years
       self.productWeight =Weight
       self.productExhaust=Exhaust
       self.productEngine=Engine
       self.productVariable=Variable
       self.productColor=Color
       self.productAmount=Amount
       self.productStore=Store
       self.productSalese=Salese
       self.productPrice=Price
       self.productCheck=Check

    def info(self):
        lischartX = [self.productID,self.productDate,self.productName, self.productYears, self.productWeight, self.productExhaust, self.productEngine
            , self.productVariable, self.productColor, self.productAmount, self.productStore,self.productSalese,self.productPrice,self.productCheck]
        return lischartX
    def productColumn(self):
        lischartX = ["ID","訂單日期","車款名稱","年份","重量","排氣量","引擎規格","變速規格","顏色","數量","車行門市","銷售人員","銷售價格","核對結果"]
        return lischartX


products = []
db = MySQLdb.connect(host="127.0.0.1",   #  連接到本身的電腦IP
                     user="admin",       #  MySQL/PHPMyAdmin 新增的 用戶
                     passwd="admin",
                     db="mydatabase")    #  MySQL/PHPMyAdmin 新增的 資料庫

cursor = db.cursor()



sql="SELECT * FROM `erptable`"
cursor.execute(sql)          # 執行新增資料
db.commit()                  # 送出
lischartX= cursor.fetchall()     # 將資料轉換成陣列
for row in lischartX:
     producchartX =product(ID=row[0],Date=row[1],Name=row[2],Years=row[3],Weight=row[4],Exhaust=row[5],Engine=row[6],Variable=row[7],Color=row[8],Amount=row[9],Store=row[10],Salese=row[11],Price=row[12],Check=row[13])
     products.append(producchartX)


# 視窗設定
win = tk.Tk()
win.wm_title("ERP訂單系統")
win.resizable(width=True, height=True) # 步驟4：設定主視窗可以被調整大小
win.minsize(width=800 , height=600)    #  最小尺寸
win.maxsize(width=1600, height=800)      #  最大尺寸
dateRes=""
newProduct=()
chartX=[]
chartY=[]
def addData():#新增
    global newProduct
    global t1
    global t2
    # id自動為最後一筆加1
    for n in tree.get_children():
        idmax = int(tree.item(n)["values"][0])
        plusID = idmax + 1
    newProduct=product(plusID,labelDateRes["text"],entryNameString.get(),entryYearString.get(),entryWeightString.get(),entryExhaustString.get(),entryEngineString.get(),entryVariableString.get(),
                       comboboxValueColor.get(),entryAmountString.get(),comboboxValueStore.get(), entrySaleseString.get(),
                       entryPriceString.get(), radioValue2.get())

    tree.insert('', tk.END, values=newProduct.info())
    #連接SQL 新增
    sql = "INSERT INTO `erptable`(`id`, `訂單日期`, `車款名稱`, `年份`, `重量`, `排氣量`, `引擎規格`, `變速規格`, `顏色`, `數量`, `車行門市`, `銷售人員`, `銷售價格`, `核對結果`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (plusID,labelDateRes["text"],entryNameString.get(),entryYearString.get(),entryWeightString.get(),entryExhaustString.get()
           ,entryEngineString.get(),entryVariableString.get(),comboboxValueColor.get(),entryAmountString.get(),comboboxValueStore.get()
           , entrySaleseString.get(),entryPriceString.get(), radioValue2.get())
    cursor.execute(sql, val)
    db.commit()
def changeData():#修改
    # 參考資料 https://pythonguides.com/python-tkinter-treeview/
    global changeProduct
    global temp
    changeProduct = product(entryIDString.get(),labelDateRes["text"],entryNameString.get(),entryYearString.get(),entryWeightString.get(),entryExhaustString.get(),entryEngineString.get(),entryVariableString.get(),
                       comboboxValueColor.get(),entryAmountString.get(),comboboxValueStore.get(), entrySaleseString.get(),
                       entryPriceString.get(), radioValue2.get())

    selected = tree.focus()    # .focus()在 Treeview 中保存所選項目的行號，並將其值存儲在名為 selected 的變量中
    temp = tree.item(selected, "values")    # .item()接受 2 個參數，selected和"values"。這意味著從選定的行中顯示所有值。這些值將以元組格式顯示。這存儲在名為temp的變量中
    tree.item(selected, values=changeProduct.info())
    #連接SQL 修改
    sql="UPDATE `erptable` SET `id`=%s,`訂單日期`=%s,`車款名稱`=%s,`年份`=%s,`重量`=%s,`排氣量`=%s,`引擎規格`=%s,`變速規格`=%s,`顏色`=%s,`數量`=%s,`車行門市`=%s,`銷售人員`=%s,`銷售價格`=%s,`核對結果`=%s WHERE `id`=%s"
    val = (entryIDString.get(), labelDateRes["text"], entryNameString.get(), entryYearString.get(), entryWeightString.get(),
           entryExhaustString.get(), entryEngineString.get(), entryVariableString.get(), comboboxValueColor.get(), entryAmountString.get(),
           comboboxValueStore.get() , entrySaleseString.get(), entryPriceString.get(), radioValue2.get(),entryIDString.get())
    cursor.execute(sql, val)
    db.commit()
def delectData():#刪除
    for selected_item in tree.selection():
        tree.delete(selected_item)
    #連結SQL刪除
    sql = "DELETE FROM `erptable` where `id`= %s"
    val = (entryIDString.get())
    cursor.execute(sql, val)
    db.commit()
#label
labelID =tk.Label(win,text="ID").place(x=300,y=0)
labelDate = tk.Label(win, text="訂單日期日期：", font=fonchartX)
labelDate.place(x=0, y=5)
checkButton = Button(win, text="🗓️", command=createNewWindow, fg="white", font=fonchartX)
checkButton.place(x=80, y=0)
labelDateRes = Label(win, text="", bd=0, font=fonchartX)
labelDateRes.place(x=120, y=10)
labelName =tk.Label(win,text="車輛名稱").place(x=0,y=40)
labelYear =tk.Label(win,text="車輛年份").place(x=0,y=80)
labelweight =tk.Label(win,text="車輛重量").place(x=0,y=120)
labelExhaust =tk.Label(win,text="車輛排氣量").place(x=0,y=160)
labelEngine =tk.Label(win,text="引擎規格").place(x=0,y=200)
labelcolor =tk.Label(win,text="顏色").place(x=300,y=40)
labelVariable =tk.Label(win,text="變速規格").place(x=0,y=240)
labelStore =tk.Label(win,text="銷售門市").place(x=300,y=80)
labelSalese =tk.Label(win,text="銷售人員").place(x=300,y=160)
labelAmount=tk.Label(win,text="數量").place(x=300,y=120)
labelPrice =tk.Label(win,text="價格").place(x=300,y=200)

#entry
entryIDString = tk.StringVar()
entryIDString.set("")
entryName = tk.Entry(win, textvariable=entryIDString, width=12).place(x=360,y=0)
entryNameString = tk.StringVar()
entryNameString.set("")
entryName = tk.Entry(win, textvariable=entryNameString, width=12).place(x=80,y=40)

entryYearString = tk.StringVar()
entryYearString.set("")
entryNum = tk.Entry(win, textvariable=entryYearString, width=12).place(x=80,y=80)
entryWeightString = tk.StringVar()
entryWeightString.set("")
entryweight = tk.Entry(win, textvariable=entryWeightString, width=12).place(x=80,y=120)

entryExhaustString = tk.StringVar()
entryExhaustString.set("")
entryExhaust = tk.Entry(win, textvariable=entryExhaustString, width=12).place(x=80,y=160)

entryEngineString = tk.StringVar()
entryEngineString.set("")
entryEngine = tk.Entry(win, textvariable=entryEngineString, width=12).place(x=80,y=200)

entryVariableString = tk.StringVar()
entryVariableString.set("")
entryVariable = tk.Entry(win, textvariable=entryVariableString, width=12).place(x=80,y=240)

entryAmountString = tk.StringVar()
entryAmountString.set("")
entryAmount = tk.Entry(win, textvariable=entryAmountString, width=12).place(x=360,y=120)

entrySaleseString = tk.StringVar()
entrySaleseString.set("")
entrSalese = tk.Entry(win, textvariable=entrySaleseString, width=12).place(x=360,y=160)

entryPriceString = tk.StringVar()
entryPriceString.set("")
entryPrice = tk.Entry(win, textvariable=entryPriceString, width=12).place(x=360,y=200)
#建立下拉式選單
def on_field_change(index, value, op):
    print("combobox updated to ",comboboxValueColor.get(),comboboxValueStore.get())
comboboxValueColor = tk.StringVar()
comboboxValueColor.trace('w', on_field_change)              # 注意：當資料不同時，就會呼叫 on_field_change
color = ttk.Combobox(win, width=10, textvariable=comboboxValueColor)
color['values'] = ('競技藍', '深黑色', '白色', '紅色')
color.place(x=360, y=40)                                           # 放置位置

comboboxValueStore = tk.StringVar()
comboboxValueStore.trace('w', on_field_change)              # 注意：當資料不同時，就會呼叫 on_field_change
productionUnit = ttk.Combobox(win, width=10, textvariable=comboboxValueStore)
productionUnit['values'] = ('桃園中正門市', '桃園中壢門市', '桃園青埔門市')
productionUnit.place(x=360, y=80)                                  # 放置位置

#建立核對結果
labelCheck =tk.Label(win,text="核對結果").place(x=300,y=240)
def evenchartX():
   global radioValue2
   print(radioValue2.get())
# 多選一的元件 Radiobutton
radioValue2 = tk.StringVar()                               # 元件的變數 String
radioValue2.set(True)
tk.Radiobutton(win, text='審核完成',variable=radioValue2, value='審核完成').place(x=360,y=240)
tk.Radiobutton(win, text='待審核',variable=radioValue2, value='待審核').place(x=450,y=240)


# btn
btn1=tk.Button(win,text="新增產品",command=addData).place(x=540,y=100)
btn2=tk.Button(win,text="修改產品",command=changeData).place(x=620,y=100)
btn3=tk.Button(win,text="刪除產品",command=delectData).place(x=700,y=100)

# tree
columns = producchartX.productColumn()       # 欄位名稱
tree = ttk.Treeview(win,columns=columns, show="headings")
tree.place(x=25,y=350,width=1300)

for i in columns:
    tree.heading(i, text=i)             # 欄位文字設定
    tree.column(i, minwidth=0, width=60)

for i in products:
    lischartX=i.info()
    tree.insert("", tk.END, values=lischartX)      # 插入資料
#tree def
def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        entryIDString.set(record[0])
        labelDateRes["text"] = record[1]
        entryNameString.set(record[2])
        entryYearString.set(record[3])
        entryWeightString.set(record[4])
        entryExhaustString.set(record[5])
        entryEngineString.set(record[6])
        entryVariableString.set(record[7])
        comboboxValueColor.set(record[8])
        entryAmountString.set(record[9])
        comboboxValueStore.set(record[10])
        entrySaleseString.set(record[11])
        entryPriceString.set(record[12])
        radioValue2.set(record[13])

#建立圖表
label1 =tk.Label(win)             # 建立Label物件 顯示圖片
label1.pack()
def open_ImageFile_file():
    #global chartX
    #global chartY
    global tree
    dict1={}
    for selected_item in tree.get_children():  # 取得所有的資料
        item = tree.item(selected_item)
        #record = item['values']
        #print(record)
        #chartX.append(item['values'][1])#取得日期
        #chartY.append(item['values'][9])#取得數量
        # key is in dict1
        if item['values'][1] in dict1:
            dict1[item['values'][1]]=dict1[item['values'][1]]+item['values'][9]
        else:
            dict1[item['values'][1]] =1

    sortednames = sorted(dict1.keys(), key=lambda x: x.lower()) # 依照日期排列

    # dict1 convert to Array
    chartX=[]
    chartY=[]
    for key in sortednames:
        chartX.append(key)
        chartY.append(dict1[key])

    plt.plot(chartX, chartY, 'bo-')      # 繪製藍色直槓
    plt.legend(loc='lower left')  # 在左下角顯示標籤
    plt.title('每日銷售量')
    plt.savefig("每日銷售量.jpg")  # 儲存圖片
    plt.show()                  # 顯示"""

    fileName = "每日銷售量.jpg"  # 取得用戶的選取檔案
    x =Image.open(fileName)  # 讀取圖片
    x = x.resize((200, 200))  # 改變圖片大小
    img = ImageTk.PhotoImage(x)  # 轉換成PhotoImage
    label1.configure(image=img)
    label1.image = img
    x.close()  # 關閉圖片

# Create a button
Button(win, text="查看每日銷售量報表", command=lambda: open_ImageFile_file(),).place(x=600, y=200)

tree.bind('<<TreeviewSelect>>', item_selected) # 綁定事件 選取時



win.mainloop()