#!/usr/bin/python
class Bank():
	def __init__(self):
		self.Name=[]
		self.Amount=[]
		self.z=123000
		self.Account=[]
		self.Type=[]
		self.num=1	
	def CreateAccount(self,typenumber,name,amount) :
		self.Type.append(typenumber)
		if typenumber==1 :		
			if amount<1000 :
	                        while amount<1000:
	                                print "Minimum balance should be 1000"
	                                print "Again Enter the amount :",
	                                amount=input()
	                        self.Name.append(name)
	                        self.Amount.append(amount)
	                        print "Your Account number is :",
	                        print self.z
	                        self.Account.append(self.z)
	                        self.z=self.z+1
	                else :
	                        self.Name.append(name)
	                        self.Amount.append(amount)
	                        print "Your Account number is :",
	                        print self.z
	                        self.Account.append(self.z)
	                        self.z=self.z+1
                if typenumber==2 :
			self.Name.append(name)
			self.Amount.append(amount)
			self.Account.append(self.z)
			print "Your Account number is :",
	               	print self.z
		if typenumber==3 :
			if amount<10000 :
       		             	while amount<10000:
                	                print "Minimum balance should be 10000"
                	                print "Again Enter the amount :",
                	                amount=input()	
	 		       	self.Name.append(name)
          	      	        self.Amount.append(amount)
               		        print "Your Account number is :",
              	 	        print self.z
                        	self.Account.append(self.z)
                        	self.z=self.z+1
               		else :
                        	self.Name.append(name)
                        	self.Amount.append(amount)
                        	print "Your Account number is :",
                        	print self.z
                        	self.Account.append(self.z)
                        	self.z=self.z+1	
    		     
	def BalanceEnquiry(self,account) :
		k=self.Account.index(account)
                print "Your balance is :",
                print self.Amount[k]
                
	def DepositAmount(self,account,amount) :
		k=self.Account.index(account)
		if self.Type[k]==3 :
			print "Deposits are not permitted ."
		else :
			self.Amount[k]=self.Amount[k]+amount
			print "Your final balance is :",
			print self.Amount[k]
		
	def WithdrawAmount(self,account,amount) :	
		k=self.Account.index(account)
		if self.Type[k]==3 :
			print "Withdrawl of amount is not permitted .Only way to withdraw money is to close the account"
		else :
			if self.Amount[k]-amount>=5000 :
				self.Amount[k]=self.Amount[k]-amount
			else :
				while self.Amount[k]-amount < 5000 :	
					print ("Maximum Amount can be taken : %d" % (Amount[k]-5000))
					amount=input()
				self.Amount[k]=self.Amount[k]-amount
			print "Your final balance is :",
			print self.Amount[k]
	
	def SearchByName(self,name) :
		i=0
		while 2>1 :
			if name in self.Name[i] :
				print "Your name is :",
				print self.Name[i]
				print "Your Account number :",
				print self.Account[i]
				break
			i=i+1
			
	def CloseAccount(self,account) :
		l=account in self.Account
		if l==0 :
			print "Your Account is invalid ."
		else : 
			k=self.Account.index(account)
			print ("Balance to be refunded : %d" % (self.Amount[k]))					
			self.Account.remove(self.Account[k])
			self.Name.remove(self.Name[k])
			self.Amount.remove(self.Amount[k])
			self.Type.remove(self.Type[k])
			print "Your Account is closed "
		
num=1	
B=Bank()
while num<=6 :
	print ""
	print "1.Create account         ",
	print "2.Balance Enquiry      ",
	print "3.Deposit Amount  "
	print "4.Withdraw Amount        ",
	print "5.Search by name       ",
	print "6.Close Account   "
	print "7.exit"
	num=input()	
	if num==1 :
		print "Choose your type :"
		print "1.Savings Account     ",
		print "2.Current Account     ",
		print "3.Fixed Account"
		typenumber=input()
		print "Enter your name :",
		name=raw_input()
		print "Enter the amount :",
		amount=input()
		B.CreateAccount(typenumber,name,amount)
			
	if num==2 :
		print "Enter your account number :",
		account=input()
		B.BalanceEnquiry(account)

	if num==3 :
		print "Enter your Account number :",
		account=input()
		print "Enter the amount to be deposited :",
		amount=input()
		B.DepositAmount(account,amount)

	if num==4 :
		print "Enter your Account number :",
		account=input()
		print "Enter the amount to be withdrawn :",
		amount=input()
		B.WithdrawAmount(account,amount)

	if num==5 :
		print "Enter your name :",
		name=raw_input()
		B.SearchByName(name)
		
	if num==6 :
		print "Enter your Account number :",
		account=input()
		B.CloseAccount(account)
	
print B.Name
print B.Account
print B.Amount
print B.Type
f1=open("bank_accounts.txt","r")
f=open("bank.txt","w")
y=len(Name)
i=0
while i<=y-1 :
	f.write(nam1[i])
	f.write(" %d" %(acc1[i]))
	f.write(" %d\n"%(amoun1[i]))
	i=i+1
