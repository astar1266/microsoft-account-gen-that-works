import random
import string
import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Function to generate a random email address
def random_email():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10)) + "@hotmail.com"

# Open a new Edge browser window and navigate to the Microsoft account sign-up page
# note the part where it says webdriver.edge u can change that to your browser for example if u have chrome u will put webdriver.chrome and put your chrome path.
driver = webdriver.Edge(executable_path="     put your path here for example:        C:\\Users\\admin\\Documents\\edgeweb\\msedgedriver.exe")
driver.get("https://signup.live.com/")

time.sleep(4)

# Fill in the account information
email_input = driver.find_element(By.ID, "MemberName")
email = random_email()
email_input.send_keys(email)

submit_button = driver.find_element(By.ID, "iSignupAction")
submit_button.click()

time.sleep(7)

password_input = driver.find_element(By.ID, "PasswordInput")
password_input.send_keys("Epicpassword123")

time.sleep(7)

submit_button = driver.find_element(By.ID, "iSignupAction")
submit_button.click()

time.sleep(7)

# Wait for the page to load and navigate to the next step
time.sleep(3)
driver.find_element(By.ID, "FirstName").send_keys("John")
driver.find_element(By.ID, "LastName").send_keys("Doe")

submit_button = driver.find_element(By.ID, "iSignupAction")
submit_button.click()


time.sleep(5)

driver.find_element(By.ID, "BirthMonth").send_keys("January")
driver.find_element(By.ID, "BirthDay").send_keys("1")
driver.find_element(By.ID, "BirthYear").send_keys("1990")
driver.find_element(By.ID, "iSignupAction").click()

time.sleep(7)

# Add a phone number and recovery email address
time.sleep(3)


# locate the select element using xpath
select_element = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[5]/div[1]/div[1]/select')

# create a Select object from the select element
select = Select(select_element)

# select the option by its value
select.select_by_value('+000')

time.sleep(7)

# Confirm the account creation
time.sleep(3)
driver.find_element(By.ID, "idBtn_Back").click()

# Close the browser window
driver.quit()
