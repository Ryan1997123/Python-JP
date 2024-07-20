import tkinter
import tkinter.font

#Pythonでボタンをクリックしたときの処理を関数で定義
def click_btn():
    button["text"] = "クリックしました"

root = tkinter.Tk()
print(tkinter.font.families())
root.title("初めてのウィンドウ")
root.geometry("800x600")
#ボタンをクリックすると関数を実行する
button = tkinter.Button (root, text="ボタンの文字例",
font=("Times New Roman", 24), command=click_btn)
button.place(x=200, y=100)
root.mainloop()

