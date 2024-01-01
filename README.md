# RSACrypto
Our tool is designed to decrypt and encrypt strings using RSA cipher, The public and private keys for encryption can be generated using RSACrypto or given by the user. Also, All keys either private or public need to be given as .PEM files. 
 _____   _____         _____                  _        
|  __ \ / ____|  /\   / ____|                | |       
| |__) | (___   /  \ | |     _ __ _   _ _ __ | |_ ___  
|  _  / \___ \ / /\ \| |    | '__| | | | '_ \| __/ _ \ 
| | \ \ ____) / ____ \ |____| |  | |_| | |_) | || (_) |
|_|  \_\_____/_/    \_\_____|_|   \__, | .__/ \__\___/ 
                                   __/ | |
                                  |___/|_|
      
--Credits:
[*]Ghada Bin Rubaian
[*]Muneera Alsulaiman
[*]Asma Al Yami
[*]Lujain Alqahtani
[*]Dalal Alkhaldi

->Intructor: Dr.Reem Alassaf
->course:programming for CyberSecurity
#pre requirement:
pip install rsa 
#usage:
1.Encrypting a text and generate Keys :
python RsaCrypto.py -eg -pt plain.txt
2.Decrypting a cipher text:
python RsaCrypto.py -d -ct cipher.txt -pub public.pem -pr private.pem
3.Encrypting a text with user provided Keys:
python RsaCrypto.py -ep -pt plain.txt -pub public.pem -pr private.pem


 
