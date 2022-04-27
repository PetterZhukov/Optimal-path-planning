from tkinter import Tk
from ttkbootstrap import Style
from UI.MainPage import MainPage



style = Style(theme = "morph") # 使用的主题名称
root = style.master
root.title("最优路径规划  --Zkv")
MainPage(root)
root.mainloop()