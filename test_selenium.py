from selenium import webdriver

from time import sleep

options = webdriver.ChromeOptions()

options.binary_location = '/home/gael/Projects/argonaultes/education/epsi-i1-reinforcement-learning/chrome-linux64/chrome'

service = webdriver.ChromeService(executable_path='/home/gael/Projects/argonaultes/education/epsi-i1-reinforcement-learning/chromedriver-linux64/chromedriver')

driver = webdriver.Chrome(options=options, service=service)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

sleep(5)

driver.get("http://127.0.0.1:5000")

sleep(5)