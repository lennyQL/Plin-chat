#<=====Plin's GUI=====>

import tkinter as tk

###############
# interface
###############

def run():
# global variable
    global enter, response_area, lb, action

# main window
    root = tk.Tk()
# window size
    root.geometry("880x560")
# window title
    root.title("Chat Bot : PLIN")
# font
    font = ("Helevetica", 14)
    font_log = ("Helevetica", 12)

# menu bar
    menubar = tk.Menu(root)
    root.config(menu=menubar)
# 「ファイル」menu
    filemenu = tk.Menu(menubar)
    menubar.add_cascade(label="ファイル", menu=filemenu)
    filemenu.add_command(label="閉じる", command=root.destroy)
# 「オプション」menu
    action = tk.IntVar()
    optionmenu = tk.Menu(menubar)
    menubar.add_cascade(label="オプション", menu=optionmenu)
    optionmenu.add_radiobutton(
        label="Responderを表示",  #アイテム名
        variable = action,       #選択時の値を格納するオブジェクト
        value = 0                #actionの値を0にする
    )
    optionmenu.add_radiobutton(
        label="Responderを表示しない",  #アイテム名
        variable = action,       #選択時の値を格納するオブジェクト
        value = 1                #actionの値を1にする
    )

# キャンバス
    canvas = tk.Canvas(
                root,            #親要素をメインウインドウに設定
                width = 500,     #幅
                height = 300,    #高さ
                relief=tk.RIDGE, #枠線の表示
                bd=2             #枠線の幅
            )
    canvas.place(x=370, y=0)

    img = tk.PhotoImage(file = "plin1.gif") #表示するイメージ
    canvas.create_image(
        0,
        0,
        image = img,
        anchor = tk.NW           #配置の起点となる位置(NorthWest)
    )


# main loop
    root.mainloop()

#*****main program*****
if __name__ == "__main__":
    run()
