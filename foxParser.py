from selenium import webdriver

from selenium.webdriver.firefox.options import Options


options = Options()

options.add_argument("--headless")

# options.add_argument( "--screenshot test.jpg http://google.com/" )

driver = webdriver.Firefox(firefox_options=options,
                           executable_path='/app/firefoxdriver/geckodriver')

driver.get('http://google.com/')

driver.save_screenshot('test.png')

print(driver.title)

print(driver.current_url)

driver.quit()
