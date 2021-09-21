from tkinter import *
from tkinter import ttk, messagebox, filedialog
import tkinter as tk
import DB_con_FB
import re, sys, datetime,emoji
import DB_encryption
import encryption_form, decryption_form,emoji

print(sys.getrecursionlimit())
# sys.setrecursionlimit(1000)
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  # this is for checking valid email
# this is not correct method and it is in under x development


class Login(tk.Tk):
    def __init__(self, master) -> None:

        self.master = master
        self.master.resizable(False, False)
        get_width=self.master.winfo_screenwidth()
        get_height=self.master.winfo_screenheight()
        print(get_height,get_width)
     #   log_widht=300
      #  log_height=415
      #  x =(log_widht/3) - (get_width/3)
       # y = (log_height/2) - (get_height/3)
        self.master.geometry(f'{300}x{415}+{int(520)}+{int(130)}')
        self.master.title("LOGIN | SIGNUP Window")
        self.master.iconbitmap('img_log_sig_otp/login.ico')
       # self.master.eval('tk::PlaceWindow . mid')


        #creating images
        self.img_log=PhotoImage(file="img_log_sig_otp/rsz_log_bak.gif")
        #need to change fonts!!!


        # creating a frame to hold
        self.frame_header = ttk.Frame(self.master)
        self.fram_body = ttk.Frame(master=self.master, relief=SOLID)

        #creating emojis
        self.a=emoji.emojize(":cross_mark:")
        self.a1=emoji.emojize(":wastebasket:")
        self.a2=emoji.emojize(":dashing_away:")
        self.a3 = emoji.emojize(":crossed_swords:")


        # creating a label
        self.login_header_label = Label(self.frame_header, text=" LOGIN  |  SIGNUP ", font=('Arial', 22, 'bold')
                                            ,border=5,borderwidth=3,bg="black",fg="red")
        self.login_label=ttk.Label(self.fram_body,image=self.img_log)
        self.username_label = Label(self.fram_body, text="Username:",bg="black",fg="red",font=('Haettenschweiler'))
        self.password_label = Label(self.fram_body, text="Password:",bg="black",fg="red",border=2,font=('Haettenschweiler'))
        self.design_label = Label(self.fram_body,text="-----------------------------------------------------"
                                  ,bg="black",fg="red")
        # creating a entry
        self.usr_entry =  Entry(self.fram_body, width=20,bg="black",fg="yellow")
        self.pass_entry = Entry(self.fram_body, width=20,show='#',bg="black",fg="yellow")

        # cretinf buttons
        self.login_btn = Button(self.fram_body, text="Login"+str(self.a2), command=self.login_btn_com,fg="red",bg="black",activebackground="yellow",
                                font=("Garamond",11),border=4,borderwidth=4)
        self.clear_btn = Button(self.fram_body, text="Clear"+str(self.a1), command=self.clear_btn_com,fg="red",bg="black",activebackground="yellow"
                                ,font=("Garamond",11),border=4,borderwidth=4)
        self.signup_btn = Button(self.fram_body, text="Signup"+str(self.a3), command=self.signup_btn_com,fg="red",bg="black",activebackground="yellow"
                                 ,font=("Garamond",11),border=4,borderwidth=4)
        self.quit_btn = Button(self.fram_body, text="Quit"+str(self.a), command=self.quit_btn_com,fg="red",bg="black",activebackground="yellow"
                               ,font=("Garamond",11),border=4,borderwidth=4)

        #creating a hover  structure
        self.login_btn.bind("<Enter>",self.hover_enter_login)
        self.login_btn.bind("<Leave>",self.hover_leave_login)

        self.clear_btn.bind("<Enter>", self.hover_enter_clear)
        self.clear_btn.bind("<Leave>", self.hover_leave_clear)

        self.signup_btn.bind("<Enter>", self.hover_enter_signup)
        self.signup_btn.bind("<Leave>", self.hover_leave_signup)

        self.quit_btn.bind("<Enter>", self.hover_enter_quit)
        self.quit_btn.bind("<Leave>", self.hover_leave_quit)


        # creating for griding and packing
        self.frame_header.pack()
        self.fram_body.pack()

        self.login_label.place(x=0,y=0)

        self.login_header_label.grid(row=0, columnspan=2, padx=5, pady=20, ipadx=5, ipady=5)
        self.username_label.grid(row=0, column=0, padx=30, pady=30, ipadx=5, ipady=5, sticky='w')
        self.password_label.grid(row=1, column=0, padx=30, pady=30, ipadx=5, ipady=5, sticky='w')

        self.usr_entry.grid(row=0, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        self.pass_entry.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)

        self.design_label.grid(row=2,columnspan=2)

        self.login_btn.grid(row=3, column=0, padx=5, pady=5, ipadx=2, ipady=2)
        self.clear_btn.grid(row=3, column=1, padx=5, pady=5, ipadx=2, ipady=2)
        self.signup_btn.grid(row=4, column=0, padx=5, pady=10, ipadx=5)
        self.quit_btn.grid(row=4,column=1, padx=5, pady=10, ipadx=5)

    # w, h =self.master.winfo_screenwidth(),self.master.winfo_screenheight()
    # print(w,h)

    #creating a hover function:
    def hover_enter_login(self,event):
        self.login_btn["bg"]="#f72f2f"
    def hover_leave_login(self,e):
        self.login_btn["bg"]="black"

    def hover_enter_clear(self,event):
        self.clear_btn["bg"]="#e8383e"
    def hover_leave_clear(self,e):
        self.clear_btn["bg"]="black"


    def hover_enter_signup(self,event):
        self.signup_btn["bg"]="#f78c2f"
    def hover_leave_signup(self,e):
        self.signup_btn["bg"]="black"

    def hover_enter_quit(self,event):
        self.quit_btn["bg"]="yellow"
    def hover_leave_quit(self,e):
        self.quit_btn["bg"]="black"

    def login_btn_com(self):
        print("Logging u in!")
        self.usr_name = self.usr_entry.get()
        self.usr_pass = self.pass_entry.get()
        print(self.usr_name, self.usr_pass)
        if self.usr_name == '':
            print("checking for username entered or not")
            messagebox.showerror(title="Login error!", message="Please enter your username!!")
        if self.usr_pass == '':
            print("checking for password entered or not!")
            messagebox.showerror(title="Login error!", message="Please enter your password!")
        self.auth = DB_con_FB.get_data(self.usr_name, self.usr_pass)  # need to change here
        print(self.auth)  # need to change here
        #   self.auth1=[]
        #   self.auth1 +=self.auth
        print([self.usr_name, self.usr_pass])

        if self.auth == 1:
            messagebox.showinfo(title="Login", message="  Login Successfull!!  "
                                                       "by login you are accepting our Terms and Condition!")
            self.encryption_window = Toplevel(self.master)
            self.log3 = Encrypt_Decrypt(self.encryption_window)
            self.master.iconify()


        else:
            messagebox.showinfo(title="Login", message="    Login Unsuccessfull!!    ")

        self.clear_btn_com()



    def signup_btn_com(self):

        #    for x in self.fram_body.winfo_children():
        #       x.destroy()
        #   for y in self.frame_header.winfo_children():
        #      y.destroy()
        #   self.fram_body.pack_forget()
        #  self.frame_header.pack_forget()
        print("Siginning u in!!")
        self.new_window = Toplevel(self.master)
        self.log = signup_window(self.new_window)
       # self.master.iconify()

    def clear_btn_com(self):
        print("cleared")
        self.usr_entry.delete(0, END)
        self.pass_entry.delete(0, END)

    def quit_btn_com(self):
        self.master.quit()



class signup_window():
    def __init__(self, master) -> None:

        self.master_sign = master
        self.master_sign.title("SIGNUP Window")

       # self.master_sign.geometry("400x450")
        self.master_sign.geometry(f'{400}x{450}+{int(520)}+{int(110)}')
        self.master_sign.resizable(False, False)
        self.master_sign.iconbitmap('img_log_sig_otp/sign_up.ico')

        # creaeting a frame
        self.frame_header = ttk.Frame(self.master_sign, relief=SOLID)
        self.frame_body = ttk.Frame(self.master_sign, relief=RIDGE)

        #creating a image
        self.img_back=PhotoImage(file="img_log_sig_otp/rsz_680914.gif")

        #creating emojis
        self.b=emoji.emojize(":crossed_swords:")
        self.b1 = emoji.emojize(":fast_reverse_button:")
        self.b2 = emoji.emojize(":wastebasket:")
        self.b3 = emoji.emojize(":atom_symbol:")



        # creating a labels
        # for header
        self.header_label = Label(self.frame_header, text=str(self.b)+"          |  Signup  |          "+str(self.b), font=('Arial', 22, 'bold')
                                  ,bg='#5e8feb')

        # for body
        self.img_label = Label(self.frame_body, image=self.img_back)
        self.user_input = Label(self.frame_body, text="Enter your username, Password  Email id for signup",
                                    font=('Arial', 11, 'bold'),bg="#97b4c4",fg="black")
        self.username_label = Label(self.frame_body, text="Username:",bg="#97b4c4",fg="black"
                                    ,font=('Haettenschweiler'))
        self.password_label = Label(self.frame_body, text="Password:",bg="#97b4c4",fg="black"
                                    ,font=('Haettenschweiler'))
        self.email_label = Label(self.frame_body, text="Email:",bg="#97b4c4",fg="black"
                                 ,font=('Haettenschweiler', 13))


        # entry field
        self.usr_entry = Entry(self.frame_body, width=20,bg="#99bdff",fg="black")
        self.pass_entry = Entry(self.frame_body, width=20,bg="#99bdff")
        self.email_entry = Entry(self.frame_body, width=24,bg="#99bdff")

        # creating buttons  ##a1c4cf
        self.signup_btn = Button(self.frame_body, text="Signup"+str(self.b), command=self.signup_btn_com_nw
                                 ,bg="#1c84a3",fg="black",activebackground="#007599",border=4,borderwidth=5
                                 ,font=("Garamond",11,'bold'))

        self.clear_btn = Button(self.frame_body, text="Clear"+str(self.b2), command=self.clear_btn_com_nw
                                ,bg="#1c84a3",fg="black",activebackground="#007599",border=4,borderwidth=5
                                ,font=("Garamond",11,'bold'))
        self.back_btn = Button(self.frame_body, text=str(self.b1)+"Back", command=self.back_btn_com
                               ,bg="#1c84a3",fg="black",activebackground="#007599",border=4,borderwidth=5
                               ,font=("Garamond",11,'bold'))

        #creating hover structure
        self.signup_btn.bind("<Enter>",self.hover_enter_signup)
        self.signup_btn.bind("<Leave>",self.hover_leave_signup)

        self.clear_btn.bind("<Enter>", self.hover_enter_clear)
        self.clear_btn.bind("<Leave>", self.hover_leave_clear)

        self.back_btn.bind("<Enter>", self.hover_enter_back)
        self.back_btn.bind("<Leave>", self.hover_leave_back)

        # griding and packing
        self.img_label.place(x=0, y=0)


        self.frame_header.pack()
        self.frame_body.pack()



        self.header_label.grid(row=0, columnspan=2)

        self.user_input.grid(row=0, columnspan=2, padx=10, pady=20, ipady=3, ipadx=3)

        self.username_label.grid(row=1, column=0, padx=5, pady=5, ipadx=3, ipady=3)
        self.password_label.grid(row=2, column=0, padx=5, pady=5, ipadx=3, ipady=3)
        self.email_label.grid(row=3, column=0, padx=5, pady=5, ipadx=3, ipady=3)

        self.usr_entry.grid(row=1, column=1, padx=20, pady=25, ipadx=3, ipady=3)
        self.pass_entry.grid(row=2, column=1, padx=20, pady=25, ipadx=3, ipady=3)
        self.email_entry.grid(row=3, column=1, padx=20, pady=25, ipadx=3, ipady=3)

        self.clear_btn.grid(row=4, column=1, padx=5, pady=5, ipadx=3, ipady=3)
        self.signup_btn.grid(row=4, column=0, padx=5, pady=5, ipadx=3, ipady=3, sticky='ne')
        self.back_btn.grid(row=5, columnspan=2, padx=5, pady=10, ipadx=5)
    #creating a hover functions
    def hover_enter_signup(self,e):
        self.signup_btn["bg"]="#a1c4cf"
    def hover_leave_signup(self,e):
        self.signup_btn["bg"]="#1c84a3"

    def hover_enter_clear(self,e):
        self.clear_btn["bg"]="#a1c4cf"
    def hover_leave_clear(self,e):
        self.clear_btn["bg"]="#1c84a3"

    def hover_enter_back(self,e):
        self.back_btn["bg"]="#a1c4cf"
    def hover_leave_back(self,e):
        self.back_btn["bg"]="#1c84a3"


    def signup_btn_com_nw(self):
        self.usr = self.usr_entry.get()
        self.password = self.pass_entry.get()
        self.email = self.email_entry.get()
        if self.usr == '':
            messagebox.showinfo(title="Signup error", message="Enter your username!")

        if self.password == '':
            messagebox.showinfo(title="Signup error", message="Enter your Password!")

        if self.email == '':
            messagebox.showinfo(title="Signup error", message="Enter your email!")

        else:
            self.a = checkmail(self.email)
        if self.a != 1:
            messagebox.showerror(title="Email error", message="Check  your Email! please")
        else:
            self.verify=DB_con_FB.username_input(self.usr, self.password, self.email)

        if self.verify == 1:
            messagebox.showinfo(title="SIGNED UP|SUCCESFULLY", message="One more step to verify You!")
            DB_con_FB.getting_data(self.usr,self.password)
            self.master_sign.iconify()
            self.otp_window = Toplevel(self.master_sign)
            self.log = otp_window_(self.otp_window)
        else:
            print("ooops!!")

        self.master_sign.tkraise()
        self.clear_btn_com_nw()

    def clear_btn_com_nw(self):
        self.usr_entry.delete(0, END)
        self.pass_entry.delete(0, END)
        self.email_entry.delete(0, END)

    def back_btn_com(self):
        Login(master=self.master_sign)
        self.master_sign.destroy()

        #    self.master.geometry("%dx%d+0+0" % (w, h))


class otp_window_():
    def __init__(self, master) -> None:
        self.master_otp = master
        self.master_otp.geometry("360x300")
        self.master_otp.geometry(f'{360}x{300}+{int(520)}+{int(110)}')
        self.master_otp.title("<<OTP>>")
        self.otp_cont = ttk.Frame(self.master_otp, relief=GROOVE)
        self.master_otp.iconbitmap('img_log_sig_otp/otp.ico')

        #creating image

        self.back_otp=PhotoImage(file="img_log_sig_otp/rsz_otp.gif")
        print("entered")
        #creating a frame
        # creatin labels
        self.otp_design=Label(self.otp_cont,image=self.back_otp)
        self.label_header = Label(self.otp_cont, text="  OTP | VERIFICATION   ", font=('Arial', 22, 'bold'),bg="black",fg="green")

        self.otp_label = Label(self.otp_cont, text="Enter your 5 digit otp send to your registered email!",
                                   font=('Arial', 10, 'bold'),bg="black",fg="green")

        # creating entry
        self.otp_cont.pack()
        self.otp_entry = Entry(self.otp_cont, width=20,bg="#4abd53")
        print("entered near button")

        # creatin buttons
        self.otp_btn = Button(self.otp_cont, text="Verify", command=self.verify,font=('arial',10)
                              ,bg="black",fg="#005407",activebackground="#026b0b")
        #creating a hover
        self.otp_btn.bind("<Enter>",self.hover_enter_otp)
        self.otp_btn.bind("<Leave>",self.hover_leave_otp)

        # gridding
        self.otp_design.place(x=0,y=0)
        self.label_header.grid(row=0, column=0, padx=20, pady=20, ipadx=3, ipady=1)
        self.otp_label.grid(row=1, column=0, padx=20, pady=20, ipadx=3, ipady=1)
        self.otp_entry.grid(row=2, column=0, padx=20, pady=20, ipadx=3, ipady=1)
        self.otp_btn.grid(row=3, column=0, padx=30, pady=30, ipadx=5, ipady=1)
        print("entered near hover!")

        self.master_otp.tkraise()

    def hover_enter_otp(self,e):
        self.otp_btn["bg"]="#78f582"
    def hover_leave_otp(self,e):
        self.otp_btn["bg"]="black"

    def verify(self):
        self.otp_value = self.otp_entry.get()
        self.otp_verify1 = int(self.otp_value)
        self.otp_verify =DB_con_FB.opt_verification(self.otp_verify1)
        if self.otp_verify == 1:
            messagebox.showinfo(title="OTP | SUCCESSFULL", message="OTP Verification is Successful!!")
            Login(master=self.master_otp)
            self.master_otp.destroy()
        else:
            messagebox.showerror(title="OTP | UNSUCCESSFULL", message="Please check your otp!!")



def checkmail(email):
    print(email)
    if (re.search(regex, email)):
        print("Valid Email")  # need to return and show in mesageg box
        return 1
    else:
        print("Invalid Email")


class Encrypt_Decrypt():
    def __init__(self, master):
      #  super(, self).__init__(master)
        self.master_ed = master
        self.master_ed.resizable(False, False)
        self.frame = ttk.Frame(self.master_ed).pack()
        self.master_ed.geometry("640x520")

        self.master_ed.geometry(f'{640}x{520}+{int(400)}+{int(80)}')
        self.master_ed.title("#Selection#")

        self.master_ed.iconbitmap('img_log_sig_otp/encryption.ico')

        # crreating a styles for window2
        self.style = ttk.Style()

        self.style.configure('frame_header.TLabel', background='black')
        self.style.configure('frame_body.TLabel', background='blue')

        self.style.configure('frame_body1.TButton', background='#24e34a')
        self.style.configure('frame_body1.TButton', background='#24e34a')
        self.style.configure('frame_body1.TButton', background='#24e34a')

        # start code here

        self.frame_header = Frame(self.master_ed,background='black')

        self.frame_body =Frame(self.master_ed, background='black')

        # using images

        self.encr_img = PhotoImage(
            file="img_window1/rsz_1rsz_heade_back.gif")  # make the header with aa diagram
        self.imf_header = ttk.Label(self.frame_header, image=self.encr_img)
        self.imf_header.grid(row=0, column=1)
        self.back_grod = PhotoImage(
            file='img_window1/rsz_wallpaperflarecom_wallpaper.gif')
        self.img_label = ttk.Label(self.frame_body, image=self.back_grod)
        self.img_label.place(x=0, y=0)

        self.label_header = ttk.Label(self.frame_header, style='frame_header.TLabel', text="     ENCRYPTION AND DECRYPTION     "
                                      , font=('Arial', 20, 'bold'), foreground='Red')

        self.label_design = ttk.Label(self.frame_header,
                                      text="       ------------------------------------------------------ "
                                           "       ---------------------------------------- "
                                      , background='black', foreground='red')

        self.label_content = ttk.Label(self.frame_body, style='frame_body.TLabel', text="     Select the option that   "
                                                                                        "the operation that u have to perform !     ",
                                       font=(
                                           'Arial', 16), foreground='red', background='black')

        # creating a images for buttons and configuration!

        self.btn_encryp = PhotoImage(file='img_window1/rsz_download.gif')
        self.btn_decryp = PhotoImage(file='img_window1/rsz_download_1.gif')
        self.btn_quit = PhotoImage(file='img_window1/rsz_qiut.gif')

        # creating a button for encryption and decryption
        self.encry_btn = Button(self.frame_body, text="ENCRYPTION", bg='#00f024', fg='white', activebackground='red'
                                , image=self.btn_encryp, padx=4, compound=RIGHT, command=self.encrypt, font='Ravie')
        self.decry_btn = Button(self.frame_body, text="DECRYPTION", bg='#29bf23', fg='white', command=self.decrypt
                                , image=self.btn_decryp, padx=4, compound=RIGHT, activebackground='red', font='Ravie')
        self.quit = Button(self.frame_body, text="QUIT", bg='#0a6e06', fg='white', activebackground='#d400a2',
                           image=self.btn_quit, padx=5, compound=RIGHT, command=self.quit_, font='Ravie',
                           cursor="pirate")

        # creating about label

        self.abt = ttk.Label(self.frame_body, text="Developed by:- "
                                                   "  Akatsuki Organisation and development   ", font='Ravie',
                             background='black', foreground='red')
        # self.name=self.usr_name
        # self.usr_label=ttk.Label(self.frame_body,text=self.name,font='Ravie',background='black',foreground='red')

        # creating a hover structure
        self.encry_btn.bind("<Enter>", self.hover_enter_encryp)
        self.encry_btn.bind("<Leave>", self.hover_leave_encryp)

        self.decry_btn.bind("<Enter>", self.hover_enter_decryp)
        self.decry_btn.bind("<Leave>", self.hover_leave_decryp)

        self.quit.bind("<Enter>", self.hover_enter_quit)
        self.quit.bind("<Leave>", self.hover_leave_quit)

        # gridding
        self.frame_header.pack()
        self.frame_body.pack()

        self.label_header.grid(row=0, column=0)
        self.label_design.grid(row=1, column=0)
        self.label_content.grid(row=0, column=0)

        self.encry_btn.grid(row=1, column=0, padx=0, pady=40, ipadx=5, ipady=5)
        self.decry_btn.grid(row=2, column=0, padx=0, pady=40, ipadx=5, ipady=5)
        self.quit.grid(row=3, column=0, padx=0, pady=40, ipadx=5, ipady=5)

        self.abt.grid(row=4, column=0, padx=4)

    #  self.usr_label.place(x=6,y=350)

    def quit_(self):
        self.master_ed.quit()

    def encrypt(self):
        self.enc = Toplevel(self.master_ed)
        self.app = encryption(self.enc)

    def decrypt(self):
        self.dec = Toplevel(self.master_ed)
        self.app = decryption(self.dec)

    # creating a hover function
    def hover_enter_encryp(self, event):
        self.encry_btn["bg"] = "#00ff12"

    def hover_leave_encryp(self, event):
        self.encry_btn["bg"] = "#29bf23"

    def hover_enter_decryp(self, event):
        self.decry_btn["bg"] = "#00ff12"

    def hover_leave_decryp(self, event):
        self.decry_btn["bg"] = "#00ad1a"

    def hover_enter_quit(self, event):
        self.quit["bg"] = "#00ff12"

    def hover_leave_quit(self, event):
        self.quit["bg"] = "#0a6e06"


class encryption():
    def __init__(self, master):
        print("encryption part entered")
        self.master_encryp = master
        self.master_encryp.geometry("410x270")
        self.master_encryp.geometry(f'{410}x{270}+{int(500)}+{int(110)}')
        self.master_encryp.resizable(False, False)
        self.master_encryp.title("#Encryption#")

        # creating a label and entry for the encryption
        self.frame_header = Frame(self.master_encryp,bg='blue')
        self.frame_body = Frame(self.master_encryp,bg='red')

        # creating a background
        self.back_grod = PhotoImage(file='img_window1/rsz_rdblu4.gif')
        self.img_label = ttk.Label(self.frame_body, image=self.back_grod)
        self.img_label.place(x=0, y=0)

        # creating a styles\
        self.style = ttk.Style()
        self.style.configure("body.TLabel", background='#783af2')
        self.style.configure("design.TLabel", background='#1e0257')
        self.style.configure("header.TLabel", background='red')
        self.style.configure('TFrame', background='red')

        # creasting icon\
        self.master_encryp.iconbitmap('img_window1/data-encryption-32.ico')

        # creating a label and entry
        self.emo = emoji.emojize(":locked_with_key:")
        self.label_head = ttk.Label(self.frame_header, text=str(self.emo)+"    ENCRYPTION!!!  ", font=('Showcard Gothic', 20, 'bold')
                                   ,style='header.TLabel')
        self.img_header = PhotoImage(
            file='img_window1/rsz_window2_back.gif').subsample(2, 2)
        self.img_header_ = ttk.Label(self.frame_header, image=self.img_header)

        #    self.label_design=ttk.Label(self.frame_header,text='---------------------------------------------------------' )

        self.label_encrypt = ttk.Label(self.frame_body, text="Text:", style='body.TLabel', font='Stencil')
        self.label_key = ttk.Label(self.frame_body, text="Key:", style='body.TLabel', font='Stencil')
        self.label_encrypted = ttk.Label(self.frame_body, text="Encryted text:", style='body.TLabel', font='Stencil')

        self.entry_encrypt = Entry(self.frame_body, width=20, font='Georgia',bg='#783af2',fg='#000000')
        self.entry_key = Entry(self.frame_body, width=20, font='Georgia',bg='#783af2',fg='#000000')
        self.entry_encrypted = ttk.Entry(self.frame_body, width=20, font='Georgia', state="disabled",style='body.TLabel')

        # self.label_design = ttk.Label(self.frame_body, text='-----------------------------------------------------')
        #      self.label_design1 = ttk.Label(self.frame_body,
        #                                  text='--------------------------------------------------------------------')

        # creating a images for butn
        self.generate_img = PhotoImage(file='img_window1/generate.gif').subsample(2,
                                                                                                                      2)
        self.clear_img = PhotoImage(file='img_window1/rsz_reset.gif').subsample(2,
                                                                                                                    2)
        self.save_img = PhotoImage(file='img_window1/save.gif').subsample(2, 2)
        self.back_img = PhotoImage(file='img_window1/back btn.gif').subsample(2, 2)

        # creating a button
        self.encrypt_btn = Button(self.frame_body, text="Generate", command=self.encryption_, bg='red', fg='white',
                                  padx=10
                                  , image=self.generate_img, compound=RIGHT, activebackground='#8800d6')
        self.clear_btn = Button(self.frame_body, text="Clear", bg='red', command=self.clear_, fg='white'
                                , image=self.clear_img, compound=RIGHT, activebackground='#8800d6')
        self.save_btn = Button(self.frame_body, text="Save", bg='red', command=self.save_, fg='white'
                               , image=self.save_img, compound=RIGHT, activebackground='#8800d6')
        self.back_btn = Button(self.frame_body, text="Back", bg='red', fg='white', command=self.back_,
                               activebackground='#8800d6')
        # creating a hover for button
        self.encrypt_btn.bind("<Enter>", self.hover_enter_encrypt)
        self.encrypt_btn.bind("<Leave>", self.hover_leave_encrypt)

        self.clear_btn.bind("<Enter>", self.hover_enter_clear)
        self.clear_btn.bind("<Leave>", self.hover_leave_clear)

        self.save_btn.bind("<Enter>", self.hover_enter_save)
        self.save_btn.bind("<Leave>", self.hover_leave_save)

        self.back_btn.bind("<Enter>", self.hover_enter_back)
        self.back_btn.bind("<Leave>", self.hover_leave_back)

        # griding and packing
        self.frame_header.pack()
        self.frame_body.pack()

        self.label_head.grid(row=0, column=0)
        self.img_header_.grid(row=0, column=1)
        #     self.label_design.grid(row=1,columnspan=2)

        self.label_encrypt.grid(row=0, column=0, padx=20, pady=20)
        self.label_key.grid(row=1, column=0, padx=20, pady=20)
        self.label_encrypted.grid(row=6, column=0, padx=5, pady=5, ipadx=4, ipady=5, sticky='w')

        self.entry_encrypt.grid(row=0, column=1, padx=20, pady=20)
        self.entry_key.grid(row=1, column=1, padx=20, pady=20)
        self.entry_encrypted.grid(row=6, column=1, padx=5, pady=5, sticky='sw')
        #    self.label_design.grid(row=2,columnspan=3,padx=20,pady=5)   .grid(row=6, column=1, padx=5, pady=5,sticky='sw')
        #   self.label_design1.grid(row=4, columnspan=3, padx=20, pady=5)

        self.encrypt_btn.grid(row=3, column=1, padx=5, pady=10, sticky='n')
        self.clear_btn.grid(row=3, column=1, padx=5, pady=10, sticky='e')
        self.save_btn.grid(row=3, column=0, padx=50, pady=10, sticky='e')
        self.back_btn.grid(row=3, column=0, padx=5, pady=10, sticky='w')

    def encryption_(self):
        print("encrypting part")
        self.a = self.entry_encrypt.get()  # need to check the text has been given or not
        self.b = str(self.entry_key.get())
        self.b_ck= self.b.isdigit()
        if self.b_ck != True:
            messagebox.showerror(title="Invalid Option",message="Enter a Number between 1 to 49!!! :)")

        if self.a == '':
            messagebox.showinfo(title="Entry error", message="Enter your encrypt text")
            self.master_encryp.tkraise()
        if self.b == '':
            messagebox.showinfo(title="Entry error", message="Enter your key")
            self.master_encryp.tkraise()

        if self.a != '':
            if self.b != '':
                self.entry_encrypted.configure(state="enabled")

        #passing the values


        self.c = encryption_form.encrypt_(self.a, self.b)
        self.d = self.entry_encrypted.insert(0, self.c)

        DB_encryption.Encryption_values(self.a, self.b,self.c)

        self.master_encryp.tkraise()

    def clear_(self):
        print("cleared")
        self.entry_encrypt.delete(0, END)
        self.entry_key.delete(0, END)
        self.entry_encrypted.delete(0, END)
        self.entry_encrypted.configure(state="disabled")

    def save_(self):
        print("successfully saved!")
        print("successfully saved!")
        self.file = filedialog.asksaveasfile(defaultextension='.txt',
                                             filetypes=[("Text file", ".txt"), ("Html file", ".html"),
                                                        ("all files", ".*")])
        self.tim = str(datetime.datetime.now())
        self.filetext_decrypt = str(self.entry_encrypt.get())
        self.filetext_decrypted = str(self.entry_encrypted.get())
        self.file.write("ENRCYPTING TEXT:")
        self.file.write('\n')
        self.file.write(self.filetext_decrypt)
        self.file.write('\n')
        self.file.write('ENCRYPTED TEXT:')
        self.file.write('\n')
        self.file.write(self.filetext_decrypted)
        self.file.write('\n')
        self.file.write(self.tim)
        self.file.close()

    def back_(self):
        self.master_encryp.destroy()

    # creating a function for hover
    def hover_enter_encrypt(self, event):
        self.encrypt_btn["bg"] = "blue"

    def hover_leave_encrypt(self, event):
        self.encrypt_btn["bg"] = "red"

    def hover_enter_clear(self, event):
        self.clear_btn["bg"] = "blue"

    def hover_leave_clear(self, event):
        self.clear_btn["bg"] = "red"

    def hover_enter_save(self, event):
        self.save_btn["bg"] = "blue"

    def hover_leave_save(self, event):
        self.save_btn["bg"] = "red"

    def hover_enter_back(self, event):
        self.back_btn["bg"] = "blue"

    def hover_leave_back(self, event):
        self.back_btn["bg"] = "red"


class decryption:
    def __init__(self, master):
        print("decryption part!!")
        self.master_decry = master
        self.master_decry.geometry("410x270")
        self.master_decry.geometry(f'{410}x{270}+{int(500)}+{int(130)}')
        self.master_decry.resizable(False, False)
        self.master_decry.title("#Decryption#")

        # creating a label and entry for the encryption
        self.frame_headers = ttk.Frame(self.master_decry)
        self.frame_bodys = ttk.Frame(self.master_decry)

        # creasting icon\
        self.master_decry.iconbitmap('img_window1/decrypted.ico')

        # creating a styles\
        self.style = ttk.Style()
        self.style.configure("body.TLabel", background='#783af2')
        self.style.configure("design.TLabel", background='#1e0257')
        self.style.configure("header.TLabel", background='blue')

        self.style.configure('TFrame', background='red')
        # creating a background
        self.back_grod = PhotoImage(file='img_window1/rsz_rdblu4.gif')
        self.img_label = ttk.Label(self.frame_bodys, image=self.back_grod)
        self.img_label.place(x=0, y=0)

        # creating a label and entry
        self.emo=emoji.emojize(":unlocked:")
        self.label_head = ttk.Label(self.frame_headers, text=str(self.emo)+"   DECRYPTION!!!  ", font=('Showcard Gothic', 23, 'bold'),
                                    style='header.TLabel')
        self.img_header = PhotoImage(
            file='img_window1/rsz_window2_back.gif').subsample(2, 2)
        self.img_header_ = ttk.Label(self.frame_headers, image=self.img_header)

        self.label_decrypt = ttk.Label(self.frame_bodys, text="Text:", font='Stencil', style='body.TLabel')
        self.label_key = ttk.Label(self.frame_bodys, text="Key:", font='Stencil', style='body.TLabel')
        self.label_decrypted = ttk.Label(self.frame_bodys, text="DECRYPTED text:", font='Stencil', style='body.TLabel')

        self.entry_decrypt = Entry(self.frame_bodys, width=20, font='Georgia',bg='#783af2',fg='#000000')
        self.entry_key = Entry(self.frame_bodys, width=20,  font='Georgia',bg='#783af2',fg='#000000')
        self.entry_decrypted = ttk.Entry(self.frame_bodys, width=20 , font='Georgia', state="disabled",style="body.TLabel")

        # creating images for btn
        self.generate_img = PhotoImage(file='img_window1/generate.gif').subsample(2,
                                                                                                                      2)
        self.clear_img = PhotoImage(file='img_window1/rsz_reset.gif').subsample(2,
                                                                                                                    2)
        self.save_img = PhotoImage(file='img_window1/save.gif').subsample(2, 2)
        self.back_img = PhotoImage(file='img_window1/back btn.gif').subsample(2, 2)

        # creating a button
        self.decrypt_btn = Button(self.frame_bodys, text="Generate", bg='red', fg='white', command=self.decryption_
                                  , image=self.generate_img, compound=RIGHT, activebackground='#8800d6')
        self.clear_btn = Button(self.frame_bodys, text="Clear", bg='red', fg='white', command=self.clear_
                                , image=self.clear_img, compound=RIGHT, activebackground='#8800d6'
                                )
        self.save_btn = Button(self.frame_bodys, text="Save", bg='red', fg='white', command=self.save_,
                               image=self.save_img, compound=RIGHT, activebackground='#8800d6')
        self.back_btn = Button(self.frame_bodys, text="Back", bg='red', fg='white', command=self.back_,
                               activebackground='#8800d6')

        # creating a hover for button
        self.decrypt_btn.bind("<Enter>", self.hover_enter_decrypt)
        self.decrypt_btn.bind("<Leave>", self.hover_leave_decrypt)

        self.clear_btn.bind("<Enter>", self.hover_enter_clear)
        self.clear_btn.bind("<Leave>", self.hover_leave_clear)

        self.save_btn.bind("<Enter>", self.hover_enter_save)
        self.save_btn.bind("<Leave>", self.hover_leave_save)

        self.back_btn.bind("<Enter>", self.hover_enter_back)
        self.back_btn.bind("<Leave>", self.hover_leave_back)

        # griding and packing   command=self.back_
        self.frame_headers.pack()
        self.frame_bodys.pack()

        self.label_head.grid(row=0, column=0)
        self.img_header_.grid(row=0, column=1)
        #      self.label_design.grid(row=1)

        self.label_decrypt.grid(row=0, column=0, padx=20, pady=20)
        self.label_key.grid(row=1, column=0, padx=20, pady=20)
        self.label_decrypted.grid(row=5, column=0, padx=5, pady=5, ipadx=4,ipady=5, sticky='w')

        self.entry_decrypt.grid(row=0, column=1, padx=20, pady=20)
        self.entry_key.grid(row=1, column=1, padx=20, pady=20)
        self.entry_decrypted.grid(row=5, column=1, padx=5, pady=5, sticky='w')
        #     self.label_design.grid(row=2, columnspan=3, padx=20, pady=5)
        #    self.label_design1.grid(row=4, columnspan=3, padx=20, pady=5)

        self.decrypt_btn.grid(row=3, column=1, padx=5, pady=10, sticky='n')
        self.clear_btn.grid(row=3, column=1, padx=5, pady=10, sticky='e')
        self.save_btn.grid(row=3, column=0, padx=50, pady=10, sticky='e')
        self.back_btn.grid(row=3, column=0, padx=5, pady=10, sticky='w')

    def decryption_(self):
        print("decrypting part")
        self.a = self.entry_decrypt.get()
        self.b = str(self.entry_key.get())
        self.b_ck = self.b.isdigit()
        if self.b_ck != True:
            messagebox.showerror(title="Invalid Option", message="Enter a number between 1 to 49!")
        if (self.a == ''):
            messagebox.showinfo(title="Entry error", message="Please enter the text!")
            self.master_decry.tkraise()
        if (self.b == ''):
            messagebox.showinfo(title="Entry error", message="Please enter the key!")
            self.master_decry.tkraise()

        if self.a != '':
            if self.b != '':
                self.entry_decrypted.configure(state="enabled")


        self.c = decryption_form.decrypt_(self.a, self.b)
        self.d = self.entry_decrypted.insert(0, self.c)

        DB_encryption.Decryption_values(self.a, self.b, self.c)

    def clear_(self):
        print("cleared")
        self.entry_decrypt.delete(0, END)
        self.entry_key.delete(0, END)
        self.entry_decrypted.delete(0, END)
        self.entry_decrypted.configure(state="disabled")

    def save_(self):
        print("successfully saved!")
        self.file = filedialog.asksaveasfile(defaultextension='.txt',
                                             filetypes=[("Text file", ".txt"), ("Html file", ".html"),
                                                        ("all files", ".*")])
        self.tim = str(datetime.datetime.now())
        self.filetext_decrypt = str(self.entry_decrypt.get())
        self.filetext_decrypted = str(self.entry_decrypted.get())
        self.file.write("DECRYPTING TEXT:")
        self.file.write('\n')
        self.file.write(self.filetext_decrypt)
        self.file.write('\n')
        self.file.write('DECRYPTED TEXT:')
        self.file.write('\n')
        self.file.write(self.filetext_decrypted)
        self.file.write('\n')
        self.file.write(self.tim)
        self.file.close()

    def back_(self):
        self.master_decry.destroy()

        # creating a function for hover

    def hover_enter_decrypt(self, event):
        self.decrypt_btn["bg"] = "blue"

    def hover_leave_decrypt(self, event):
        self.decrypt_btn["bg"] = "red"

    def hover_enter_clear(self, event):
        self.clear_btn["bg"] = "blue"

    def hover_leave_clear(self, event):
        self.clear_btn["bg"] = "red"

    def hover_enter_save(self, event):
        self.save_btn["bg"] = "blue"

    def hover_leave_save(self, event):
        self.save_btn["bg"] = "red"

    def hover_enter_back(self, event):
        self.back_btn["bg"] = "blue"

    def hover_leave_back(self, event):
        self.back_btn["bg"] = "red"


def main():
    print("hello here we are going to use tkinter!!")
    root = Tk()
    log = Login(root)
    root.mainloop()


if __name__ == '__main__':
    main()

