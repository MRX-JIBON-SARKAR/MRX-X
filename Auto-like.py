#Write By Zahirul
Github: https://github.com/MRX-JIBON-SARKAR
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

Set up the webdriver (replace the path with the location of your chromedriver)
driver = webdriver.Chrome('/path/to/chromedriver')

 List of Facebook IDs to like posts for
fb_ids = ['id1', 'id2', 'id3']

 Login to Facebook
driver.get('https://www.facebook.com')
email_field = driver.find_element_by_id('email')
password_field = driver.find_element_by_id('pass')
email_field.send_keys('your_facebook_email')
password_field.send_keys('your_facebook_password')
password_field.send_keys(Keys.RETURN)

 Like posts for each Facebook ID
for fb_id in fb_ids:
    driver.get(f'https://www.facebook.com/{fb_id}')
    time.sleep(5)  # Wait for the page to load
    like_buttons = driver.find_elements_by_xpath("//a[@aria-label='Like']")
    for button in like_buttons:
        button.click()
        time.sleep(2)  # Wait for the like to register

# Close the browser
driver.quit()
