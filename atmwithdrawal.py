#withdrawal
balance=1000
pin=int(input("enter the number:"))
stored_pin=6781
if(pin==stored_pin):
    print("welcome to the bank!")
else:
    print("user denied")
    
    print("___Atm__Menu")
    print("1.checkbalance")
    print("2.deposit")
    print("3.withdrawal")
    print("4.exit")
choice=input("enter the choice:")
if(choice=="1"):
    print("balance",balance)
elif(choice=="2"):
    amount_deposit=float(input("enter the amount to deposit:"))
    totalamt=amount_deposit+balance
    print("the total amount is:",totalamt)
elif(choice=="3"):
    amount_withdrawal=float(input("enter the amount to withdraw:"))
    remaining_amount_bank=amount_withdrawal-balance
else:
    print("welcome bank again!")