import argparse
import RsaCipher 



print("""
 _____   _____         _____                  _        
|  __ \ / ____|  /\   / ____|                | |       
| |__) | (___   /  \ | |     _ __ _   _ _ __ | |_ ___  
|  _  / \___ \ / /\ \| |    | '__| | | | '_ \| __/ _ \ 
| | \ \ ____) / ____ \ |____| |  | |_| | |_) | || (_) |
|_|  \_\_____/_/    \_\_____|_|   \__, | .__/ \__\___/ 
                                   __/ | |
                                  |___/|_|
      
      """)
print("--Credits:")
print("[*]Ghada Bin Rubaian\n[*]Muneera Alsulaiman\n[*]Asma Al Yami\n[*]Lujain Alqahtani\n[*]Dalal Alkhaldi\n")
print("->Intructor: Dr.Reem Alassaf")
print("->course:programming for CyberSecurity \n")
parser = argparse.ArgumentParser(description="Encryption and Decryption messages")
parser.add_argument('-pt','--PlainText', help='Message before encryption',metavar='',type=str)#private key . pub
parser.add_argument('-ct','--cipherText', help='Message after encryption',metavar='',type=str)
parser.add_argument('-pr','--privatekeyfile', help='Write the name of file as PEM file to find private key',type=str)#pem
parser.add_argument('-pub','--publickeyfile', help='Write the name of file as PEM file to find public key',type=str)
parser.add_argument('-ep','--encryptionP', help='encryption a message by using PEM', action='store_true')#with k without k
parser.add_argument('-eg','--encryptionG', help='encryption a message by generating a public and private keys', action='store_true')
parser.add_argument('-d', '--decryption', help='decryption a message',action='store_true')
args=parser.parse_args()
if args.encryptionG:
    p1,p2,n,z,e,d = RsaCipher.SetKeys()
    RsaCipher.encryption(args.PlainText,e,n)
    RsaCipher.ExportKeysInPEM(n,e,d,p1,p2) 
if args.encryptionP:
    n,e,p1,p2,d =RsaCipher.InportKeysFromPEM(args.publickeyfile, args.privatekeyfile,)
    RsaCipher.encryption(args.PlainText,e,n)

if args.decryption:
    n,e,p1,p2,d= RsaCipher.InportKeysFromPEM(args.publickeyfile , args.privatekeyfile)  
    RsaCipher.decryption(args.cipherText,d,n)
