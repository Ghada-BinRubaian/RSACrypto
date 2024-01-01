import random , math , rsa , base64

# to set the public key (n, e) and private key (n,e,d,p1,p2)
def SetKeys():
    key=Key_Generator()
    p1=key.generatePrime()
    p2=key.generatePrime()
    while p1==p2:
      p2=key.generatePrime()
    n=p1*p2
    z=(p1-1)*(p2-1)
    e=key.FindE(z)
    d=key.Find_D(e,z)
    while d == None :
        e=key.FindE(z)
        d=key.Find_D(e,z)
    return p1,p2,n,z,e,d 
#to open the plainText or CipherText
def openfile(fileName):
  try:
    with open(fileName,'rb') as file:
      filecontent=file.read()
    stringFormat=filecontent.decode()
    return stringFormat
  except Exception as e:
    print(f"Error happened in openfile method : {e}")

#to write on file the plainText or CipherText 
def writetoFile(text,flag):
  bytetext=str(text).encode()
  file=f'RsaCryptoText{flag}.txt'
  try:
    with open(file,'wb')as file:
      file.write(bytetext)
  except Exception as e:
    print(f"Error happened in writetoFile {e}")

#encrypt text first by calling openfile to get the plainText ,
# then convert it to list of integers to calculate  ciphered = message^e mod n
# then take the string representation of ciphered then convert it to base64
def encryption(text,e,n):
    textInString=openfile(text)
    plain_int=[ord(char) for char in textInString]
    cipher_int=[pow(i ,e,n) for i in plain_int]
    cipherText=''.join(chr(i) for i in cipher_int)
    cipherText_base64=base64.b64encode(cipherText.encode("utf-8")).decode()
    #take a random number to produce multiple files each time run encryption , so we donot the overwrite the new text in old files 
    #e.g : RsaCryptoTextEncrypt1.txt, RsaCryptoTextEncrypt2.txt , RsaCryptoTextEncrypt3.txt,....
    version=random.randint(1,10)
    Encrypt=f'Encrypt{version}'
    writetoFile(cipherText_base64,Encrypt)
    print(f"The encrypted Text saved in RsaCryptoTextEncrypt{version}.txt")

# secrypt text first by calling openfile to get the CipherText ,
#then decode the base64 cipherText , convert it to list of integers to calculate message=ciphered^d mod n 
# then take the string representation of message
def decryption (CipherText,d,n):
    textInString=openfile(CipherText)
    encryptedText = base64.b64decode(textInString).decode("utf-8")
    int_encryptedText = [ord(char) for char in encryptedText]
    int_plainText = [pow(i, d, n) for i in int_encryptedText]
    plainText = ''.join(chr(i) for i in int_plainText)
    #take a random number to produce multiple files each time run decryption , so we donot the overwrite the new text in old files 
    #e.g : RsaCryptoTextDecrypt1.txt, RsaCryptoTextDecrypt2.txt , RsaCryptoTextDecrypt3.txt,....
    version=random.randint(1,10)
    Decrypt=f'Decrypt{version}'
    writetoFile(plainText,Decrypt)
    print(f"The decrypted Text saved in RsaCryptoTextDecrypt{version}.txt")

#function to extract the public key (n, e) private key (n,e,d,p1,p2) from .pem publicKey and privateKey files 
def  InportKeysFromPEM(publicfile, privatefile):
    #publicKey, privateKey
    try:
     if(publicfile!=None):
        with open(publicfile,'rb') as pubfile:
          publicKey=rsa.PublicKey.load_pkcs1(pubfile.read(),  "PEM")
     if(privatefile!=None):
      with open(privatefile,'rb') as prifile:
       privateKey=rsa.PrivateKey.load_pkcs1(prifile.read(), "PEM")
     else:
        raise("could not find keys")
     n , e = publicKey.n,publicKey.e
     p1, p2=privateKey.p , privateKey.q
     d=privateKey.d
     return n,e,p1,p2,d
    except Exception as e :
      print(f"Exception Happened in InportKeysFromPEM method : {e}")

#function to send the public key (n, e) private key (n,e,d,p1,p2) as .pem publicKey and privateKey files 
def ExportKeysInPEM(n,e,d,p1,p2):
    try:
    #take a random number to produce multiple files each time run ExportKeysInPEM , so we donot the overwrite the new text in old files 
    #e.g : public1.pem, private1.pem , public2.pem, private2.pem ,............
     version=random.randint(1,10)
     publicfile=f'public{version}.pem'
     privatefile=f'private{version}.pem'
     public_key=rsa.PublicKey(n,e)
     private_key=rsa.PrivateKey(n,e,d , p1, p2)

     with open(publicfile,"wb") as publicfile:
       publicfile.write(public_key.save_pkcs1('PEM'))

     with open(privatefile,"wb") as privatefile:
       privatefile.write(private_key.save_pkcs1('PEM'))
    except Exception as e :
      print(f"Exception happened in ExportKeysInPEM method : {e}") 

#class contain all the required method to calculate the public key and private key    
class Key_Generator():
  
  def FindE(self,z):
   E=random.randint(3,z-1)
   while math.gcd(E,z) != 1.0:
      E=random.randint(3,z-1)
   return E

# generate value for [d](multi-inverse of e) 
  def Find_D(self,e,z):
   for d in range(3,z):
     if ((d*e) % z) == 1.0  and d!=e :
        return d
  
#function to check if it prime number 
  def is_Prime(self,num):
    if num<2 : 
     return False
    for i in range(2, int(math.sqrt(num))+1):
     if num%i==0:
       return False
    return True 
#generate a prime number
  def generatePrime(self):
      p=random.randint(409, pow(10,3))
      while not self.is_Prime(p):
        p=random.randint(409,pow(10 , 3))
      return p
  












