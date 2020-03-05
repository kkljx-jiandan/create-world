import tkinter as tk
import tkinter.scrolledtext
import tkinter.messagebox
from tkinter import ttk
import time
import re
import datetime
import sympy

def _print(text='',end='\n'):
    sc1.insert('end', str(text)+end)

class _math(object):
    def trou_formula(self,value_list):
        can_list = []  # 参数
        temp = []
        max=len(value_list)
        _print(type(value_list))
        for num in range(1, max + 1):
            can_list.append([num ** x for x in range(1, max + 1)])
        a = sympy.Matrix(can_list)
        b = sympy.Matrix(value_list)
        x = sympy.symarray('x', (max, 1))
        dict = sympy.solve(a * x - b)
        # return dict
        for items in dict.items():
            temp.append(items[1])
        n = sympy.Symbol('n')
        value = 0
        temp_len = len(temp)
        for i in range(0, temp_len):
            letter = sympy.simplify(temp[i] * n ** (temp_len - i - 1))
            value += letter
        return value

    def time_percentage(self):
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        second = datetime.datetime.now().second
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            f_days = 29
        else:
            f_days = 28
        # f_days = February_days
        month_day = [0, 31, 31 + f_days, 62 + f_days, 92 + f_days, 123 + f_days, 153 + f_days, 184 + f_days,215 + f_days, 245 + f_days, 276 + f_days, 306 + f_days]
        all_day = month_day[month - 1] + day
        all_hour = (all_day - 1) * 24 + hour
        all_minute = all_hour * 60 + minute
        all_second = all_minute * 60 + second
        days_percentage = all_second / (337 + f_days) / 24 / 60 / 60
        return days_percentage

    def feibo(self,max):
        n, a, b = 0, 0, 1
        while n <= max:
            yield a
            a, b = b, a + b
            n += 1

    def tran(self,max):
        n, L = 1, [1]
        while n <= max:
            yield L
            L1 = [0] + L[:]
            L = [L1[i + 1] + L1[i] for i in range(len(L))] + [1]
            n = n + 1
math=_math()

class _guiCommand(object):
    def uptime2(self):
        now = 0

        La2["text"] =str(
            datetime.datetime.now().year) + '已经过去了\n' + str(math.time_percentage() * 100)[:11] + '%'

        root.after(500, self.uptime2)

    def uptime1(self):
        now = 0

        La1["text"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        root.after(1000, self.uptime1)

    def error(self,message):
        tk.messagebox.showerror('错误', message)

    def change(*kw, **arg):
        ck1.place(x=370, y=100)
        if co1.get()=='自定义数组':
            La5.place(x=80,y=100)
            En1.place(x=205,y=100)
            La6.place_forget()
            En2.place_forget()
            La7.place_forget()
            sp1.place_forget()
            La8.place_forget()
        elif co1.get() == '自定义函数':
            La6.place(x=80, y=100)
            En2.place(x=190, y=100)
            La5.place_forget()
            En1.place_forget()
            La7.place_forget()
            sp1.place_forget()
            La8.place_forget()
        elif co1.get()=='杨辉三角':
            La7.place(x=200, y=100)
            sp1.place(x=268,y=100)
            La5.place_forget()
            En1.place_forget()
            La6.place_forget()
            En2.place_forget()
            La8.place_forget()
            return 2
        else:
            La8.place(x=180,y=100)
            La6.place_forget()
            En2.place_forget()
            La7.place_forget()
            sp1.place_forget()
            La5.place_forget()
            En1.place_forget()
            return 3

    def enter(self):
        if co1.get()=='自定义数组':
            value=En1.get()
            _print(value)
            _print('[正在加载数据]')
            pattern=r'([a-zA-Z\u4e00-\u9fa5])'
            match=re.match(pattern,value)
            if value=='':
                self.error('请输入数组')
            elif match!=None:
                self.error('不能带有其他字符')
            else:
                value_list=[]
                value_tuple=value.split(',')
                _print(value_tuple)
                for num in value_tuple:
                    if num!='':
                        _print(num)
                        value_list.append(int(num))

                _print('\n')
                time1=time.time()
                sc1.insert('end', math.trou_formula(value_list))
                time2 = time.time()

                sc1.insert('end', '[耗时'+str(time2-time1)+'秒]')
                if ck1_value.get()==1:
                        pass
        elif co1.get() == '自定义函数':
            value = En2.get()
            if value=='':
                self.error('请输入函数')
            else:
                if ck1_value.get() == 1:
                    pass
        elif co1.get()=='杨辉三角':
            if ck1_value.get() == 1:
                pass
        else:
            if ck1_value.get() == 1:
                pass
Gui=_guiCommand()

if __name__ == '__main__':
    # ====================基本设置====================
    root = tk.Tk()
    root.geometry('540x400')
    root.minsize(540, 400)
    root.maxsize(540, 400)
    root.title('数学小工具  ————©版权所有 渐淡')
    # ====================基本设置====================

    La1 = tk.Label(root, text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    La2 = tk.Label(root, text='')
    La3 = tk.Label(root, text='求任何数组通项公式')
    La4=tk.Label(root, text='')
    list=('自定义数组','自定义函数','杨辉三角','斐波那契数列')
    co1= ttk.Combobox(root, width=12, textvariable=1, state='readonly',values=list)
    co1.bind('<<ComboboxSelected>>',Gui.change)
    co1.current(0)

    sc1 = tk.scrolledtext.ScrolledText(root, width=70, height=16)
    bu1 = ttk.Button(root, text='开始计算',width=70,command=Gui.enter)

    #====================in change()====================
    ck1_value=tk.StringVar(value="0")
    ck1 = ttk.Checkbutton(root, text='绘制函数图', onvalue=1, offvalue=0, variable=ck1_value)

    La5 = tk.Label(root, text='请输入数组，用“,”分割')
    La6 = tk.Label(root, text='请输入函数      f(x)=')
    La7 = tk.Label(root, text='请输入行数')
    La8 = tk.Label(root, text='斐波那契数列公式，点击开始')
    En1 = tk.Entry(root, width=18)
    En2 = tk.Entry(root, width=18)
    sp1 = tk.Spinbox(root, width=4, from_=1, to=1000, increment=1)
    #====================in change()====================

    La1.place(x=210,y=0)
    La2.place(x=225,y=16)
    La3.place(x=150, y=66)
    co1.place(x=260,y=66)
    La4.place(x=220, y=50)
    sc1.place(x=10, y=160)
    bu1.place(x=10,y=135)

    # ====================死循环====================
    root.after(500,Gui.uptime2)
    root.after(500,Gui.uptime1)
    root.mainloop()
    # ====================死循环====================