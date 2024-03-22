import mysql.connector
import datetime  as date
import random
import string

mydb= mysql.connector.connect(host="localhost",user="root",password="9020@Abhishek",database="bankdb")
mycursor= mydb.cursor()

Admin_Login="abhishek1"
Admin_Password="9020@Abhishek"

while True:
	print("\n")
	
	print("*******************  Welcome To ADEM Bank *******************")
	print("\n")
	
	print("Your bank is always just a few clicks away.")
	print("\n")
	print("Press 1 for Admin Login")
	print("Press 2 to User Login  ")
	print("\n")
	ch=int(input("Enter Your Choice : "))

	if(ch>=3) :
		print("That was not a valid number.  Try again... ")
	elif(ch==1):
		print("Enter Admin Username and Password to Login to AdemBank's Database")
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
			print("Press 5 for Loan Approval Section ")
			print("\n")

			operation=int(input("Enter Your Choice : "))
			if(operation>=6) :
				print("That was not a valid number.  Try again... ")
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
					q="insert into AdemBank values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(n,u,z,a,s,d,f,k,g)
					mycursor.execute(q)
					mydb.commit()

					print("*****************Account Has Been Created Successfully********************")
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
						ns="update AdemBank set name='{}' where Accountnumber='{}'".format(name,accnt)
						mycursor.execute(ns)
						mydb.commit()

						print ("	*****Name Updated Successfully*****	") 
					elif(ch2==2):


						mp=input("Enter Your New Accountnumber : ")
						nm="update AdemBank set Accountnumber='{}' where password='{}'".format(mp,psd)
						mycursor.execute(nm)
						mydb.commit()

						print ("	*****Account Number Updated Successfully*****	")


					elif(ch2==3):

						newpassword=input("Enter Your New Password : ")
						us="update AdemBank set Password='{}' where Accountnumber='{}'".format(newpassword,accnt)
						mycursor.execute(us)
						mydb.commit()
						print ("	*****Password Updated Successfully*****	")

					elif(ch2==4):
						newphone=(input("Enter Your New Phone Number : "))
						if(len(newphone)!=10) or newphone.isalpha():
							print("		*****Please Enter a valid 10 digit number*****		")
						us="update AdemBank set Mobile_Number='{}' where  Accountnumber='{}'".format(newphone,accnt)
						mycursor.execute(us)
						mydb.commit()
						print ("   *****Mobile Number Updated Successfully*****		")

					elif(ch2==5):
						newadd=input("Enter Your New Address : ")
						ns1="update AdemBank set address='{}' where Accountnumber='{}'".format(newadd,accnt)
						mycursor.execute(ns1)
						mydb.commit()
						print("   *****Address Updated Successfully *****   ") 
					else:

						print("Operation Aborted!!!")

			elif(operation==3):
	
				accnt=input("Enter the AccountNumber : ")
				psd=input("Enter the Password : ")
				
				print("Trying to delete Account holder with account number:	",accnt)
				ok=input("Press 'S' if you wish to continue:	")
				input="S"
				if (ok==input):

					delet="delete from AdemBank where password='{}'".format(psd)
					mycursor.execute(delet)
					mydb.commit()
				
					delet1="delete from Transactions where Accountnumber1='{}'".format(accnt)
					mycursor.execute(delet1)
					mydb.commit()
				
					print("\n")
					print("************* ACCOUNT HAS BEEN DELETED SUCCESSFULLY *******************")
					exit()
					
				else:
	
					print("Operation Aborted!!!")

			elif(operation==4):
				mycursor.execute("SELECT * from AdemBank")
				print("_________________________________________________________________________________________________________________________________________")
				print("Name      AccountNumber   PassWord   Date of Birth \t      Address          Mob No         Aadhar No        Balance     Annual Income	")
				print("_________________________________________________________________________________________________________________________________________")
				for x in mycursor:
					print(x)
					print("_________________________________________________________________________________________________________________________________________")
			elif(operation == 5):
				# Loan approval section
				print("\n")
				print("Loan Approval Section")
				print("\n")

				# Assuming an annual income threshold for eligibility
				annual_income_min = 200000  # threshold
				age_min = 23  # Minimum age for eligibility

				# Fetch user data
				u = input("Enter User AccountNumber: ")
				p = input("Enter User Password: ")
				

				check_user_query = "SELECT * FROM AdemBank WHERE AccountNumber = %s AND Password = %s"
				mycursor.execute(check_user_query, (u, p))
				user_data = mycursor.fetchone()

				if user_data:
					dob="SELECT Date_of_birth FROM AdemBank where Accountnumber='{}'".format(u)
					mycursor.execute(dob)
					dob1=mycursor.fetchone()[0]
					user_age = date.datetime.now().year - dob1.year

					d1="select annual_income from AdemBank where Accountnumber='{}'".format(u)
					mycursor.execute(d1)
					ai=mycursor.fetchone()[0]

					if ai >= annual_income_min and user_age >= age_min:
						print("\n")
						print("Loan Application Eligible")
						loan_amount_maximum = ai * 0.12  # 12% of annual income
						print(f"Eligible Loan Amount: Rs {loan_amount_maximum}")

						santion_loan=int(input("Enter the loan amount needed: "))
						if (santion_loan<=loan_amount_maximum):

							print("Generating the Loan ID number now...")
							Lo_id=''.join(random.choice(string.digits) for i in range(8))

							p = santion_loan
							r = int(input("Enter the rate of interest "))
							n = int(input("Enter the number of years "))

							t = (p*r*n*10)/100
							print("The total interest to be paid is:",t)
							print("\n")
							m = (p+t)/(n*10)
							print("The  monthly payment amount is:",m)

							d1="select Name from AdemBank where Accountnumber='{}'".format(u)
							mycursor.execute(d1)
							nme=mycursor.fetchone()[0]

							Lo_id1="insert into customerloan values('{}','{}','{}','{}','{}','{}','{}','{}')".format(Lo_id,u,p,n,r,m,t,nme)
							mycursor.execute(Lo_id1)
							mydb.commit()
							
						else:
							print("\n")
							print("Loan can be approved only for 12% of your annual income which is around Rs:",loan_amount_maximum )

					else:
						print("\n")
						print("Annual Income is  ",ai,"and Age is  ",user_age, "against Minimum Annual income of 200000 and Minimum age of 23" )
						print("Loan Application Not Eligible")
				else:
					print("\n")
					print("User not found. Please check the AccountNumber and Password.")

			else:
				print("No more tasks")
				exit()


	if(ch==2):
		u=input("Enter Your AccountNumber : ")
		p=input("Enter Your Password : ")
		a="select * from AdemBank where AccountNumber='{}' and Password='{}'".format(u,p)
		mycursor.execute(a)
		data=mycursor.fetchall()
		if data:
			while True:
				d1="select Name from AdemBank where Accountnumber='{}'".format(u)
				mycursor.execute(d1)
				nme=mycursor.fetchone()[0]
				print("\n")
				print("\n")
				print("*************         Welcome",nme,"!!!","      *****************")
				print("\n")
				print("Press 1 to Withdraw Money")
				print("Press 2 to Deposit Money")
				print("Press 3 to View Last Five Transaction ")
				print("Press 4 to View Your Profile ")
				print("Press 5 to Check Eligibility for a loan")
				print("Press 6 to Log Out")

				ch1=int(input("Enter Your Choice : "))

				if(ch1>=7):
					print(" Invalid Input ")
				if(ch1==1):
					np="select Balance from AdemBank where AccountNumber='{}'".format(u)
					mycursor.execute(np)
					bal=mycursor.fetchone()[0]
				
					print("Your Account Balance is : " ,bal)

					while True:
						a1=int(input("Enter the amount for withdrawal: "))
				
						if a1<=bal:
							credited=0
						
							t6="update AdemBank set Balance=Balance - '{}' where AccountNumber='{}'".format(a1,u)
							mycursor.execute(t6)
							mydb.commit()


							bp="insert into Transactions values('{}','{}','{}')".format(credited,a1,u)
							mycursor.execute(bp)
							mydb.commit()

							np9="select Balance from AdemBank where AccountNumber='{}'".format(u)
							mycursor.execute(np9)
							bal1=mycursor.fetchone()[0]

							print("\n")
							print("Your AccountNumber:" ,u , "is debited with Rs" , a1 )
							print("towards Net Banking. Available balance is Rs : " , bal1, " ₹ only ")
							break

						else:

							print("   ********* Insufficient Balance Please Try Again !  **********")
							break
				elif(ch1==2): 
					debited=0

					while True:
						a11=(input("Enter the amount to deposit : "))

						t6= "update AdemBank set Balance=Balance +'{}' where AccountNumber='{}'".format(a11,u)
						mycursor.execute(t6)
						mydb.commit()

						mn="insert into Transactions values('{}','{}','{}')".format(a11,debited,u)
						mycursor.execute(mn)
						mydb.commit()

						np9="select Balance from AdemBank where AccountNumber='{}'".format(u)
						mycursor.execute(np9)
						bal2=mycursor.fetchone()[0]

						print("\n")
						print("Your AccountNumber:" ,u , "is Credited with Rs" , a11 )
						print("towards Net Banking. Available balance is Rs : " , bal2, " ₹ only")
						break


				elif(ch1==3):
					prt="Select Credited,Debited from Transactions where Accountnumber1='{}'".format(u)
					mycursor.execute(prt)
					print("*************** The Transaction Details are as Follows*********************")
					print("\n")
					for i in mycursor:
						print("Credited , Debited  : " ,i)
					d8="select Balance from AdemBank where AccountNumber='{}'".format(u)
					mycursor.execute(d8)
					bal=mycursor.fetchone()[0]
					print("\n")
					print("Account Balance		: ",bal)
					print("________________________________")


				elif(ch1==4):
					
					print("_________________________________________________________________________________________________")
					print("**********************                    ACCOUNT DETAILS                *************************")
					print("__________________________________________________________________________________________________")

					d1="select Name from AdemBank where Accountnumber='{}'".format(u)
					mycursor.execute(d1)
					nme=mycursor.fetchone()[0]

					d2="select AccountNumber from AdemBank where Accountnumber='{}'".format(u)
					mycursor.execute(d2)
					act=mycursor.fetchone()[0]

					d3="select Password from AdemBank where Accountnumber='{}'".format(u)
					mycursor.execute(d3)
					pswd=mycursor.fetchone()[0]

					d4="select Address from AdemBank where Accountnumber='{}'".format(u)
					mycursor.execute(d4)
					dtfbth=mycursor.fetchone()[0]

					d5="select Date_of_birth from AdemBank where Accountnumber='{}'".format(u)
					mycursor.execute(d5)
					addrs=mycursor.fetchone()[0]

					d6="select Mobile_Number from AdemBank where Accountnumber='{}'".format(u)
					mycursor.execute(d6)
					mobln=mycursor.fetchone()[0]

					d7="select Aadhar_no from AdemBank where Accountnumber='{}'".format(u)
					mycursor.execute(d7)
					adhr=mycursor.fetchone()[0]

					d8="select Balance from AdemBank where AccountNumber='{}'".format(u)
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

					# Loan application
					print("\n")
					print("Loan Application")
					print("\n")

					u = input("Enter Your AccountNumber: ")
					p = input("Enter Your Password: ")

					check_user_query = "SELECT * FROM AdemBank WHERE AccountNumber = %s AND Password = %s"
					mycursor.execute(check_user_query, (u, p))
					user_data = mycursor.fetchone()

					if user_data:
						dob="SELECT Date_of_birth FROM AdemBank where Accountnumber='{}'".format(u)
						mycursor.execute(dob)
						dob1=mycursor.fetchone()[0]
						
						user_age = date.datetime.now().year - dob1.year

						d1="select annual_income from AdemBank where Accountnumber='{}'".format(u)
						mycursor.execute(d1)
						ai=mycursor.fetchone()[0]

						# Assuming an annual income threshold for eligibility
						annual_income_min = 200000  # threshold
						age_min = 23  # Minimum age for eligibility

						if ai >= annual_income_min and user_age >= age_min:
							print("\n")
							print("Loan Application Eligible")
							loan_amount = ai * 0.12  # 12% of annual income
							print(f"Eligible Loan Amount: Rs {loan_amount}")
							print("Contact Bank Officials for processing the loan")
						# Implement loan application process here
						else:
							print("\n")
							print("Annual Income is  ",ai,"and Age is  ",user_age, "against Minimum Annual income of 200000 and Minimum age of 23" )
							print("Loan Application Not Eligible")
					else:
						print("\n")
						print("User not found. Please check the AccountNumber and Password.")
				elif(ch1==6):
					print("\n")
					print("*******        Thanks For Banking with us        *******")
					exit()
	else:
		print("\n")
		print("        Login Again to continue further operations	")
		exit()
		
