import time
from selenium import webdriver

# importing By class that allows us to choose the element search method
from selenium.webdriver.common.by import By

#initialising the browser driver
driver = webdriver.Chrome()

#sleep command is pausing the command execution for a certain amount of seconds
time.sleep(5)

#get method makes browser open the given link
driver.get("https://suninjuly.github.io/text_input_task.html")
time.sleep(5)

#find_element method allows us to find the needed element on the website by specifying its path
#the method takes search type and value as arguements
#this time we are searching for text area
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

#now we are putting the response text into the found field
textarea.send_keys("get()")
time.sleep(5)

#and then let's find the submit button
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

#now we will tell driver to push the button. After this command we should see an answer that response was right
submit_button.click()
time.sleep(5)

#after everything is done, we shouldn't forget to close the browser window
driver.quit()
