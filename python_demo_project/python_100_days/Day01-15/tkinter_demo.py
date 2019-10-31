import tkinter
import tkinter.messagebox

def main():
    flag = True

    #修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color,msg = ('red','hello world!') if flag else ('blue','goodbye,world')
        label.config(text=msg,fg=color)
    
    #确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel("确定要退出吗?"):
            top.quit()
    
    #创建顶层窗口
    top = tkinter.Tk()
    top.geometry('240x160')
    top.title('小游戏')
    #创建标签对象并添加到顶层窗口
    label = tkinter.Label(top,text='hello world!',font='Arial -32',fg='red')
    label.pack(expand=1)
    #创建一个装按钮的容器
    pane1 = tkinter.Frame(top)
    #创建按钮对象并添加到容器中,设置回调函数
    button1 = tkinter.Button(pane1,text='修改',command=change_label_text)
    button1.pack(side='left')

    button2 = tkinter.Button(pane1,text='退出',command=confirm_to_quit)
    button2.pack(side='right')
    pane1.pack(side='bottom')

    #打开主事件循环
    tkinter.mainloop()

if __name__ == "__main__":
    main()

    