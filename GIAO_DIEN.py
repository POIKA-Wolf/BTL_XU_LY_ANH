from tkinter import *

# thư viện chèn ảnh pillow
from PIL import ImageTk, Image

master = Tk()  # mở lên cửa sổ chương trình

master.title("giao diện")  # tên cửa sổ giao diện
master["bg"] = "white"  # màu nền trắng
master.attributes("-topmost", True)  # luôn hiển thị trên màn hình trừ khi mình tắt
master.geometry("700x500")  # kích thước ảnh XxY
name = Label(master, bg="red", text="Các màu điện trở", font=("Arial", 15)).place(
    x=30, y=50
)
email = Label(master, text="Giá trị điện trở", font=("Arial", 15)).place(
    x=30, y=90
)  # bg màu ô , fg màu chữ
password = Label(master, text="  BÁO LỖI  ", font=("Arial", 15)).place(x=30, y=130)

# GTtro=Label(master, text=+answer, font=("Arial", 15))
# GTtro.place(x=200, y=50)

# chiều cao của ô nhập phụ thuộc vào kích thước chứ
e2 = Entry(master, width=20, font=("Arial", 15)).place(x=200, y=90)
e3 = Entry(master, width=40, font=("Arial", 15)).place(x=200, y=130)


# redbutton = Button(top, text="Red", font=("Arial", 15), fg="red", command=anvao)
# redbutton.place(x=20, y=450, width=70, height=30)
greenbutton = Button(master, text="Black", font=("Arial", 15), fg="black")
greenbutton.place(x=200, y=450, width=70, height=30)
bluebutton = Button(master, text="Blue", font=("Arial", 15), fg="blue")
bluebutton.place(x=400, y=450, width=70, height=30)
blackbutton = Button(master, text="Green", font=("Arial", 15), fg="green")
blackbutton.place(x=580, y=450, width=70, height=30)


img_import = Image.open("T.png")
resize = img_import.resize((250, 250), Image.LANCZOS)
img = ImageTk.PhotoImage(resize)

hinh_anh = Button(master, text="hinh", font=("Time New Roman", 11), image=img)
hinh_anh.place(x=410, y=180)

master.mainloop()
