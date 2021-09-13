import mysql.connector
import smtplib
from email.message import EmailMessage
import random

mydb = mysql.connector.connect(host="localhost",user="Akatsuki",password="itachi*",database="login_signup")
cursor=mydb.cursor()

'''cursor.execute("DELETE  FROM Login ")
mydb.commit()
print("succesful")'''

def get_data(usr,key):
    data="SELECT DISTINCT username,password FROM Login WHERE username=%s AND password=%s "
    val=(usr,key)
    u = 0
    cursor.execute(data,val)
    q=cursor.fetchall()
    for x in q:
        val1=[]
        val1+=val
        
        print(val1)
        if val1 == [usr,key]:
            u+=1
            # need to get from here email
            usrmail = "SELECT emailid FROM Login WHERE username=%s and password=%s"
            val = (usr, key)
            mail_usr = []
            q=0
            cursor.execute(usrmail, val)
            for i in cursor:
                q+=1
                mail_usr += i
                print(mail_usr)
                 
                
    
    if u == 1:
        print("valid authetication!!!")
        
    else:
        print("invalid authentication")
       
    return q  
                 

def otp_through1_mail(usr_mail):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)  #default port server for sending mails 587
    #WHEN U USE SMPT_SSL PORT NUMBER IS 465
   # mails=["darklgnd100@gmail.com","tarunskt5678@gmail.com"]
    global otp
    otp = random.randrange(10000, 100000)
 #   print(otp)
    print("OTP generated successfully")

    msg=EmailMessage()
    msg['From']="whitelegend56@gmail.com"
    msg['To']=usr_mail
    msg['Subject']="YOUR OTP>>>"
    msg.set_content("Your OTP for Encryption_app is>>\n\n\n\n\n\t\t\t\n"+str(otp)+"\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\n\n\nBY-Akatsuki Organisation and "
            "Development \n\n\n\n\n----------------------------------\n\n")

    #login
    server.login("whitelegend56@gmail.com","wmozuzkzyeuijuif")
    server.send_message(msg)
    print("otp went successfully to your mail")

    server.quit()


def opt_verification(usr_enters):

    r=0
   
    if otp == int(usr_enters):
        print(type(usr_enters))
        print(otp)
        print("Access Granted!")
        r+=1
        
    else:
        print("Access Denied! or invalid code")
        print("Authentication Error!!! \n To Verify it is you Log in again!! :(\n")  
    return r    

def signup_mail(usr,key):
    data="SELECT DISTINCT username,password FROM Login WHERE username=%s AND password=%s "
    val=(usr,key)
    u = 0
    cursor.execute(data,val)
    q=cursor.fetchall()
    for x in q:
        val1=[]
        val1+=val
        
        print(val1)
        if val1 == [usr,key]:
            u+=1
            # need to get from here email
            usrmail = "SELECT emailid FROM Login WHERE username=%s and password=%s"
            val = (usr, key)
            mail_usr = []
            q=0
            cursor.execute(usrmail, val)
            for i in cursor:
                q+=1
                mail_usr += i
                print(mail_usr)
                otp_through1_mail(mail_usr)
                return q