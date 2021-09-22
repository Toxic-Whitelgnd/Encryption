import datetime

import pyrebase

firebaseConfig = {
  'apiKey': "",
  'authDomain': "",
  'projectId': "",
  'storageBucket': "",
  'messagingSenderId': "",
  'appId': "",
  'measurementId': "",
    'databaseURL':""
  #i removed due to privacy
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



