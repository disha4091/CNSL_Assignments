# first of all import the socket library
import socket            
from random import randint
import math
from Crypto.Cipher import DES
import codecs
s = socket.socket()        
print ("Socket successfully created")
 
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 1237
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)    
print ("socket is listening")           
 
# a forever loop until we interrupt it or
# an error occurs
while True:
 
# Establish connection with client.
  c, addr = s.accept()    
  print ('Got connection from', addr )
 
  pStr = input("This is server, enter p: ")
  c.send(pStr.encode())
  p = int(pStr)
  gStr = c.recv(1024).decode()
  # print(info_b)
  g = int(gStr)

  private_a = 4
  #print (eb)
  #print (nb)
  x = (g**private_a)%p
  
  xStr = str(x) 
  c.send(xStr.encode())
  
  yStr = c.recv(1024).decode()
  
  y = int(yStr)
  
  ka = (y**private_a)%p
  print("Secret key for server = %d" %ka)
  
  message = int(input("Enter message for client->integer value: "))
  msg_bytes = message.to_bytes(8, 'little')
  #print(msg_bytes)
  def pad(text):
    n = len(text) % 16
    return text + (b' ' * n)

  key = ka.to_bytes(8, 'little')

  des = DES.new(key, DES.MODE_ECB)

  encrypted_text = des.encrypt(msg_bytes)
  #decrypted_text = des.decrypt(encrypted_text)
  
  #print(int.from_bytes(decrypted_text, 'little'))
  #print(type(encrypted_text))
  c.sendall(encrypted_text)
  
  encrypted_text_cl = c.recv(1024)

  decrypted_text_cl = des.decrypt(encrypted_text_cl)
  print('Encrypted text is: ' + str(encrypted_text_cl))
  print('Decrypted text is: %d' %int.from_bytes(decrypted_text_cl, 'little'))
  c.close()
  # Breaking once connection closed
  break