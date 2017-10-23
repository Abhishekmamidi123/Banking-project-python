import datetime
import re
import pickle

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

class Account:
	number_accounts = 0
	interest_rate = {'Savings':4, 'Current':0,'Fixed':12}

	def __init__(self):
		pass

	def create_account(self, name, balance):
		Account.number_accounts += 1
		self.account_no = Account.number_accounts
		self.active = 1
		self.name = name
		self.balance = balance
		return self.account_no

	def update_interest(self):
		rate = Account.interest_rate[self.account_type]

		if (datetime.datetime.now().year == self.last_updated[1]):
			dif = (datetime.datetime.now().month - self.last_updated[0])
		else:
			if (datetime.datetime.now().month < self.last_updated[0]):
				dif = (datetime.datetime.now().year - self.last_updated[1]-1)*12 + 12 - (self.last_updated[0] - datetime.datetime.now().month)
			else:
				dif = (datetime.datetime.now().year - self.last_updated[1])*12 + (datetime.datetime.now().month - self.last_updated[0])

		self.balance += (dif*rate*self.balance/100)
		self.last_updated = [datetime.datetime.now().month, datetime.datetime.now().year]

	def balance_enquiry(self):
		self.update_interest()		
		return self.balance

	def deposit(self):
		self.update_interest()
		dep_amount = input("Enter the amount you wish to deposit: ")
		self.balance += dep_amount
		return self.balance

	def withdraw(self):
		withdraw_amount = input("Enter the amount you wish to withdraw: ")

		if self.balance - withdraw_amount >= 0:
			self.balance -= withdraw_amount
			return self.balance

		print "Insufficient funds to withdraw given amount."
		return -1

	def compare_name(self, search_name):
		pattern = '[\w\s]*'+search_name+'[\w\s]*'
		prog = re.compile(pattern,re.I)
		result = prog.match(self.name)
		if result == None:
			return [-1]
		if result.group(0) == self.name:
			self.balance_enquiry()
			return [1, self.name, self.account_no]
		else:
			return [-1]

	def close_account(self):
		balance = self.balance_enquiry()
		self.balance = 0
		print "You have withdrawn an amount of " + str(balance) + " and closed your account."
		self.active = 0

class Savings(Account):
	def __init__(self):
		self.last_updated = [datetime.datetime.now().month, datetime.datetime.now().year]
		self.account_type = "Savings"

	def withdraw(self):
		withdraw_amount = input("Enter the amount you wish to withdraw: ")

		if self.balance - withdraw_amount >= 1000:
			self.balance -= withdraw_amount
			return self.balance

		print "Insufficient funds to withdraw given amount."
		return -1

class Current(Account):
	def __init__(self):
		self.last_updated = [datetime.datetime.now().month, datetime.datetime.now().year]
		self.account_type = "Current"	


class Fixed(Account):
	def __init__(self):
		self.last_updated = [datetime.datetime.now().month, datetime.datetime.now().year]
		self.account_type = "Fixed"

	def deposit(self):
		print "This is a Fixed Account. You will not be able to deposit."
		return -1

	def withdraw(self):
		print "This is a Fixed account. Close the account if you want to withdraw."
		return -1



accounts = load_obj('accounts')
closed_accounts = load_obj('closed_accounts')
Account.number_accounts = accounts[0]

while 1:
	print "1. Create Account\n2. Balance Enquiry\n3. Deposit\n4. Withdraw\n5. Search by name\n6. Close Account\n0. Exit"
	choice = input()

	if choice == 1:
		choice = input("1. Savings\n2. Current\n3. Fixed\n")

		if choice == 1:
			new_account = Savings()

		elif choice == 2:
			new_account = Current()

		elif choice == 3:
			new_account = Fixed()

		else:
			print "Invalid Choice"

		name = raw_input("Enter Full Name: ")
		balance = input("Initial balance: ")

		ac_no = new_account.create_account(name, balance)
		accounts[ac_no] = new_account
		print "Your account number is ", ac_no

	elif choice == 2:
		ac_no = input("Enter your account number: ")
		account = accounts[ac_no]
		print "Your balance is ", account.balance_enquiry()

	elif choice == 3:
		ac_no = input("Enter your account number: ")
		account = accounts[ac_no]
		balance = account.deposit()
		if balance != -1:
				print "Your balance is ", balance		

	elif choice == 4:
		ac_no = input("Enter your account number: ")
		account = accounts[ac_no]
		balance = account.withdraw()
		if balance != -1:
				print "Your balance is ", balance		
		
	elif choice == 5:
		search_name = raw_input("Enter name you want to search for: ")
		flag = 0
		for ac_no, account in accounts.iteritems():
			if ac_no != 0:
				result = account.compare_name(search_name)
				if result[0] == 1:
					print str(result[1])+' '+str(result[2])
					flag = 1

		if flag == 0:
			print "Name hasn't been found"			

	elif choice == 6:
		ac_no = input("Enter your account number: ")
		account = accounts[ac_no]
		if (raw_input("Are you sure you want to close your account? (y/n): ") == 'y'):
			account.close_account()
			closed_accounts[ac_no] = account
			del accounts[ac_no]

	elif choice == 0:
		accounts[0] = Account.number_accounts
		save_obj(accounts,'accounts')
		save_obj(closed_accounts,'closed_accounts')

		break

	else:
		print "Invalid input"