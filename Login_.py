from email import message
from tkinter import *
from tkinter import ttk,messagebox,filedialog
import tkinter as tk
import Login_Db,DB_managing
import re,sys,datetime
import encryption_form,decryption_form


print(sys.getrecursionlimit())
#sys.setrecursionlimit(1000)
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
#this is not correct method and it is in under xdevelopment  
#need to add images for login and signup window!!  XD

class Login(tk.Tk):
    def __init__(self,master) -> None:
    
        self.master=master
        self.master.resizable(False, False)
        self.master.geometry("300x360")
        
        
        #creating a frame to hold
        self.frame_header=ttk.Frame(self.master)
        self.fram_body=ttk.Frame(master=self.master,relief=SOLID) 

        #creating a label
        self.login_header_label=ttk.Label(self.frame_header,text=" LOGIN  |  SIGNUP ",font=('Arial',22,'bold'))
        self.username_label=ttk.Label(self.fram_body,text="Username:")
        self.password_label=ttk.Label(self.fram_body,text="Password:")

        #creating a entry
        self.usr_entry=ttk.Entry(self.fram_body, width=20)
        self.pass_entry=ttk.Entry(self.fram_body, width=20)

        #cretinf buttons
        self.login_btn = ttk.Button(self.fram_body,text="Login",command=self.login_btn_com)
        self.clear_btn = ttk.Button(self.fram_body,text="Clear",command=self.clear_btn_com)
        self.signup_btn = ttk.Button(self.fram_body,text="Signup",command=self.signup_btn_com)
        self.quit_btn  = ttk.Button(self.fram_body,text="Quit",command=self.quit_btn_com)



        #creating for griding and packing
        self.frame_header.pack()
        self.fram_body.pack()

        self.login_header_label.grid(row=0,columnspan=2,padx=5,pady=20,ipadx=5,ipady=5)
        self.username_label.grid(row=0,column=0,padx=30,pady=30,ipadx=5,ipady=5,sticky='w')
        self.password_label.grid(row=1,column=0,padx=30,pady=30,ipadx=5,ipady=5,sticky='w')

        self.usr_entry.grid(row=0,column=1,padx=5,pady=5,ipadx=5,ipady=5)
        self.pass_entry.grid(row=1,column=1,padx=5,pady=5,ipadx=5,ipady=5)

        self.login_btn.grid(row=2,column=0,padx=5,pady=5,ipadx=2,ipady=2)
        self.clear_btn.grid(row=2,column=1,padx=5,pady=5,ipadx=2,ipady=2)
        self.signup_btn.grid(row=3,column=0,padx=5,pady=10,ipadx=5)
        self.quit_btn.grid(row=3,column=1,padx=5,pady=10,ipadx=5)

       # w, h =self.master.winfo_screenwidth(),self.master.winfo_screenheight()
       # print(w,h)

    def login_btn_com(self):
        print("Logging u in!")
        self.usr_name=self.usr_entry.get()
        self.usr_pass=self.pass_entry.get()
        print(self.usr_name,self.usr_pass)
        if self.usr_name == '':
            print("checking for username entered or not")
            messagebox.showinfo(title="Login error!",message="Please enter your username!!")
        if self.usr_pass == '':  
            print("checking for password entered or not!")
            messagebox.showinfo(title="Login error!",message="Please enter your password!")  
        self.auth=Login_Db.get_data(self.usr_name,self.usr_pass)  #need to change here
        print(self.auth)  #need to change here
     #   self.auth1=[]
     #   self.auth1 +=self.auth
        print([self.usr_name,self.usr_pass])
        if self.auth == 1:
            messagebox.showinfo(title="LOGIN",message="Login successfull!!")
            self.encryption_window=Toplevel(self.master)
            self.log3=Encrypt_Decrypt(self.encryption_window)
            self.master.iconify()
            
            
        else:
            messagebox.showinfo(title="LOGIN",message="Login unsuccessfull!!")    

        

        self.clear_btn_com()

    def signup_btn_com(self):

    #    for x in self.fram_body.winfo_children():
     #       x.destroy()
     #   for y in self.frame_header.winfo_children():
      #      y.destroy()
        #   self.fram_body.pack_forget()
      #  self.frame_header.pack_forget()
        print("Siginning u in!!")
        self.new_window=Toplevel(self.master)
        self.log = signup_window(self.new_window)
        self.master.iconify()
    
    def clear_btn_com(self):
        print("cleared")
        self.usr_entry.delete(0,END)
        self.pass_entry.delete(0,END)
       

    def  quit_btn_com(self):
        self.master.quit()
   
class signup_window():
    def __init__(self, master) -> None:


        self.master_sign=master
        
        
        self.master_sign.geometry("400x430")

        #creaeting a frame
        self.frame_header=ttk.Frame(self.master_sign,relief=SOLID)
        self.frame_body=ttk.Frame(self.master_sign,relief=RIDGE)
        
        #creating a labels
        #for header
        self.header_label=ttk.Label(self.frame_header,text="|  Signup  |",font=('Arial',22,'bold'))

        #for body
        self.user_input=ttk.Label(self.frame_body,text="Enter your username, Password  Email id for signup",font=('Arial',11,'bold'))
        self.username_label=ttk.Label(self.frame_body,text="Username:")
        self.password_label=ttk.Label(self.frame_body,text="Password:")
        self.email_label=ttk.Label(self.frame_body,text="Email:")
        
        #entry field
        self.usr_entry=ttk.Entry(self.frame_body, width=20)
        self.pass_entry=ttk.Entry(self.frame_body, width=20)
        self.email_entry=ttk.Entry(self.frame_body, width=20)

        #creating buttons
        self.signup_btn=ttk.Button(self.frame_body,text="Signup",command=self.signup_btn_com_nw)
        
        self.clear_btn = ttk.Button(self.frame_body,text="Clear",command=self.clear_btn_com_nw)
        self.back_btn  = ttk.Button(self.frame_body,text="Back",command=self.back_btn_com)
        


        #griding and packing
        self.frame_header.pack()
        self.frame_body.pack()

        self.header_label.grid(row=0,columnspan=2)

        self.user_input.grid(row=0,columnspan=2,padx=10,pady=20,ipady=3,ipadx=3)

        self.username_label.grid(row=1,column=0,padx=5,pady=5,ipadx=3,ipady=3)
        self.password_label.grid(row=2,column=0,padx=5,pady=5,ipadx=3,ipady=3)
        self.email_label.grid(row=3,column=0,padx=5,pady=5,ipadx=3,ipady=3)

        self.usr_entry.grid(row=1,column=1,padx=20,pady=25,ipadx=3,ipady=3)
        self.pass_entry.grid(row=2,column=1,padx=20,pady=25,ipadx=3,ipady=3)
        self.email_entry.grid(row=3,column=1,padx=20,pady=25,ipadx=3,ipady=3)

        self.clear_btn.grid(row=4,column=1,padx=5,pady=5,ipadx=3,ipady=3)
        self.signup_btn.grid(row=4,column=0,padx=5,pady=5,ipadx=3,ipady=3,sticky='ne')
        self.back_btn.grid(row=5,columnspan=2,padx=5,pady=10,ipadx=5)
        

        

    def signup_btn_com_nw(self):   
        self.usr=self.usr_entry.get() 
        self.password=self.pass_entry.get()
        self.email=self.email_entry.get()
        if self.usr == '':
            messagebox.showinfo(title="Signup error",message="Enter your username!")
            
        if self.password == '':
            messagebox.showinfo(title="Signup error",message="Enter your Password!")
            
        if self.email == '':
            messagebox.showinfo(title="Signup error",message="Enter your email!")
            
        else:
            self.a=checkmail(self.email)  
        if self.a != 1:
            messagebox.showerror(title="Email error",message="Check  your email! please")
        else:
            DB_managing.insert_data(self.usr,self.password,self.email) 
            messagebox.showinfo(title="SIGNED UP|SUCCESFULLY",message="one more step to verify u!")
            Login_Db.signup_mail(self.usr,self.password)
            self.otp_window=Toplevel(self.master_sign)
            self.log = otp_window_(self.otp_window) 




        self.master_sign.tkraise()
        self.clear_btn_com_nw()

 

    def clear_btn_com_nw(self):
        self.usr_entry.delete(0,END)
        self.pass_entry.delete(0,END)
        self.email_entry.delete(0,END)

    def back_btn_com(self):
        self.master_sign.destroy()    
       
    #    self.master.geometry("%dx%d+0+0" % (w, h)) 
        
class otp_window_():
    def __init__(self,master) -> None:
        self.master_otp=master
        self.master_otp.geometry("360x300")
        self.otp_cont=ttk.Frame(self.master_otp,relief=GROOVE)
        #creatin labels
        self.label_header=ttk.Label(self.otp_cont,text="OTP | VERIFICATION",font=('Arial',22,'bold'))

        self.otp_label=ttk.Label(self.otp_cont,text="Enter yout 5 digit otp send to your eregistered email!",font=('Arial',10,'bold'))

        #creating entry
        self.otp_cont.pack()
        self.otp_entry=ttk.Entry(self.otp_cont,width=20)

        #creatin buttons
        self.otp_btn=ttk.Button(self.otp_cont,text="Verify",command=self.verify)

        #gridding
        self.label_header.grid(row=0,column=0,padx=20,pady=20,ipadx=3,ipady=1)
        self.otp_label.grid(row=1,column=0,padx=20,pady=20,ipadx=3,ipady=1)
        self.otp_entry.grid(row=2,column=0,padx=20,pady=20,ipadx=3,ipady=1)
        self.otp_btn.grid(row=3,column=0,padx=30,pady=30,ipadx=5,ipady=1)
    
    def verify(self):
        self.otp_value=self.otp_entry.get()
        self.otp_verify1=int(self.otp_value)
        self.otp_verify=Login_Db.opt_verification(self.otp_verify1)
        if self.otp_verify == 1:
            messagebox.showinfo(title="OTP | SUCCESSFULL",message="Your entered otp is correct!!")
            self.master_otp.destroy()
        else:
            messagebox.showerror (title="OTP | UNSUCCESSFULL",message="Please check your otp!!")
            
def checkmail(email):
    print(email)
    if(re.search(regex,email)):   
        print("Valid Email")   #need to return and show in mesageg box
        return 1
    else:   
        print("Invalid Email")  

class Encrypt_Decrypt(Login):
    def __init__(self,master):
        self.master_ed = master
        self.master_ed.resizable(False, False)
        self.frame = ttk.Frame(self.master_ed).pack()
        self.master_ed.geometry("640x520")
        self.master_ed.title("#selection#")

        #crreating a styles for window2
        self.style=ttk.Style()

        self.style.configure('frame_header.TLabel',background='black')
        self.style.configure('frame_body.TLabel',background='#24e34a')

        self.style.configure('frame_body1.TButton',background='#24e34a')
        self.style.configure('frame_body1.TButton', background='#24e34a')
        self.style.configure('frame_body1.TButton', background='#24e34a')




        #start code here

        self.frame_header = ttk.Frame(self.master_ed)

        self.frame_body = ttk.Frame(self.master_ed,style='frame_body.TLabel')

        #using images

        self.encr_img=PhotoImage(file="C:/Users/HOME/VSCODE/Encryption_app/img_window1/rsz_1rsz_heade_back.gif") #make the header with aa diagram
        self.imf_header=ttk.Label(self.frame_header,image=self.encr_img)
        self.imf_header.grid(row=0,column=1)
        self.back_grod = PhotoImage(file='C:/Users/HOME/VSCODE/Encryption_app/img_window1/rsz_wallpaperflarecom_wallpaper.gif')
        self.img_label = ttk.Label(self.frame_body, image=self.back_grod)
        self.img_label.place(x=0, y=0)


        self.label_header = ttk.Label(self.frame_header,style='frame_header.TLabel',text="ENCRYPTION AND DECRYPTION"
                                      , font=('Arial', 20, 'bold'),foreground='Red')


        self.label_design = ttk.Label(self.frame_header, text="       ------------------------------------------------------ "
                                                              "       ---------------------------------------- "
                                      ,background='black',foreground='red')

        self.label_content=ttk.Label(self.frame_body,style='frame_body.TLabel',text="     Select the option that   "
                                    "the operation that u have to perform !     ",font=(
            'Arial',16),foreground='red',background='black')

        #creating a images for buttons and configuration!

        self.btn_encryp=PhotoImage(file='C:/Users/HOME/VSCODE/Encryption_app/img_window1/rsz_download.gif')
        self.btn_decryp = PhotoImage(file='C:/Users/HOME/VSCODE/Encryption_app/img_window1/rsz_download_1.gif')
        self.btn_quit = PhotoImage(file='C:/Users/HOME/VSCODE/Encryption_app/img_window1/rsz_qiut.gif')

        #creating a button for encryption and decryption
        self.encry_btn=Button(self.frame_body,text="ENCRYPTION",bg='#00f024',fg='white',activebackground='red'
                    ,image=self.btn_encryp,padx=4,compound=RIGHT,command=self.encrypt,font='Ravie')
        self.decry_btn = Button(self.frame_body, text="DECRYPTION", bg='#29bf23', fg='white',command=self.decrypt
                      ,image=self.btn_decryp,padx=4,compound=RIGHT, activebackground='red',font='Ravie')
        self.quit = Button(self.frame_body, text="QUIT", bg='#0a6e06', fg='white', activebackground='#d400a2',
                   image=self.btn_quit,padx=5,compound=RIGHT,command=self.quit_,font='Ravie',cursor="pirate")

        #creating about label

        
        self.abt=ttk.Label(self.frame_body,text="Developed by:- "
                                                "  Akatsuki Organisation and development   ",font='Ravie',background='black',foreground='red')
        #self.name=self.usr_name                                        
        #self.usr_label=ttk.Label(self.frame_body,text=self.name,font='Ravie',background='black',foreground='red')                                       


        #creating a hover structure
        self.encry_btn.bind("<Enter>",self.hover_enter_encryp)
        self.encry_btn.bind("<Leave>",self.hover_leave_encryp)

        self.decry_btn.bind("<Enter>", self.hover_enter_decryp)
        self.decry_btn.bind("<Leave>", self.hover_leave_decryp)

        self.quit.bind("<Enter>", self.hover_enter_quit)
        self.quit.bind("<Leave>", self.hover_leave_quit)


        #gridding
        self.frame_header.pack()
        self.frame_body.pack()


        self.label_header.grid(row=0, column=0)
        self.label_design.grid(row=1, column=0)
        self.label_content.grid(row=0,column=0)

        self.encry_btn.grid(row=1,column=0,padx=0,pady=40,ipadx=5,ipady=5)
        self.decry_btn.grid(row=2, column=0, padx=0, pady=40,ipadx=5,ipady=5)
        self.quit.grid(row=3, column=0, padx=0, pady=40,ipadx=5,ipady=5)

        self.abt.grid(row=4,column=0,padx=4)
      #  self.usr_label.place(x=6,y=350)

    def quit_(self):
        self.master_ed.quit()
    


    def encrypt(self):
        self.enc = Toplevel(self.master_ed)
        self.app = encryption(self.enc)

    def decrypt(self):
        self.dec = Toplevel(self.master_ed)
        self.app = decryption(self.dec)

    #creating a hover function
    def hover_enter_encryp(self,event):
        self.encry_btn["bg"]="#00ff12"
    def hover_leave_encryp(self,event):
        self.encry_btn["bg"]="#29bf23"

    def hover_enter_decryp(self,event):
        self.decry_btn["bg"]="#00ff12"
    def hover_leave_decryp(self,event):
        self.decry_btn["bg"]="#00ad1a"

    def hover_enter_quit(self,event):
        self.quit["bg"]="#00ff12"
    def hover_leave_quit(self,event):
        self.quit["bg"]="#0a6e06"

class encryption():
    def __init__(self,master):
        print("encryption part entered")
        self.master_encryp=master
        self.master_encryp.geometry("410x280")
        self.master_encryp.resizable(False, False)
        self.master_encryp.title("#Encryption#")


        #creating a label and entry for the encryption
        self.frame_header=ttk.Frame(self.master_encryp)
        self.frame_body = ttk.Frame(self.master_encryp)

        #creating a background
        self.back_grod = PhotoImage(file='C:/Users/HOME/VSCODE/Encryption_app/img_window1/rsz_rdblu4.gif')
        self.img_label = ttk.Label(self.frame_body, image=self.back_grod)
        self.img_label.place(x=0, y=0)

        #creating a styles\
        self.style=ttk.Style()
        self.style.configure("body.TLabel",background='#783af2')
        self.style.configure("design.TLabel",background='#1e0257')
        self.style.configure("header.TLabel",background='blue')
        self.style.configure('TFrame',background='red')

        #creasting icon\
        self.master_encryp.iconbitmap('C:/Users/HOME/VSCODE/Encryption_app/img_window1/data-encryption-32.ico')


        #creating a label and entry
        self.label_head=ttk.Label(self.frame_header,text="ENCRYPTION!!!",font=('Showcard Gothic',20,'bold'),style='header.TLabel')
        self.img_header=PhotoImage(file='C:/Users/HOME/VSCODE/Encryption_app/img_window1/rsz_window2_back.gif').subsample(2,2)
        self.img_header_=ttk.Label(self.frame_header,image=self.img_header)

    #    self.label_design=ttk.Label(self.frame_header,text='---------------------------------------------------------' )

        self.label_encrypt=ttk.Label(self.frame_body,text="Text:",style='body.TLabel',font='Stencil')
        self.label_key = ttk.Label(self.frame_body,text="Key:",style='body.TLabel',font='Stencil')
        self.label_encrypted = ttk.Label(self.frame_body,text="Encryted text:",style='body.TLabel',font='Stencil')

        self.entry_encrypt=ttk.Entry(self.frame_body,width=20,font='Georgia')
        self.entry_key = ttk.Entry(self.frame_body, width=20,font='Georgia')
        self.entry_encrypted = ttk.Entry(self.frame_body, width=20,font='Georgia',state="disabled")

        #self.label_design = ttk.Label(self.frame_body, text='-----------------------------------------------------')
  #      self.label_design1 = ttk.Label(self.frame_body,
   #                                  text='--------------------------------------------------------------------')

        #creating a images for butn
        self.generate_img = PhotoImage(file='C:/Users/HOME/VSCODE/Encryption_app/img_window1/generate.gif').subsample(2, 2)
        self.clear_img = PhotoImage(file='C:/Users/HOME/VSCODE/Encryption_app/img_window1/rsz_reset.gif').subsample(2, 2)
        self.save_img = PhotoImage(file='C:/Users/HOME/VSCODE/Encryption_app/img_window1/save.gif').subsample(2, 2)
        self.back_img = PhotoImage(file='C:/Users/HOME/VSCODE/Encryption_app/img_window1/back btn.gif').subsample(2, 2)

        #creating a button
        self.encrypt_btn=Button(self.frame_body,text="Generate",command=self.encryption_,bg='red',fg='white',padx=10
                                ,image=self.generate_img,compound=RIGHT,activebackground='#8800d6')
        self.clear_btn = Button(self.frame_body, text="Clear", bg='red',command=self.clear_, fg='white'
                                ,image=self.clear_img,compound=RIGHT,activebackground='#8800d6')
        self.save_btn = Button(self.frame_body, text="Save", bg='red',command=self.save_, fg='white'
                               ,image=self.save_img,compound=RIGHT,activebackground='#8800d6')
        self.back_btn = Button(self.frame_body, text="Back", bg='red', fg='white',command=self.back_,activebackground='#8800d6')
        #creating a hover for button
        self.encrypt_btn.bind("<Enter>",self.hover_enter_encrypt)
        self.encrypt_btn.bind("<Leave>", self.hover_leave_encrypt)

        self.clear_btn.bind("<Enter>", self.hover_enter_clear)
        self.clear_btn.bind("<Leave>", self.hover_leave_clear)

        self.save_btn.bind("<Enter>", self.hover_enter_save)
        self.save_btn.bind("<Leave>", self.hover_leave_save)

        self.back_btn.bind("<Enter>", self.hover_enter_back)
        self.back_btn.bind("<Leave>", self.hover_leave_back)



        #griding and packing
        self.frame_header.pack()
        self.frame_body.pack()

        self.label_head.grid(row=0,column=0)
        self.img_header_.grid(row=0, column=1)
   #     self.label_design.grid(row=1,columnspan=2)

        self.label_encrypt.grid(row=0, column=0,padx=20,pady=20)
        self.label_key.grid(row=1, column=0,padx=20,pady=20)
        self.label_encrypted.grid(row=6, column=0,padx=5,pady=5,ipadx=4,ipady=5,sticky='w')

        self.entry_encrypt.grid(row=0, column=1,padx=20,pady=20)
        self.entry_key.grid(row=1, column=1, padx=20, pady=20)
        self.entry_encrypted.grid(row=6, column=1, padx=5, pady=5,sticky='sw')
    #    self.label_design.grid(row=2,columnspan=3,padx=20,pady=5)   .grid(row=6, column=1, padx=5, pady=5,sticky='sw')
     #   self.label_design1.grid(row=4, columnspan=3, padx=20, pady=5)

        self.encrypt_btn.grid(row=3,column=1,padx=5,pady=10,sticky='n')
        self.clear_btn.grid(row=3, column=1, padx=5, pady=10,sticky='e')
        self.save_btn.grid(row=3, column=0, padx=50, pady=10,sticky='e')
        self.back_btn.grid(row=3, column=0, padx=5, pady=10, sticky='w')
    def encryption_(self):
        print("encrypting part")
        self.a = self.entry_encrypt.get() #need to check the text has been given or not
        self.b = str(self.entry_key.get())
       

        if self.a == '':
            messagebox.showinfo(title="Entry error",message="Enter your encrypt text")
            self.master_encryp.tkraise()
        if self.b == '':
            messagebox.showinfo(title="Entry error",message="Enter your key")   
            self.master_encryp.tkraise() 

        if self.a != '':
            if self.b != '':
                self.entry_encrypted.configure(state="enabled")

        self.c = encryption_form.encrypt_(self.a,self.b)
        self.d = self.entry_encrypted.insert(0,self.c)
        self.master_encryp.tkraise()

        



    def clear_(self):
        print("cleared")
        self.entry_encrypt.delete(0,END)
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

    #creating a function for hover
    def hover_enter_encrypt(self,event):
        self.encrypt_btn["bg"]="blue"
    def hover_leave_encrypt(self,event):
        self.encrypt_btn["bg"]="red"

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
    def __init__(self,master):
        print("decryption part!!")
        self.master_decry = master
        self.master_decry.geometry("410x280")
        self.master_decry.resizable(False, False)
        self.master_decry.title("#Decryption#")

        # creating a label and entry for the encryption
        self.frame_headers = ttk.Frame(self.master_decry)
        self.frame_bodys = ttk.Frame(self.master_decry)

        # creasting icon\
        self.master_decry.iconbitmap('C:/Users/HOME/VSCODE/Encryption_app/img_window1/decrypted.ico')

        # creating a styles\
        self.style=ttk.Style()
        self.style.configure("body.TLabel",background='#783af2')
        self.style.configure("design.TLabel",background='#1e0257')
        self.style.configure("header.TLabel",background='blue')

        self.style.configure('TFrame',background='red')
        #creating a background
        self.back_grod = PhotoImage(file='C:/Users/HOME/VSCODE/Encryption_app/img_window1/rsz_rdblu4.gif')
        self.img_label = ttk.Label(self.frame_bodys, image=self.back_grod)
        self.img_label.place(x=0, y=0)

        # creating a label and entry
        self.label_head = ttk.Label(self.frame_headers, text="DECRYPTION!!!", font=('Showcard Gothic', 23, 'bold'),style='header.TLabel')
        self.img_header = PhotoImage(file='C:/Users/HOME/VSCODE/Encryption_app/img_window1/rsz_window2_back.gif').subsample(2, 2)
        self.img_header_ = ttk.Label(self.frame_headers, image=self.img_header)


        self.label_decrypt = ttk.Label(self.frame_bodys, text="Text:",font='Stencil',style='body.TLabel')
        self.label_key = ttk.Label(self.frame_bodys, text="Key:",font='Stencil',style='body.TLabel')
        self.label_decrypted = ttk.Label(self.frame_bodys, text="DECRYPTED text:",font='Stencil',style='body.TLabel')

        self.entry_decrypt = ttk.Entry(self.frame_bodys, width=20,font='Georgia')
        self.entry_key = ttk.Entry(self.frame_bodys, width=20,font='Georgia')
        self.entry_decrypted = ttk.Entry(self.frame_bodys, width=20,font='Georgia',state="disabled")

        #creating images for btn
        self.generate_img = PhotoImage(file='C:/Users/HOME/VSCODE/Encryption_app/img_window1/generate.gif').subsample(2, 2)
        self.clear_img = PhotoImage(file='C:/Users/HOME/VSCODE/Encryption_app/img_window1/rsz_reset.gif').subsample(2, 2)
        self.save_img = PhotoImage(file='C:/Users/HOME/VSCODE/Encryption_app/img_window1/save.gif').subsample(2, 2)
        self.back_img = PhotoImage(file='C:/Users/HOME/VSCODE/Encryption_app/img_window1/back btn.gif').subsample(2, 2)


        # creating a button
        self.decrypt_btn = Button(self.frame_bodys, text="Generate", bg='red', fg='white',command=self.decryption_
                                  , image=self.generate_img, compound=RIGHT,activebackground='#8800d6')
        self.clear_btn = Button(self.frame_bodys, text="Clear", bg='red', fg='white',command=self.clear_
                                , image=self.clear_img, compound=RIGHT,activebackground='#8800d6'
                                )
        self.save_btn = Button(self.frame_bodys, text="Save", bg='red', fg='white',command=self.save_ ,
                               image=self.save_img,compound=RIGHT,activebackground='#8800d6')
        self.back_btn = Button(self.frame_bodys, text="Back", bg='red', fg='white',command=self.back_,activebackground='#8800d6')

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
        self.img_header_.grid(row=0,column=1)
  #      self.label_design.grid(row=1)

        self.label_decrypt.grid(row=0, column=0, padx=20, pady=20)
        self.label_key.grid(row=1, column=0, padx=20, pady=20)
        self.label_decrypted.grid(row=5, column=0, padx=5, pady=5, ipadx=4, sticky='w')

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
        self.b = str (self.entry_key.get())
        if (self.a == ''):
            messagebox.showinfo(title="Entry error",message="Please enter the text!")
            self.master_decry.tkraise() 
        if (self.b == ''):
            messagebox.showinfo(title="Entry error",message="Please enter the key!")
            self.master_decry.tkraise() 
         
        if self.a != '':
            if self.b != '':
                self.entry_decrypted.configure(state="enabled")

        self.c = decryption_form.decrypt_(self.a,self.b)
        self.d = self.entry_decrypted.insert(0,self.c)


    def clear_(self):
        print("cleared")
        self.entry_decrypt.delete(0,END)
        self.entry_key.delete(0, END)
        self.entry_decrypted.delete(0, END)
        self.entry_encrypted.configure(state="disabled")

    def save_(self):
        print("successfully saved!")
        self.file = filedialog.asksaveasfile(defaultextension='.txt',
                                             filetypes=[("Text file",".txt"),("Html file",".html"),
                                                                                ("all files",".*")])
        self.tim=str(datetime.datetime.now())
        self.filetext_decrypt=str(self.entry_decrypt.get())
        self.filetext_decrypted=str(self.entry_decrypted.get())
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
    print("hello here ewe are going to use tkinter!")
    root=Tk()
    log=Login(root)
    
    
    root.mainloop()


if __name__=='__main__':
    main()    

    #line 83,84,61