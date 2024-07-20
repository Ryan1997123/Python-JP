import tkinter
root = tkinter.Tk()
root.title("初めてのウィンドウ")
canvas = tkinter.Canvas(root, width=400, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="./images/iroha.png")
canvas.create_image(200, 300, image=gazou)
root.mainloop()
