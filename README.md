# Banking-project-python

A small banking appication using python:

1. Create account
INPUT: Full name, initial balance (min. Rs. 5,000)
OUTPUT: Account number (new)

2. Balance enquiry
INPUT: Account number
OUTPUT: Balance

3. Deposit amount:
INPUT: Account number, amount
OUTPUT: Final balance

4. Withdraw amount:
INPUT: Account number, amount
OUTPUT: Final balance (ensure minimum balance is Rs. 5,000)

5. Search by name:
INPUT: Name (Full or partial)
OUTPUT: Full name, Account number

volenzo clara
software engineering
1.4

6. Close account:
INPUT: Account number
OUTPUT: Balance (to be refunded) (status should become inactive/closed and should reflect appropriately in all operations)

7. Import account data:
INPUT: A comma separated values (CSV) file (bank_accounts.txt) containing: Name, Account number, Balance
(If account number is -1, then create a new account)
(If name or number already exists, skip that line and add it to an unprocessed_accounts.txt file)
(Test it with 1000 dummy accounts)
