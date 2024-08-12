print("This is a Bank Applicatiom. \n Your 'Initial Balance is ₹1000 .'")
print("Amount to be deposited: ")
a=int(input())
c=a+1000
print("Your balance after depositing the money is: \n",c)

print("Amount you want to withdraw:")
b=int(input())
d=c-b

if d<0:
    print("Error! You do not have sufficient balance.")
else:
    print("Balance after withdrawl is: \n",d)