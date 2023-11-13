from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

root = Tk()
root.title("ShareIT")
root.geometry("377x520+500+200")
root.config(bg="#f4fdfe")
root.resizable(False,False)

def Send():
    window = Toplevel(root)
    window.title("Send")
    window.geometry("377x520+500+200")
    window.config(bg="#f4fdfe")
    window.resizable(False,False)

    def select_file():
        global filename
        filename = filedialog.askopenfilename(initialdir = os.getcwd(), title = 'Select Image File', filetype =(('file_type','*.txt'),('all files','*.*')))

    def sender():
        s = socket.socket()
        host = socket.gethostname()
        port = 8080
        s.bind((host,port))
        s.listen(1)
        print(host)
        print('waiting for any incoming connections...')
        conn,addr = s.accept()
        file = open(filename,'rb')
        file_data = file.read(1024)
        conn.send(file_data)
        print("Data has been transmitted successfully...")


    image_icon1 = PhotoImage(file="Img/send_btn.png")
    window.iconphoto(False,image_icon1)

    Sbackground = PhotoImage(file="Img/sender_Avt.png")
    scale_Sbackground = Sbackground.subsample(1,2)

    Label(window,image=scale_Sbackground).place(x=-2,y=0)
    Mbackground = PhotoImage(file="Img/id.png")
    Label(window,image=Mbackground,bg='#f4fdfe').place(x=60,y=200)

    host = socket.gethostname()
    Label(window,text=f'ID:{host}',bg='white',fg='black').place(x=150,y=270)

    Button(window,text=" + select file", width=10,height=1,font='arial 12 bold',bg="#fff",fg="#000",command=select_file).place(x=140, y= 100)
    Button(window, text="SEND",width=8,height=1,font='arial 12 bold',bg="#000",fg="#fff",command=sender).place(x=260, y=100)
    window.mainloop()

def Receive():
    main = Toplevel(root)
    main.title("Receive")
    main.geometry("377x520+500+200")
    main.config(bg="#f4fdfe")
    main.resizable(False,False)

    def receiver():
        ID = SenderID.get()
        filename1 = incoming_file.get()
        s=socket.socket()
        port = 8080
        s.connect((ID,port))
        file = open(filename,'wb')
        file_data = s.recv(1024)
        file.write(file_data)
        file.close()
        print("File has been received successfully")
        



    image_icon2 = PhotoImage(file="Img/1679498.png")

    main.iconphoto(False,image_icon2)

    Hbackground = PhotoImage(file="Img/file_receive.png")
    Label(main,image=Hbackground).place(x=-2,y=0)
    
    logo = PhotoImage(file="Img/siba.png")
    Label(main,image=logo,bg="#f4fdfe").place(x=140, y=230)

    Label(main, text="Receive", font=('arial',20),bg="#f4fdfe").place(x=140,y=180)
    Label(main, text="Input sender ID",font=('arial', 10, 'bold'),bg="#f4fdfe").place(x=20, y=340)
    SenderID = Entry(main, width=25,fg="black",border=2,bg='white',font=('arial',15))
    SenderID.place(x=20,y=360)
    SenderID.focus()

    Label(main, text="filename for the incoming file:",font=('arial', 10, 'bold'),bg="#f4fdfe").place(x=20, y=410)
    incoming_file = Entry(main, width=25,fg="black",border=2,bg='white',font=('arial',15))
    incoming_file.place(x=20,y=430)

    imageIcon = PhotoImage(file="Img/arrow.png")
    scaleimageicon = imageIcon.subsample(4,8)
    rr= Button(main,text="Receive",compound=LEFT,image=scaleimageicon,width=140,bg="#39c790",font="arial 14 bold",command=receiver)
    rr.place(x=20,y=470)


    main.mainloop()
    
#icon
image_icon = PhotoImage(file="Img/best-file-sharing.png")
root.iconphoto(False,image_icon)
Label(root, text="File transfer", font=('Acumin Variable Concept',20,'bold'),bg="#f4fdfe").place(x=20,y=20)
Frame(root,width=400, height=2,bg="#f3f5f6").place(x=25, y=80)
send_image = PhotoImage(file="Img/send_btn.png")
scale_img = send_image.subsample(8,8)
send = Button(root,image=scale_img,bg="#f4fdfe",bd=0,command=Send)
send.place(x=30,y=100)
receive_img = PhotoImage(file="Img/1679498.png");
scale_receive_img = receive_img.subsample(8,8)
receive = Button(root,image=scale_receive_img,bg="#f4fdfe",bd=0,command=Receive)
receive.place(x = 280,y = 100)
Label(root,text="Send",font=('Acumin Variable Concept',14,'bold'),bg="#f4fdfe").place(x=38,y=175)
Label(root,text="Receive",font=('Acumin Variable Concept',14,'bold'),bg="#f4fdfe").place(x=275,y=175)

background = PhotoImage(file="Img/bg2.png")
scale_background = background.subsample(2,2)
Label(root,image = scale_background).place(x=-2,y=312)
root.mainloop()

#Label


