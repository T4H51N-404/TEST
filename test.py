import random 
 import os 
 import time 
 p = '\033[95m' 
 c = '\033[96m' 
 c2 = '\033[36m' 
 b = '\033[94m' 
 g= '\033[92m' 
 y = '\033[93m' 
 r = '\033[91m' 
 bold = '\033[1m' 
 underline = '\033[4m' 
 off= '\033[0m' 
     
 os.system('clear') 
 os.system('figlet -f big Password | lolcat') 
 print(r+bold) 
 print('\t\tVersion : 2.O') 
 print(c2+bold) 
 a=str(''' 
  ╔══════════════════════════╗ 
  ║  Author     :   TAHSIN                                 ║ 
  ║  Github     :   TAHSIN-404                          ║ 
  ╚══════════════════════════╝ 
  ''') 
 print(a) 
 print(g+bold+'================================================'+off) 
 amount=int(input(g+bold+'\n\tEnter Password Amount :'+p+''+bold+' ')) 
 lenth=int(input(g+bold+'\n\tEnter Password Length (mx-80) :'+p+''+bold+' ')) 
 os.system('clear') 
 os.system('figlet -f small Please Wait | lolcat') 
 print(g+bold+'================================================'+off) 
 time.sleep(1) 
  
 # super set of password characters 
 charset = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$_&-+~.\{}[]()/*' 
 # length of password 
 password_length = (lenth) 
 # loop 5 times to generate different passwords 
 for i in range(amount): 
     # pick 8 random characters from the charset 
   password_chars = random.sample(charset, password_length) 
     # combine them into a string  
   password = ''.join(password_chars) 
   print('\n[>] Random password is : ', password)