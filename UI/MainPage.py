from tkinter import *
from tkinter import ttk
import tkinter.messagebox

from Caculate_Model.Condition import Condition
from Caculate_Model.calculate_OptimalPath import Calculate
from Map_Model.constant import Mode


class MainPage:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry('900x550+500+240')
        OriginFrame(self.root).pack()

        
class OriginFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master

        self.condition=None

        self.path_walk=None
        self.path_cycle=None
        self.path_drive=None

        self.hourVar=StringVar()
        self.minVar=StringVar()
        self.weatherVar=StringVar()
        self.temperatureVar=StringVar()
        self.sartingVar=StringVar()
        self.endingVar=StringVar()

        self.have_init=False

        self.creatPage()

    def creatPage(self):
        row = 0
        Label(self).grid(row=row)

        row += 1
        Label(self, text="最优路径规划",
              font=('宋体', 20, 'bold'))\
            .grid(row=row, column=0, columnspan=4)

        row += 1
        ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(self, text="条件选择", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=E, padx=35)

        row += 1
        Label(self, text="天气", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=E, padx=35)
        Entry(self, textvariable=self.weatherVar,state='readonly').grid(row=row, column=1, padx=10)

        row+=1
        Label(self, text="气温", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=E, padx=35, column=0)
        Entry(self, textvariable=self.temperatureVar,state='readonly').grid(row=row, column=1, padx=10)

        row += 1
        Label(self, text="当前时间", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=E, padx=35)

        TimeFrame=Frame(self)
        TimeFrame.grid(row=row,column=1, columnspan=4, padx=10,sticky=W)
        Entry(TimeFrame, textvariable=self.hourVar,width=10,state='readonly').grid(
            row=1, ipadx=30, padx=10, pady=10,column=1)
        Label(TimeFrame, text=" : ", font=('宋体', 13, 'bold')).grid(
            row=1, sticky=E, padx=5,column=2)
        Entry(TimeFrame, textvariable=self.minVar,width=10,state='readonly').grid(
            row=1, ipadx=30, padx=10, pady=10, column=3)


        row += 1
        Label(self, text="起点", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=E, padx=35)
        Entry(self, textvariable=self.sartingVar,state='readonly').grid(row=row, column=1, padx=10)

        Label(self, text="终点", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=E, padx=35,column=2)
        Entry(self, textvariable=self.endingVar,state='readonly').grid(row=row, column=3, padx=10)


        row += 1
        Label(self, text="搜索结果", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=E, padx=35)
        self.ansList=Listbox(self,width=50)
        self.ansList.grid(
            row=row, ipadx=80, padx=10, pady=10, columnspan=6,column=1)

        row += 1
        ttk.Button(self, text="随机生成条件", command=self.__init, style='primary.TButton').grid(
            row=row, column=1, padx=10, pady=10, sticky=EW)

        ttk.Button(self, text="计算最优路径", command=self.calculate_ans, style='primary.TButton').grid(
            row=row, column=2, padx=10)


    def __init(self):
        self.condition=Condition()
        self.have_init=True
        self.weatherVar.set(self.condition.weather)
        self.temperatureVar.set(self.condition.temperature)
        self.sartingVar.set(self.condition.starting)
        self.endingVar.set(self.condition.ending)
        self.hourVar.set(self.condition.nowtime.hour)
        self.minVar.set(self.condition.nowtime.minute)

    def __check_Init(self):
        if not self.have_init:
            tkinter.messagebox.showerror('警告','还未初始化')
            return False
        return True
    
    def calculate_ans(self):
        if self.__check_Init():
            self.path_walk=Calculate.CalculatePath(self.condition,Mode.WalkingMode)
            self.path_cycle=Calculate.CalculatePath(self.condition,Mode.CyclingMode)
            self.path_drive=Calculate.CalculatePath(self.condition,Mode.DrivingMode)
            tkinter.messagebox.showinfo('提示','计算成功')

            # clear
            self.ansList.delete(0, END)

            # insert
            self.ansList.insert("end",'步行最优：'+' -> '.join(self.path_walk.getPath()[0]))
            self.ansList.insert("end",'骑车最优：')
            self.ansList.insert("end",'         步行:'+ ' -> '.join(self.path_cycle.getPath()[0]))
            self.ansList.insert("end",'         骑车:'+' -> '.join(self.path_cycle.getPath()[1]))
            self.ansList.insert("end",'         步行:'+' -> '.join(self.path_cycle.getPath()[2]))
            self.ansList.insert("end",'驾车最优：')
            self.ansList.insert("end",'         步行:'+' -> '.join(self.path_cycle.getPath()[0]))
            self.ansList.insert("end",'         驾车:'+' -> '.join(self.path_cycle.getPath()[1]))
            self.ansList.insert("end",'         步行:'+' -> '.join(self.path_cycle.getPath()[2]))

