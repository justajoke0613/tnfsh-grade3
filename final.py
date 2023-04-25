import json
import requests
import tkinter as tk
from tkinter import ttk
#引入自己製作的json檔
respective_data_112 = 'https://api.jsonbin.io/v3/b/64107d9aebd26539d08e83ab' #112各科成績
total3_data_112 = 'https://api.jsonbin.io/v3/b/6434b486c0e7653a05a1b625' #112三科和(無數B、社)
total4_data_112 = 'https://api.jsonbin.io/v3/b/64109c8bebd26539d08e9449' #112四科和(無數B、社)

#設定8個input欄位，可分別輸入不同項目成績
def submit_grades():
    chinese_grade = input1.get()#國文
    english_grade = input2.get()#英文
    mathA_grade = input3.get()#數學A
    science_grade = input4.get()#自然
    mathB_grade = input5.get()#數學B
    history_grade = input6.get()#社會
    tot3_grade = input7.get()#三科和
    tot4_grade = input8.get()#四科和
    
#設定下拉式選單參數，並以check_num配合資料分析檔案
    if 4<=combo.current()<=9: #判斷為單科
        data = requests.get(respective_data_112).json()
        check_num = 1
    elif 0<=combo.current()<=3: #判斷為三科
        data = requests.get(total3_data_112).json()
        check_num = 3
    elif combo.current() == 10: #判斷為四科
        data = requests.get(total4_data_112).json()
        check_num = 4
        
#選取科目組合並get輸入值 
    if combo.get() == "國文":
        degree = int(input1.get())
    elif combo.get() == "英文":
        degree = int(input2.get())
    elif combo.get() == "數A":
        degree = int(input3.get())
    elif combo.get() == "自然":
        degree = int(input4.get())
    elif combo.get() == "數B":
        degree = int(input5.get())
    elif combo.get() == "社會":
        degree = int(input6.get())
    elif 0<=combo.current()<=3:
        degree = int(input7.get())
    elif combo.current() == 10:
        degree = int(input8.get())

    total_people = 0
    for i in range(15*check_num+1):
        total_people = total_people + int(data['record'][i][combo.get()])#得到總人數
    
    people = int(data['record'][15*check_num-degree][combo.get()])#得到該級分人數

    accumulated_people = 0
    for i in range(15*check_num+1-degree):
        accumulated_people = accumulated_people + int(data['record'][i][combo.get()])#得到累積人數

    accumulated_percentage = 100*accumulated_people/total_people#得到累積百分比

    if degree == 15*check_num:
        PR = 99
        p = 0
    else:
        p = 0
        for i in range(15*check_num-degree):
            p = p + int(data['record'][i][combo.get()])#除自己級分外的累積人數，PR公式用
        PR = int(100*( round((total_people-p)/total_people,4) ))#得到PR

    print('您的PR值是',PR,'，超過了{0}%的玩家'.format(PR),end = '')
    print()
    print('和你相同level的玩家有{0}人'.format(people))
    print('電神有{0}人'.format(p))
    print('店神有{0}人'.format(total_people-accumulated_people))
    print('累積人數百分比{0:.2f}%'.format(accumulated_percentage),end = '，')
    print('累積人數{0}人'.format(accumulated_people))
    if p ==0:
        print("你是最棒的")
    if PR==0:
        print("你是最爛的")

#tkinter部份本次以grid排版
root = tk.Tk() #宣告
root.geometry('530x290') #設定視窗大小
root.title("學測各科級分") #設定title
root.resizable(False, False)#視窗大小設為不可更動
weclabel = tk.Label(root, text='人生deadline', font=('Arial', 25), bg='#8C8CFF')
weclabel.grid(row=0, column=1)

# 建立下拉式選單
combo = ttk.Combobox(root, values=["國英數", "英數自", "國英自", "國數自", "國文", "英文", "數A" , "數B", "自然", "社會" , "國英數自"])
combo.grid(row=0,column=3)

# 建立4個Label和輸入框
label_chinese = tk.Label(root, text="國文級分:")
label_english = tk.Label(root, text="英文級分:")
label_mathA = tk.Label(root, text="數A級分:")
label_science = tk.Label(root, text="自然級分:")
label_mathB = tk.Label(root, text="數B級分:")
label_history = tk.Label(root, text="社會級分:")
label_tot3 = tk.Label(root,text="三科合計" )
label_tot4 = tk.Label(root,text="四科合計")

input1 = tk.Entry(root)
input2 = tk.Entry(root)
input3 = tk.Entry(root)
input4 = tk.Entry(root)
input5 = tk.Entry(root)
input6 = tk.Entry(root)
input7 = tk.Entry(root)
input8 = tk.Entry(root)


# 顯示選項對應的Label和輸入框
def show_entry():
    if combo.get() == "國英數自": 
        label_chinese.grid_forget()
        input1.grid_forget()
        label_english.grid_forget()
        input2.grid_forget()
        label_mathA.grid_forget()
        input3.grid_forget()
        label_science.grid_forget()
        input4.grid_forget()
        label_mathB.grid_forget()
        input5.grid_forget()
        label_history.grid_forget()
        input6.grid_forget()
        label_tot3.grid_forget
        input7.grid_forget
        label_tot4.grid(row=2,column=0)
        input8.grid(row=2,column=1)
    elif combo.get() == "英數自":
        label_chinese.grid_forget()
        input1.grid_forget()
        label_english.grid_forget()
        input2.grid_forget()
        label_mathA.grid_forget()
        input3.grid_forget()
        label_science.grid_forget()
        input4.grid_forget()
        label_mathB.grid_forget()
        input5.grid_forget()
        label_history.grid_forget()
        input6.grid_forget()
        label_tot3.grid(row=2,column=0)
        input7.grid(row=2,column=1)
        label_tot4.grid_forget()
        input8.grid_forget()
    elif combo.get() == "國英自":
        label_chinese.grid_forget()
        input1.grid_forget()
        label_english.grid_forget()
        input2.grid_forget()
        label_mathA.grid_forget()
        input3.grid_forget()
        label_science.grid_forget()
        input4.grid_forget()
        label_mathB.grid_forget()
        input5.grid_forget()
        label_history.grid_forget()
        input6.grid_forget()
        label_tot3.grid(row=2,column=0)
        input7.grid(row=2,column=1)
        label_tot4.grid_forget()
        input8.grid_forget()
    elif combo.get() == "國數自":
        label_chinese.grid_forget()
        input1.grid_forget()
        label_english.grid_forget()
        input2.grid_forget()
        label_mathA.grid_forget()
        input3.grid_forget()
        label_science.grid_forget()
        input4.grid_forget()
        label_mathB.grid_forget()
        input5.grid_forget()
        label_history.grid_forget()
        input6.grid_forget()
        label_tot3.grid(row=2,column=0)
        input7.grid(row=2,column=1)
        label_tot4.grid_forget()
        input8.grid_forget()
    elif combo.get() == "國文":
        label_chinese.grid(row=2,column=0)
        input1.grid(row=2,column=1)
        label_english.grid_forget()
        input2.grid_forget()
        label_mathA.grid_forget()
        input3.grid_forget()
        label_science.grid_forget()
        input4.grid_forget()
        label_mathB.grid_forget()
        input5.grid_forget()
        label_history.grid_forget()
        input6.grid_forget()
        label_tot3.grid_forget()
        input7.grid_forget()
        label_tot4.grid_forget()
        input8.grid_forget()
    elif combo.get() == "英文":
        label_chinese.grid_forget()
        input1.grid_forget()
        label_english.grid(row=2,column=0)
        input2.grid(row=2,column=1)
        label_mathA.grid_forget()
        input3.grid_forget()
        label_science.grid_forget()
        input4.grid_forget()
        label_mathB.grid_forget()
        input5.grid_forget()
        label_history.grid_forget()
        input6.grid_forget()
        label_tot3.grid_forget
        input7.grid_forget
        label_tot4.grid_forget()
        input8.grid_forget()
    elif combo.get() == "數A":
        label_chinese.grid_forget()
        input1.grid_forget()
        label_english.grid_forget()
        input2.grid_forget()
        label_mathA.grid(row=2,column=0)
        input3.grid(row=2,column=1)
        label_science.grid_forget()
        input4.grid_forget()
        label_mathB.grid_forget()
        input5.grid_forget()
        label_history.grid_forget()
        input6.grid_forget()
        label_tot3.grid_forget
        input7.grid_forget
        label_tot4.grid_forget()
        input8.grid_forget()
    elif combo.get() == "數B":
        label_chinese.grid_forget()
        input1.grid_forget()
        label_english.grid_forget()
        input2.grid_forget()
        label_mathA.grid_forget()
        input3.grid_forget()
        label_science.grid_forget()
        input4.grid_forget()
        label_mathB.grid(row=2,column=0)
        input5.grid(row=2,column=1)
        label_history.grid_forget()
        input6.grid_forget()
        label_tot3.grid_forget
        input7.grid_forget
        label_tot4.grid_forget()
        input8.grid_forget()
    elif combo.get() == "自然":
        label_chinese.grid_forget()
        input1.grid_forget()
        label_english.grid_forget()
        input2.grid_forget()
        label_mathA.grid_forget()
        input3.grid_forget()
        label_science.grid(row=2,column=0)
        input4.grid(row=2,column=1)
        label_mathB.grid_forget()
        input5.grid_forget()
        label_history.grid_forget()
        input6.grid_forget()
        label_tot3.grid_forget
        input7.grid_forget
        label_tot4.grid_forget()
        input8.grid_forget()
    elif combo.get() == "社會":
        label_chinese.grid_forget()
        input1.grid_forget()
        label_english.grid_forget()
        input2.grid_forget()
        label_mathA.grid_forget()
        input3.grid_forget()
        label_science.grid_forget()
        input4.grid_forget()
        label_mathB.grid_forget()
        input5.grid_forget()
        label_history.grid(row=2,column=0)
        input6.grid(row=2,column=1)
        label_tot3.grid_forget
        input7.grid_forget
        label_tot4.grid_forget()
        input8.grid_forget()
    elif combo.get() == "國英數":
        label_chinese.grid_forget()
        input1.grid_forget()
        label_english.grid_forget()
        input2.grid_forget()
        label_mathA.grid_forget()
        input3.grid_forget()
        label_science.grid_forget()
        input4.grid_forget()
        label_mathB.grid_forget()
        input5.grid_forget()
        label_history.grid_forget()
        input6.grid_forget()
        label_tot3.grid(row=2,column=0)
        input7.grid(row=2,column=1)
        label_tot4.grid_forget()
        input8.grid_forget()
    
# 建立按鈕以顯示Label和輸入框
button = tk.Button(root, text="顯示成績輸入框", command=show_entry)
button.grid(row=1,column=3)

#製作送出按鈕
submit_button = tk.Button(root, text="提交成績", command=submit_grades)
submit_button.grid(row=7, column=1)

root.mainloop()


'''
#讀取資料
if check_num == 1:
    data = requests.get(respective_data_112).json()
elif check_num == 3:
    data = requests.get(total3_data_112).json()
elif check_num == 4:
    data = requests.get(total4_data_112).json()



if str == "國文":
    degree = int(input1)
elif str == "英文":
    degree = int(input2)
elif str == "數A":
    degree = int(input3)
elif str == "自然":
    degree = int(input4)
elif str == "數B":
    degree = int(input5)
elif str == "社會":
    degree = int(input6)
elif check_num == 3:
    degree = int(input7)
elif check_num == 4:
    degree = int(input8)

total_people = 0
for i in range(15*check_num+1):
  total_people = total_people + int(data['record'][i][str])#得到總人數


people = int(data['record'][15*check_num-degree][str])#得到該級分人數

accumulated_people = 0
for i in range(15*check_num+1-degree):
  accumulated_people = accumulated_people + int(data['record'][i][str])#得到累積人數

accumulated_percentage = 100*round(accumulated_people/total_people,4)#得到累積百分比

if degree == 15*check_num:
  PR = 99
else:
  p = 0
  for i in range(15*check_num-degree):
    p = p + int(data['record'][i][str])#除自己級分外的累積人數，PR公式用
  PR = int(100*( round((total_people-p)/total_people,4) ))#得到PR

#print(degree,people,total_people,accumulated_people,accumulated_percentage,PR) test
print('您的PR值是',PR,'，超過了{0}%的玩家'.format(PR),end = '')
print()
print('和你相同level的玩家有{0}人'.format(people))
print('電神有{0}人'.format(p))
print('店神有{0}人'.format(total_people-accumulated_people))
print('累積人數百分比{0}%'.format(accumulated_percentage),end = '，')
print('累積人數{0}人'.format(accumulated_people))


'''

