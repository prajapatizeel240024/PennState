from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to the website
url = 'https://www.google.com/'
driver.get(url)

# Give the page some time to load
time.sleep(2)

# Locate the search textbox and send keys
textbox = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')  # Replace with correct XPath if needed
textbox.send_keys("Hello world")

# Give some time to see the input before closing the browser
time.sleep(2)

# Close the driver
driver.quit()