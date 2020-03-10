import tkinter as tk
import tkinter.scrolledtext
import tkinter.messagebox
from tkinter import ttk
import datetime
import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure


check_x = np.linspace(-10, 10, 100)
pi=PI=3.1415926535898
e=E=2.718281828459


def _print(*args,sep=' ',end='\n'):
    for string in args:
        sc1.insert('end', str(string) + sep)
    sc1.insert('end', end)

class _math(object):
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
        n=0
        a, b = 1, 1
        while n < max:
            yield a
            a, b = b, a + b
            n = n+1

    def tran(self,max):
        n, L = 0, [1]
        while n < max:
            yield L
            L1 = [0] + L[:]
            L = [L1[i + 1] + L1[i] for i in range(len(L))] + [1]
            n = n + 1
math=_math()

class _guiCommand(object):

    def clean(*kw, **arg):
        sc1.delete(1.0, 'end')

    def uptime2(self):
        La2["text"] =str(
            datetime.datetime.now().year) + '已经过去了\n' + str(math.time_percentage() * 100)[:11] + '%'

        root.after(500, self.uptime2)

    def uptime1(self):
        La1["text"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        root.after(1000, self.uptime1)

    def error(self,message):
        tk.messagebox.showerror('错误', message)

    def tips(self,message):
        tk.messagebox.showinfo('提示', message)

    def change(*kw, **arg):
        if co1.get() == '自定义函数':
            La9['text'] ='自定义函数操作说明：\n任意给定一个关于未知数x的函数，本程序将自动生成函数图。\n给定函数后，输入一个x的值，本程序将生成函数f(x)的值\n该操作只支持实数范围内的运算。'
            La5.place(x=160, y=120)
            En2.place(x=270, y=120)
            La6.place_forget()
            sp1.place_forget()
            La7.place_forget()
            sp2.place_forget()
            La11.place_forget()
            sp3.place_forget()
        elif co1.get()=='杨辉三角':
            La9['text'] ='杨辉三角操作说明：\n输入行数m、列数n，点击查询，\n本程序通过运算迅速给出杨辉三角数列中第m行第n列的值。\n该操作中m和n须小于或等于1000。'
            La6.place(x=150, y=120)
            sp1.place(x=218,y=120)
            La11.place(x=300,y=120)
            sp3.place(x=368, y=120)
            La5.place_forget()
            En2.place_forget()
            La7.place_forget()
            sp2.place_forget()
        else:
            La9['text']='斐波那契数列操作说明：\n输入整数n（n≤10000）\n本程序通过运算迅速给出斐波那契数列中第n项的值。'
            sp2.place(x=288,y=120)
            La7.place(x=220, y=120)
            La5.place_forget()
            En2.place_forget()
            La6.place_forget()
            sp1.place_forget()
            La11.place_forget()
            sp3.place_forget()

    def enter(self):
        self.clean()
        if co1.get() == '自定义函数':
            global x, X
            x = X = check_x
            value = En2.get()
            if value=='':
                self.error('请输入函数')
                return
            text = u'，！{}【】（）“”‘’＋－×÷'
            base = u',!()()()""\'\'+-*/'
            table = {ord(f): ord(t) for f, t in zip(text, base)}
            value = value.translate(table)
            value = value.replace('^', '**')
            value = value.replace('π', 'pi')
            try:
                eval(value)*1.0
            except:
                self.error('出错了，原因是：“出现无效字符”')
                En2['text'] = ''
            else:
                y = eval(value)*check_x/check_x
                del x
                self.show(y)
        elif co1.get()=='杨辉三角':
            if sp1.get()=='' or sp3.get()=='':
                self.error('请输入行数或列数')
                return
            value1 = int(sp1.get())
            value2 = int(sp3.get())
            if value1>1000 or value2>1000:
                self.error('你输入的值过大')
            elif value2>=value1:
                self.error('第'+str(value1)+'行没有第'+str(value2)+'项')
            else:
                i=0
                for num_line in math.tran(value1):
                    i+=1
                    if i==0:
                        self.clean()
                    _print('第'+str(i)+'行'+str(num_line),end='\n\n')
                self.tips('综上所述，第'+str(value1)+'行第'+str(value2)+'列的值是'+str(num_line[value2-1]))
        else:
            if sp2.get()=='':
                self.error('请输入第几个')
                return
            value = int(sp2.get())
            if value>10000:
                self.error('你输入的值过大')
            elif value<1:
                self.error('斐波那契中不存在第'+value+'项')
            else:
                i = 0
                for num_line in math.feibo(value):
                    i+=1
                    _print('第' + str(i) + '个' + str(num_line),end='\n\n')
                self.tips('综上所述，斐波那契中第' + str(i) + '个数的值是' + str(num_line))

    def ckeck(self):
        value=En3.get()
        if value == '':
            self.error('请输入函数')
            return
        text = u'，！{}【】（）“”‘’＋－×÷'
        base = u',!()()()""\'\'+-*/'
        table = {ord(f): ord(t) for f, t in zip(text, base)}
        value = value.translate(table)
        value = value.replace('^', '**')
        value = value.replace('π', 'pi')
        try:
            eval(value)
        except:
            tk.messagebox.showerror('错误', '出错了，原因是：“出现无效字符”')
            En3['text'] = ''
        else:
            x=eval(value)
            y = eval(En2.get())
            self.tips('x为'+str(En3.get())+'时，f(x)值为:'+str(y))

    def show(self,y):
        global draw,En3
        draw = tk.Tk()
        draw.title("查询")
        draw.geometry('500x515+100+100')
        draw.configure(background='white')
        La10 = tk.Label(draw, text='x=?',bg='white')
        La10.place(x=30, y=20)
        La11=tk.Label(draw, text='已知f(x)='+En2.get(),bg='white')
        La11.place(x=30, y=0)
        En3 = tk.Entry(draw, width=12)
        En3.place(x=80, y=20)
        bu2 = ttk.Button(draw, text='确定', command=self.ckeck)
        bu2.place(x=50, y=70)
        fig = Figure(figsize=(5, 4), dpi=100)
        fig.add_subplot(111).plot(check_x,y)
        canvas = FigureCanvasTkAgg(fig, master=draw)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place()
        toolbar = NavigationToolbar2Tk(canvas, draw)
        toolbar.update()
        canvas.get_tk_widget().place(x=0,y=98)
        tk.mainloop()
Gui=_guiCommand()


if __name__ == '__main__':

    # ====================基本设置====================
    root = tk.Tk()
    root.geometry('600x540')
    root.title('数学小工具  ————©版权所有 渐淡')
    # ====================基本设置====================

    La1 = tk.Label(root, text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    La2 = tk.Label(root, text='')
    La3 = tk.Label(root, text='求任何数组')
    La4=tk.Label(root, text='')
    #list=('自定义数组','自定义函数','杨辉三角','斐波那契数列')
    list = ('自定义函数', '杨辉三角', '斐波那契数列')
    co1= ttk.Combobox(root, width=12, textvariable=1, state='readonly',values=list)
    co1.bind('<<ComboboxSelected>>',Gui.change)
    co1.current(0)

    sc1 = tk.scrolledtext.ScrolledText(root, width=82, height=25)
    bu1 = ttk.Button(root, text='查询',width=84,command=Gui.enter)

    #====================in change()====================

    La5 = tk.Label(root, text='请输入函数      f(x)=')
    La6 = tk.Label(root, text='请输入行数')
    La7 = tk.Label(root, text='请输入个数')
    La8 = tk.Label(root, text='请输入数组，用“,”分割')
    La9 = tk.Label(root,fg='blue')
    La11=tk.Label(root,text='请输入列数')
    En1 = tk.Entry(root, width=18)
    En2 = tk.Entry(root, width=18)


    sp1 = tk.Spinbox(root, width=6,from_=1, to=10000, increment=1)
    sp2 = tk.Spinbox(root, width=5, from_=1, to=10000, increment=1)
    sp3 = tk.Spinbox(root, width=5, from_=1, to=10000, increment=1)

    La9.place(x=140,y=40)
    Gui.change()
    #====================in change()====================



    La1.place(x=0,y=0)
    La2.place(x=15,y=16)
    La3.place(x=197, y=17)
    co1.place(x=260,y=17)
    La4.place(x=220, y=0)
    bu1.place(x=0,y=155)
    sc1.place(x=0, y=180)

    # ====================死循环====================
    root.after(500,Gui.uptime2)
    root.after(1000,Gui.uptime1)
    root.mainloop()

    # ====================死循环====================