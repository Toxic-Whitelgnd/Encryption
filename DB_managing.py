from email import message
import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(host="localhost",user="Akatsuki",password="itachi*",database="login_signup")
cursor=mydb.cursor()


def insert_func(usr1,passkey1,mail1):
    r=0
    usr_name = "INSERT INTO Login (username,password,emailid) VALUES(%s,%s,%s)"
    pass_word = (usr1,passkey1,mail1)
    cursor.execute(usr_name, pass_word)
    mydb.commit()
    print("inserted successfully")
    r += 1
    print(r)
    return r 
  
def insert_data(usr,passkey,mail):
      while True:
        try:
            insert_func(usr,passkey,mail)
            break
        except  Exception :
            print("USERNAME ALREADY EXISTED")
            messagebox.showerror(title="exixst",message="try another username")

            break        
              