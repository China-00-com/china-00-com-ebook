# coding:utf-8

from tkinter import *


def login(event):
    true_account = "111"
    true_password = "222"
    account = account_e.get()
    password = password_e.get()
    if account == true_account and password == true_password:
        info_l["text"] = "登陆成功"
    else:
        info_l["text"] = "用户名或密码错误"
        account_e.delete(0, len(account))
        password_e.delete(0, len(password))


root = Tk()
root.wm_title("Spide部署工具")
account_l = Label(root, text="账号")
account_l.grid(row=0, sticky=W)

account_e = Entry(root)
account_e.grid(row=0, column=1, sticky=E)

password_l = Label(root, text="密码")
password_l.grid(row=1, sticky=W)

password_e = Entry(root)
password_e["show"] = "*"
password_e.grid(row=1, column=1, sticky=E)

login_b = Button(root, text="登陆")
login_b.bind("<Button-1>", login)
login_b.grid(row=2, column=1, sticky=E)

info_l = Label(root, text="提示信息")
info_l.grid(row=3)

root.mainloop()
