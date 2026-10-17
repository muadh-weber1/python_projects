
print("WELCOME TO WEBER BANK")
account_balance = 50000
bank_operation = ["1 CHECK BALANCE",
"2 WITHDAWAL",
"3 DEPOSIT",
"4 EXIT"]


def deposit():
    print("visit any nearest bank or pos")
    
    
def withdrawal():
    global account_balance
    
    amount = int(input("how much do you want to withdraw: "))
    
    account_balance= account_balance-amount
    if amount<=account_balance:
        print("withdrawal successful your balance is",account_balance)
    else:
         print("insufficient funds kindly deposit into your account ")
   
    
    
    
def balance():
    print("your balance is", account_balance)  

def exit():
    print("Thank you")
       

def show_options():
    print("#pick an option ")
    for operation in bank_operation:
       print(operation)
    
    
while True :
       
         show_options()
         choice=int(input("choose an option: "))     
         pin =int(input("enter your pin:  "))
         
         
         if pin != 2030:
               print("incorrect pin account will be blocked after 5 inorrect trials")
               pin =int(input("enter your pin:  "))
         if choice ==1:
             balance()
              
         if choice==2:
           withdrawal()
         if choice==3:
           deposit() 
         if choice==4:
            
            break

