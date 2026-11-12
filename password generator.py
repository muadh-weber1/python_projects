import secrets 
import string
import re
import time
from cryptography.fernet import Fernet



def master_password():
	master_key=input("create your master key: ")
	ww=input("confirm created master key: ")
	while True:
		if 2!=master_key:
			print("password doesn't match")
def pass_gen(plen, use_numbers, use_symbols):
    charset = string.ascii_letters 
    if use_numbers:
        charset += string.digits
    if use_symbols:
        charset += "@#&*"
    while True:
        password = ""
        for i in range(plen):
            password += secrets.choice(charset)
        if use_numbers and not any(c in string.digits for c in password):
            continue
        if use_symbols and not any(c in "@#&*" for c in password):
            continue
        if  not any(c in string.ascii_uppercase for c in password):
        	continue
        if not any(c in string.ascii_lowercase for c in password):
             continue            
				            
				            

        return password
def generate():
	while True:
	   try:
	       plen =int(input("enter your password length:"))
	       if plen<8:
	           print("minimum length is 8")
	           continue
	       pass_no=int(input("how many passwords do you want? "))
	       break
	   except ValueError:   
	  			print("only numbers allowed ")
	  			continue
	while True:
		answer =input("include numbers in your password  y/n: ").lower()
		if answer=="y" or answer=="n":
	 		break
		print("only n or y allowed")
	use_numbers=answer =="y"
	while True:
 		answer_2=input("include symbols in your password  y/n: ").lower()
 		if answer_2== "y"or  answer_2== "n":
 			break
 		print("only y or n allowed")
	use_symbols= answer_2=="y"
	site =input("What do you want to use the password for? ")				
	for i in range(pass_no):
		password=pass_gen(plen,			use_numbers,use_symbols)
		print (password)
		token=fernet.encrypt(password.encode()).decode()
		with open("vault.txt", "a")as f:
				f.write(site + ":" + token + "\n")
				time.sleep(2)
				print("saved")
def find():
    site = input("which site? ")
    found = False
    try:
    	with open("vault.txt", "r") as f:
        	for line in f:
        	      if line.lower().startswith(site.lower() + ":"):
                	found = True
                	if found:
                		print("checking")
                		print(line.strip())
                		time.sleep(2)
                		print("password found🎉")
                	else:
                		print("checking")
                		time.sleep(5)
                		print("password not found😓")
    except FileNotFoundError :
          	print("no password saved yet")
   	
        
def view_saved():
	try:
		with open("vault.txt", "r") as f:
			for line in f:
				if not line.strip():
					continue
				site, token = line.strip().rsplit(":", 1)
				password =fernet.decrypt(token.encode()).decode()
				print(site, password)
				
	except FileNotFoundError:
				print("password not saved yet")
def rate(password):
    length = len(password)
    
    # Check which character categories are present
    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_symbol = bool(re.search(r"[@#&*]", password))
    
    # Count how many varieties are used (out of 4)
    variety_count = sum([has_lower, has_upper, has_digit, has_symbol])
    
    # Flexible logic:
    # 1. Very long passwords (12+ chars) are strong even with lower variety
    # 2. Standard passwords (8+ chars) need good variety (at least 3 types)
    if (length >= 12 and variety_count >= 2) or (length >= 8 and variety_count >= 3):
        return "STRONG🔏🔏"
    # 3. Decent length with some variety
    elif length >= 8 and variety_count >= 2:
        return "MEDIUM 🟡"
    else:
        return "WEAK ❌"
        
	
	   
	 			
def password_strength():
	   password=input("enter password to check: ")
	   print("checking password strength")
	   time.sleep(0.2)
	   result =rate(password)
	   print(result)

def checksaved_strength():
	try:
		strong=0
		weak=0
		with open("vault.txt", "r") as f:
			for line in f:
				site,token=line.strip().rsplit(":",1)
				password= fernet.decrypt(token.encode()).decode()
				print(site,password)
			
				if not line:
					continue
				site,password=line.rsplit(":", 1)
				result=rate(password)
				print(site,"-",result)
				if result.startswith("STRONG🔏🔏"):
					strong+=1
				else:
					weak+=1
			print("weak passwords=",weak)
			print("strong passwords=",strong)		
	except FileNotFoundError:
			print("password not saved yet")
def load_key():
				   try:
				   	with open("key.key", "rb")as f :
				   		return f.read()
				   except FileNotFoundError:
				    	key=Fernet.generate_key()
				    	with open("key.key","wb")as f :
				    		f.write(key)
				    		return key
fernet=Fernet(load_key())			
				   
	   			
while True:
	
	print("WELCOME TO WEBER KEY")
	print ("1.generate password")
	print("2.find password ")
	print ("3.view saved passwords")
	print("4.check saved passwords strength ")
	print("5.check random password strength")
	print("6.exit")
	try:
		choice=int(input("choose an option : "))
	except ValueError:
		print("only numbers allowed")
		continue
	
					
	if choice==1:
		generate()
	elif choice ==2:
		find()
	elif choice==3:
		view_saved()
	elif choice==4:
		checksaved_strength()
	elif choice==5:
		password_strength()	
	elif choice==6:
		print("Thank you for using Weber key🤝 We've got your password security🔏 covered")
		break
	else:
		print("1,2,3,4,5,6only allowed")		
		
								
		

	
			

