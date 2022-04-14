# Import socket module
import socket            
from random import randint
import math
from Crypto.Cipher import DES
# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
port = 1237
# connect to the server on local computer
s.connect(('127.0.0.1', port))
 
# receive data from the server and decoding to get the string.
gStr = input("This is client, enter g: ")
g = int(gStr)
s.sendall(gStr.encode())
pStr = s.recv(1024).decode()
p = int(pStr)

private_b = 3

y = (g**private_b)%p

yStr = str(y) 
s.sendall(yStr.encode())
  
xStr = s.recv(1024).decode()
  
x = int(xStr)
kb = (x**private_b)%p
print("Secret key for client = %d" %kb)
message = int(input("Enter message for server->integer value: "))
msg_bytes = message.to_bytes(8, 'little')
#print(msg_bytes)
def pad(text):
    n = len(text) % 16
    return text + (b' ' * n)

key = kb.to_bytes(8, 'little')

des = DES.new(key, DES.MODE_ECB)

encrypted_text_cl = des.encrypt(msg_bytes)
  #decrypted_text = des.decrypt(encrypted_text)
  
  #print(int.from_bytes(decrypted_text, 'little'))
  #print(type(encrypted_text))
s.sendall(encrypted_text_cl)


encrypted_text = s.recv(1024)

decrypted_text = des.decrypt(encrypted_text)
print('Encrypted text is: ' + str(encrypted_text))
print('Decrypted text is: %d' %int.from_bytes(decrypted_text, 'little'))

# close the connection
s.close()  