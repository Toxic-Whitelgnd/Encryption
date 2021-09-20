import pyrebase,requests
from tkinter import messagebox
import smtplib
from email.message import EmailMessage
import random,emoji


firebaseConfig = {
  'apiKey': "AIzaSyCuvYXMKrZVJh0UjI5xZjgXL6zJnzt_9mM",
  'authDomain': "encrypyfb.firebaseapp.com",
  'projectId': "encrypyfb",
  'storageBucket': "encrypyfb.appspot.com",
  'messagingSenderId': "245378921082",
  'appId': "1:245378921082:web:147146504bf3f6147141c3",
  'measurementId': "G-RYC643NLVZ",
    'databaseURL':"https://encrypyfb-default-rtdb.firebaseio.com/"
}
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth=firebase.auth()
storage=firebase.storage()

#here we are using db!!
#this is for signup
def username_input(usr,password,emailid):
    while True:
        try:
            a = db.child("Logininfo").child(usr).get().val()
            print(type(a))
            b = a['username']
            print(type(b))
            if usr == b:
                print("username already exixted")
                messagebox.showinfo(title="Username Exist!",message="Try another user name!!!")
                return 0
            break
        except TypeError:
            insert_data(usr,password,emailid)
            return 1
        

#need to code here for checking the username!!!!
def insert_data(usr,password,emailid):
    data = {
        'username': usr, 'password': password, 'emailid': emailid

    }
    db.child("Logininfo").child(usr).set(data)  # child is the table name another child name for own id
    print("created")


#thiss is for passing the verification for the signup
def getting_data(usrname,passwordd):
    login = db.child("Logininfo").child(usrname).get().val()
    print(usrname)
    login_pass=login['password']
    print(login_pass)
    if login_pass == passwordd:
        print("fuked up")
        c=db.child("Logininfo").child(usrname).get().val()
        d=c['emailid']
        print(d)
        #we will call this to the smpt fuction to send the otp!!
        otp_through1_mail(d)

    else:
        print("mffff")

#this is for otp to mail at signup side
def otp_through1_mail(usr_mail):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)  #default port server for sending mails 587
    #WHEN U USE SMPT_SSL PORT NUMBER IS 465
   # mails=["darklgnd100@gmail.com","tarunskt5678@gmail.com"]
    global otp
    otp = random.randrange(10000, 100000)
 #   print(otp)
    print("OTP generated successfully")
    a = emoji.emojize(":check_mark:")
    a1 = emoji.emojize(":hollow_red_circle:")
    a2 = emoji.emojize(":warning:")
    a3 = emoji.emojize(":fast_reverse_button:")
    a4 = emoji.emojize(":fast-forward_button:")
    a5 = emoji.emojize(":atom_symbol:")
    a6 = emoji.emojize(":love_letter:")

    msg=EmailMessage()
    msg['From']="akatsukiorganisationdev999@gmail.com"
    msg['To']=usr_mail
    msg['Subject']=str(a6)+"YOUR "+str(a1)+"TP"+str(a)
    msg.set_content("Your OTP for Encryption_app is>>\n\n\n\n\n\n\t\t\t"+str(a3)+str(otp)+str(a4)+"\n\n\n\n\n\n\n\n\n\t\t\t\t"
             "\t\t\t\n\n\n"+str(a5)+"BY-Akatsuki Organisation and "
            "Development \n\n\n\n\n-----------------------------------------------------------------\n\n")

    #login
    server.login("akatsukiorganisationdev999@gmail.com","lgrztplkwseotosn")
    server.send_message(msg)
    print("otp went successfully to your mail")

    server.quit()

#this is for otp verification
def opt_verification(usr_enters):
    r = 0

    if otp == int(usr_enters):
        print(type(usr_enters))
        print(otp)
        print("Access Granted!")
        r += 1

    else:
        print("Access Denied! or invalid code")
        print("Authentication Error!!! \n To Verify it is you Log in again!! :(\n")
    return r
#this is for login
def get_data(usr,password):
    while True:
        try:
            a=db.child("Logininfo").child(usr).get().val()
            b=a['username']
            c=a['password']
            if b == usr:
                if c == password:
                    print("successful")
                    return 1
                break
        except:
            messagebox.showinfo(title="Username Error",message="It seems u don't have Account!")
            break
#this is for verify wheter username already exsited
def check_username(user,passs,email):
    while True:
       ''' try:
            a = db.child("Logininfo").child(user).get().val()
            b = a['username']
            pass
            break'''
