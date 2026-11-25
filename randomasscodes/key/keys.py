from cryptography.fernet import Fernet
key=Fernet.generate_key()
#with open("mykey.key","wb") as mykey:
#   mykey.write(key)

with open("mykey.key","rb") as mykey:
    key=mykey.read()
print(key)
f=Fernet(key)
#with open("gaything.txt","rb") as originalf:
#    original=originalf.read()
#encrypted=f.encrypt(original)
#with open("enc_gay.crp","wb") as enc_file:
#     enc_file.write(encrypted)
with open('enc_gay.crp',"rb") as enc_file:
    encrypted=enc_file.read()

decrypted=f.decrypt(encrypted)
with open("der_gay.txt","wb") as decryptedf:
    decryptedf.write(decrypted)