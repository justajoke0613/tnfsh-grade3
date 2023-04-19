import tkinter as tk
from tkinter import ttk
#待處理事項：和爬蟲合併，介面美化(
check_num = 0
#用check_num 偵測所選取的科目組合，並配合爬蟲
#利用函式控制讀取成績輸入值
def submit_grades():
    chinese_grade = input1.get()#國文成績
    english_grade = input2.get()#英文成績
    mathA_grade = input3.get()#數A
    science_grade = input4.get()#
    mathB_grade = input5.get()
    history_grade = input6.get()
    tot3_grade = input7.get()#三科和
    tot4_grade = input8.get()#四科和

    print("Chinese Grade:", chinese_grade)
    print("English Grade:", english_grade)
    print("Math Grade:", mathA_grade)
    print("Science Grade:", science_grade)
    print("MathB Grade:", mathB_grade)
    print("History Grade:", history_grade)
    print("tot3_grade:",tot3_grade)
    print("tot4_grade:",tot4_grade)

root = tk.Tk()
root.geometry('530x290') #設定視窗大小
root.title("學測各科級分") #設定title
root.resizable(False, False)#視窗大小設為不可更動
weclabel = tk.Label(root, text='歡迎進行學測落點分析', font=('Arial', 25), bg='#8C8CFF')
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
    global check_num
    if combo.get() == "國英數自": 
        check_num = 4
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
        check_num = 3
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
        check_num = 3
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
        check_num = 3
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
        check_num = 1
        s = "國文"
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
        check_num = 1
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
        check_num = 1
        s = "數A"
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
        check_num = 1
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
        check_num = 1
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
        check_num = 1
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
        check_num = 3
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
