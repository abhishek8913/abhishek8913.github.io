from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import random

#random number of texts
text_number_goal =random.randint(25, 35)
# Install Chrome WebDriver
chrome_driver_path = ChromeDriverManager().install()

# Create a Chrome WebDriver
driver = webdriver.Chrome()

RecievedMessage=[]
NotFoundUser=[]

# Open Instagram
driver.get('https://www.instagram.com/accounts/login/')

#COUNTER TO PREVENT TOO MANY DMS
DM_count=0

# Read the Excel file into a pandas DataFrame
df = pd.read_excel('USERS.xlsx')

# # Get the first 5 values from the 'USER NAME' column
# UsersArray = df['USER NAME'].head(5).tolist()
#UsersArray = df['USER NAME'].tolist()
UsersArray = df['USER NAME'].head(text_number_goal).tolist()

# Load the Excel file into a Pandas dataframe
df_DELETE = pd.read_excel("USERS.xlsx")

# Delete the first 5 rows
df_DELETE = df_DELETE.iloc[text_number_goal:]

# Save the modified dataframe back to the Excel file
df_DELETE.to_excel("USERS.xlsx", index=False)

print(UsersArray)


# LOGIN CREDENTIALS
UserName='***' #enter instagram username
password='***' #enter instagram pass

try:
    # Wait for the login page to load (adjust the time as needed)
    driver.implicitly_wait(random.randint(7, 9))

    # Locate the input field using the specified XPath
    input_field = driver.find_element(By.XPATH, '//input[@name="username"]')

    # Send a value to the input field
    input_field.send_keys(UserName)

    # Locate the password field using the specified XPath
    password_field = driver.find_element(By.XPATH, '//input[@name="password"]')

    # Send a value to the password field
    password_field.send_keys(password)

    # Submit the form
    password_field.submit()

    # Delay so that Login is done completely
    time.sleep(random.randint(12, 28))



except Exception as e:
    print(f"An error occurred: {e}")





for Customer in UsersArray:



    # Navigate to DM Page after Successful Login
    driver.get('https://www.instagram.com/direct/inbox/?next=%2F')

    try:
        # In case a popup appears for enabling notification
        NotNowButton = driver.find_element(By.XPATH, '//button[@class="_a9-- _ap36 _a9_1"]')
        NotNowButton.click()
    except:
        print("Not now button not found")


    # Flag that checks if user is found
    userFlag=1

    # Flag to check if message is sent
    MessageSent=1



    try:
        # Click on the New Chat button from where users will be searched
        NewChatButton = driver.find_element(By.XPATH, '//div[@class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x9bdzbf x1ypdohk x78zum5 x1f6kntn xwhw2v2 x10w6t97 xl56j7k x17ydfre x1swvt13 x1pi30zi x1n2onr6 x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 x1i0vuye x1tu34mt xzloghq" and contains(text(), "Send message")]')
        NewChatButton.click()
        print("NewChatButton Clicked")

        time.sleep(random.randint(0, 5))


    except:
        print("New Chat button not found")
    try:
        # Locate the user Search field using the specified XPath
        SearchUser_field = driver.find_element(By.XPATH, '//input[@class="x5ur3kl xopu45v x1bs97v6 xmo9t06 x1j8ye7u x1rjkts5 x13z9klp xjc6cxp x178xt8z xm81vs4 xso031l xy80clv x5n08af x1iyjqo2 xvs91rp xklk4pu xdj266r x11i5rnm xat24cr x1mh8g0r x1plvlek xryxfnj x1iorvi4 xn6708d xjkvuk6 x1s3xk63 xlqc9nw x8tigb1 x1ad04t7 x1glnyev xs3hnx8 x7xwk5j x1rheh84 x1ck6gwh x175bfct x1meze4m x10eltez x1qt4tve x1s07b3s xkq2eht x1rvh84u x1ejq31n xd10rxx x1sy0etr x17r0tee x5ib6vp xjbqb8w xzd0ubt"]')

        # Send a value to the USer Search field
        SearchUser_field.send_keys(Customer)
    except:

        try:
            # Locate the user Search field using the XPath in case previous XPATH did not work
            SearchUser_field = driver.find_element(By.XPATH, '//input[@placeholder="Search..."]')

            # Send a value to the search field
            SearchUser_field.send_keys(Customer)
        except:
            try:
                # Locate the user Search field using the XPath in case previous XPATH did not work
                SearchUser_field = driver.find_element(By.XPATH, '//input')

                # Send a value to the search field
                SearchUser_field.send_keys(Customer)
            except:
                print("Search field not found")


        try:
            # After typing in username, list of users popup, so we need to match the username with the required user
            Users = driver.find_elements(By.XPATH, '//div[@class="x9f619 x1ja2u2z x1k90msu x6o7n8i x1qfuztq x10l6tqk x17qophe x13vifvy x1hc1fzr x71s49j xh8yej3"]//div[@class="x9f619 x1n2onr6 x1ja2u2z x78zum5 x2lah0s x1qughib x6s0dn4 xozqiw3 x1q0g3np"]//div[@class="x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x2lah0s x193iq5w xeuugli x1iyjqo2"]//span[@class="x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft"]')

            for user in Users:
                Uname= user.get_attribute('innerHTML')
                print('UName ',Uname)

                if Uname.lower() == Customer.lower():
                    print("User Matched")
                    user.click()
                    userFlag=1
                    print("User Clicked")
                    break

                else:
                    userFlag=0
                    print("User Not Found")


        except:
            print("User not found")


        if userFlag==0:
           # NotFoundUser.append(Customer)
            continue


        elif userFlag==1:
            try:

                # After User is found successfully a chat button will pop up.
                ChatButton = driver.find_element(By.XPATH, '//div[@class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x9bdzbf x1ypdohk x78zum5 x1f6kntn xwhw2v2 xl56j7k x17ydfre x1n2onr6 x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 x1i0vuye xn3w4p2 x5ib6vp xc73u3c x1tu34mt xzloghq"]')
                ChatButton.click()
                print("ChatButton Clicked")

                time.sleep(random.randint(2, 6))


            except:
                print("Chat button not found")



            try:
                 # Locate the MEssage field using the specified XPath
                message_field = driver.find_element(By.XPATH, '//div[@aria-label="Message"]')

                # Send message to the message field
                message_field.send_keys("Hey my name is ****, I’m a short form content expert . I’m reaching out cause I’d love to work with you . Plenty of samples available on my profile! Looking forward to working with you .")


                try:

                    # Locate the send button after message is typed
                    SendMessageButton = driver.find_element(By.XPATH, '//div[@class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 x1i0vuye xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp x173jzuc x1yc6y37 xfs2ol5"]')
                    SendMessageButton.click()
                    MessageSent=1
                    print("SendMessageButton Clicked")
                    time.sleep(random.randint(3, 6))


                except:

                    try:
                        # In case send button was not found press the ENTER key
                        message_field.send_keys(Keys.RETURN)
                        MessageSent=1
                    except:
                        MessageSent=0

                        print("SendMessageButton button not found")


            except:
                print("No message sent")


            if MessageSent==1:
                # Even if bot is stopped a sheet with remaining users will be created
               # RecievedMessage.append(Customer)
                # Remove rows where 'USER NAME' matches elements in RecievedMessage
                #df_remaining = df[~df['USER NAME'].isin(RecievedMessage)]

                # Save the remaining data to a new Excel file
                #df_remaining.to_excel('RemainingUsers.xlsx', index=False)
                #update the number of max Dm's at a time
                DM_count+=1
                if DM_count > text_number_goal: #start with 35 DMs a day and work up
                    print("Safety limit exceeded now exiting")
                    driver.quit() #exits so that the user isnt banned

                time.sleep(random.randint(2,4))






# Close the browser window
driver.quit()

