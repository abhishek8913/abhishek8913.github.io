from ast import While
from codecs import charmap_build
##from  import isalpha,isdigit
import datetime  as date
from distutils.log import error
from logging import exception, raiseExceptions
from sqlite3 import IntegrityError
SpecialSym =['$', '@', '#', '%']


import mysql.connector 
dates1=date.datetime.now()
import random
import string

mydb=mysql.connector.connect(host="localhost",user="root",password="9020@Abhishek",database="bankdb")
mycursor= mydb.cursor()
Admin_Login="abhishek1"
Admin_Password="9020@Abhishek"

while True:
	print("\n")
	print("*  *  *  *  *  Welcome To ADEM Bank  *  *  *  *  *")
	print("\n")
	
	print("Experience the next level banking.")
	print("\n")
	print("Press 1 for Admin Login")
	print("Press 2 to User Login  ")
	print("\n")
	ch=int(input("Enter Your Choice : "))

	if(ch>=3) :
		print("  Try again... Enter valid choice ")
	elif(ch==1):
		print("Enter Admin Username and Password to Login to Adem Bank's Database")
		admin=input("Enter the Admin Username:	")
		pswd=input("Enter the Admin Password:	")
		if (admin==Admin_Login) and (pswd==Admin_Password):
			print("\n")
			print("Accessing the database...")
			print("\n")
			print("Choose the operation you want to perform")
			print("\n")
			print("Press 1 to Create an Account and Login Credentials  ")
			print("Press 2 to Update an Account  ")
			print("Press 3 to Delete an Account Permanently  ")
			print("Press 4 to View Account details	")
			#print("Press 5 for Loan Approval Section ")
			print("\n")

			operation=int(input("Enter Your Choice : "))
			if(operation>=5) :
				print("  Try again... Enter valid choice")
			elif(operation==1):
				while True:
			
					n=input("Enter User Name Here : ")
					print("Generating User AccountNumber & Password now...")
					u=''.join(random.choice(string.digits) for i in range(8))
					
					z=''.join(random.choice(string.digits) for i in range(4))

	
					k=int(input("Enter the Amount of money you want to deposit : "))
					print("Please enter Date of birth in proper format !!! DD/MM/YYYY")
			
					a=input("Enter Your Date of Birth : ")
					a = date.datetime.strptime(a, "%d/%m/%Y").date()
					

					s=input("Enter Your Address : ")

					d=input("Enter Your Phone Number : ")
					if (len(d)!=10) or (d.isalpha()):
						print("Please enter a valid 10 digit Number")
						break
	
					f=input("Enter Your 12 Digit Aadhar Number : ")
					if(len(f)!=12) or (f.isalpha()):
						print("Please Enter a valid 12 digit aadhar Number")
						break

					g=int(input("Enter Your Annual Income : "))
					q="insert into adembank values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(n,u,z,a,s,d,f,k,g)
					mycursor.execute(q)
					mydb.commit()

					print("*  *  *  *  Account Has Been Created Successfully  *  *  *  *")
					print("\n")
					print(" Name of Account Holder	:   ",n)
					print(" Account Number		:   ",u)
					print(" Password		:   ",z)
					break

			elif(operation==2):
				accnt=input("Enter the AccountNumber : ")
				psd=input("Enter the Password : ")

				while True:
					print("Press 1 To Update Name  ")
					print("Press 2 To Update Account Number   ")
					print("Press 3 To Update PassWord  ")
					print("Press 4 To Update Phone Number  ")
					print("Press 5 To Update Address  ")
					ch2=int(input("Enter your Choice  "))
					if(ch2>=6):
						print("Invalid input")
						break
					if(ch2==1):
						name=input ("Enter Your New Name : ")
						ns="update adembank set name='{}' where Accountnumber='{}'".format(name,accnt)
						mycursor.execute(ns)
						mydb.commit()

						print ("	* * * Name Updated Successfully * * *	") 
					elif(ch2==2):


						mp=input("Enter Your New Accountnumber : ")
						nm="update adembank set Accountnumber='{}' where password='{}'".format(mp,psd)
						mycursor.execute(nm)
						mydb.commit()

						print ("	* * * Account Number Updated Successfully * * * ")


					elif(ch2==3):

						newpassword=input("Enter Your New Password : ")
						us="update adembank set Password='{}' where Accountnumber='{}'".format(newpassword,accnt)
						mycursor.execute(us)
						mydb.commit()
						print ("	* * * Password Updated Successfully * * *	")

					elif(ch2==4):
						newphone=(input("Enter Your New Phone Number : "))
						if(len(newphone)!=10) or newphone.isalpha():
							print("		* * * Please Enter a valid 10 digit number * * * 	")
						us="update adembank set Mobile_Number='{}' where  Accountnumber='{}'".format(newphone,accnt)
						mycursor.execute(us)
						mydb.commit()
						print ("   * * * Mobile Number Updated Successfully * * *	")

					elif(ch2==5):
						newadd=input("Enter Your New Address : ")
						ns1="update adembank set address='{}' where Accountnumber='{}'".format(newadd,accnt)
						mycursor.execute(ns1)
						mydb.commit()
						print("   * * * Address Updated Successfully * * *   ") 
					else:

						print("Operation Aborted!!!")

			elif(operation==3):
	
				accnt=input("Enter the AccountNumber : ")
				psd=input("Enter the Password : ")
				
				print("Trying to delete Account holder with account number:	",accnt)
				ok=input("Press 'S' if you wish to continue:	")
				input="S"
				if (ok==input):

					delet="delete from adembank where password='{}'".format(psd)
					mycursor.execute(delet)
					mydb.commit()
				
					delet1="delete from Transactions where Accountnumber1='{}'".format(accnt)
					mycursor.execute(delet1)
					mydb.commit()
				
					print("\n")
					print(" * * * ACCOUNT HAS BEEN DELETED SUCCESSFULLY * * * ")
					exit()
					
				else:
	
					print("Operation Aborted!!!")

			elif(operation==4):
				mycursor.execute("SELECT * from adembank")
				print("_________________________________________________________________________________________________________________________________________")
				print("Name      AccountNumber   PassWord   Date of Birth \t      Address          Mob No         Aadhar No        Balance     Annual Income	")
				print("_________________________________________________________________________________________________________________________________________")
				for x in mycursor:
					print(x)
					print("_________________________________________________________________________________________________________________________________________")
			
	if(ch==2):
		u=input("Enter Your AccountNumber : ")
		p=input("Enter Your Password : ")
		a="select * from adembank where AccountNumber='{}' and Password='{}'".format(u,p)
		mycursor.execute(a)
		data=mycursor.fetchall()
		if data:
			while True:
				d1="select Name from adembank where Accountnumber='{}'".format(u)
				mycursor.execute(d1)
				nme=mycursor.fetchone()[0]
				print("\n")
				print("\n")
				print("* * * * * Welcome",nme,"!!!"," * * * * *")
				print("\n")
				print("Press 1 to Withdraw Money")
				print("Press 2 to Deposit Money")
				print("Press 3 to View Last Five Transaction ")
				print("Press 4 to View Your Profile ")
				print("Press 5 to Log Out")
				print("Press 6 to Log Out")

				ch1=int(input("Enter Your Choice : "))

				if(ch1>=6):
					print(" Invalid Input ")
				if(ch1==1):
					np="select Balance from adembank where AccountNumber='{}'".format(u)
					mycursor.execute(np)
					bal=mycursor.fetchone()[0]
				
					print("Your Account Balance is : " ,bal)

					while True:
						a1=int(input("Enter the amount for withdrawal: "))
				
						if a1<=bal:
							credited=0
						
							t6="update adembank set Balance=Balance - '{}' where AccountNumber='{}'".format(a1,u)
							mycursor.execute(t6)
							mydb.commit()


							bp="insert into Transactions values('{}','{}','{}')".format(credited,a1,u)
							mycursor.execute(bp)
							mydb.commit()

							np9="select Balance from adembank where AccountNumber='{}'".format(u)
							mycursor.execute(np9)
							bal1=mycursor.fetchone()[0]

							print("\n")
							print("Your AccountNumber:" ,u , "is debited with Rs" , a1 )
							print("towards Net Banking. Available balance is Rs : " , bal1, " ₹ only ")
							break

						else:

							print("   * * * * * Insufficient Balance Please Try Again ! * * * * *")
							break
				elif(ch1==2): 
					debited=0

					while True:
						a11=(input("Enter the amount to deposit : "))

						t6= "update adembank set Balance=Balance +'{}' where AccountNumber='{}'".format(a11,u)
						mycursor.execute(t6)
						mydb.commit()

						mn="insert into Transactions values('{}','{}','{}')".format(a11,debited,u)
						mycursor.execute(mn)
						mydb.commit()

						np9="select Balance from adembank where AccountNumber='{}'".format(u)
						mycursor.execute(np9)
						bal2=mycursor.fetchone()[0]

						print("\n")
						print("Your AccountNumber:" ,u , "is Credited with Rs" , a11 )
						print("towards Net Banking. Available balance is Rs : " , bal2, " ₹ only")
						break


				elif(ch1==3):
					prt="Select Credited,Debited from Transactions where Accountnumber1='{}'".format(u)
					mycursor.execute(prt)
					print("* * * * * The Transaction Details are as Follows * * * * *")
					print("\n")
					for i in mycursor:
						print("Credited , Debited  : " ,i)
					d8="select Balance from adembank where AccountNumber='{}'".format(u)
					mycursor.execute(d8)
					bal=mycursor.fetchone()[0]
					print("\n")
					print("Account Balance		: ",bal)
					print("________________________________")


				elif(ch1==4):
					
					print("_________________________________________________________________________________________________")
					print("		* * * * * * *                 ACCOUNT DETAILS                * * * * * * *		")
					print("_________________________________________________________________________________________________")

					d1="select Name from adembank where Accountnumber='{}'".format(u)
					mycursor.execute(d1)
					nme=mycursor.fetchone()[0]

					d2="select AccountNumber from adembank where Accountnumber='{}'".format(u)
					mycursor.execute(d2)
					act=mycursor.fetchone()[0]

					d3="select Password from adembank where Accountnumber='{}'".format(u)
					mycursor.execute(d3)
					pswd=mycursor.fetchone()[0]

					d4="select Address from adembank where Accountnumber='{}'".format(u)
					mycursor.execute(d4)
					dtfbth=mycursor.fetchone()[0]

					d5="select Date_of_birth from adembank where Accountnumber='{}'".format(u)
					mycursor.execute(d5)
					addrs=mycursor.fetchone()[0]

					d6="select Mobile_Number from adembank where Accountnumber='{}'".format(u)
					mycursor.execute(d6)
					mobln=mycursor.fetchone()[0]

					d7="select Aadhar_no from adembank where Accountnumber='{}'".format(u)
					mycursor.execute(d7)
					adhr=mycursor.fetchone()[0]

					d8="select Balance from adembank where AccountNumber='{}'".format(u)
					mycursor.execute(d8)
					bal=mycursor.fetchone()[0]
					
					print("Name of Account Holder	: ",nme)
					print("AccountNumber		: ",act)
					print("Password			: ",pswd)
					print("Address  		: ",dtfbth)
					print("Date of Birth		: ",addrs)
					print("Mobile Number		: ",mobln)
					print("Aadhar Number		: ",adhr)
					print("Account Balance		: ",bal)
					print("__________________________________________________________________________________________________")
				elif(ch1==5):
					print("\n")
					print("* * * * * * *        Thanks For Banking with us       * * * * * * *")
					exit()	
					
	else:
				
		print("        Login Again to continue further operations	")
		exit()
			