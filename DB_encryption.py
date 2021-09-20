import datetime

import pyrebase

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

def Encryption_values(Enc_txt,key,Encrypted_txt):
  data={
    'enc_txt':Enc_txt,
    'key_val':key,
    'encrpt_txt': Encrypted_txt
  }
  db.child("Encrypted_part").child(Enc_txt).set(data)

def Decryption_values(Dec_txt,key,Decryptr_txt):
  data={
    'dec_txt':Dec_txt,
    'key_val': key,
    'Decrpt_txt':Decryptr_txt
  }
  db.child("Decrypted_part").child(Dec_txt).set(data)



