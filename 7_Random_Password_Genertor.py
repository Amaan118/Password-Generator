import random
import string

upper = 0
lower = 0
digits = 0
special = 0

def ask_user():
	print("Choose 1 for Yes and 0 for No")
	try:
		global upper
		upper = int(input("A. Include Upper Case Letters (1) or (0) : "))
		
		global lower
		lower = int(input("B. Include Lowercase Letters (1) or (0) : "))
		
		global digits
		digits = int(input("C. Include Digits (1) or (0) : "))
		
		global special
		special = int(input("D. Include Special Characters (1) or (0) : "))
		
	except:
			print("\nPlease Enter an integer ")
			exit()
			
password = ""
print("=== WELCOME TO RANDOM PASSWORD GENERATOR ===")

ask_user()
part1 = []
pass_len = int(input("\nEnter Length of Password : "))

if upper == 1:
	part1.extend(string.ascii_uppercase)
if lower == 1:
	part1.extend(string.ascii_lowercase)
if digits == 1:
	part1.extend(string.digits)
if special == 1:
	part1.extend(string.punctuation)

password = "".join(random.sample(part1,pass_len))		
print(f"Your {pass_len} digit Password is {password}")