from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

BASE_URL = "http://123.200.2.57:60842"

# browser = webdriver.Chrome(executable_path='/home/tanvir/Downloads/chromedriver')
browser = webdriver.Firefox(executable_path='/home/tanvir/Downloads/geckodriver')
browser.get(BASE_URL + "/login")

phone = browser.find_element_by_name( "inputPhone" )
pin = browser.find_element_by_name( "inputPin" )
submit   = browser.find_element_by_id( "submit" )

phone.clear()
pin.clear()
phone.send_keys( "01676835883" )
time.sleep(1)
pin.send_keys( "1212" )
time.sleep(1)
submit.click()
time.sleep(2)


browser.get( BASE_URL + "/flats/add_flat" )
flatNumber = browser.find_element_by_name( "flatNumber" )
level = browser.find_element_by_name( "flatLevel" )
buildingNumber = browser.find_element_by_name( "buildingNumber" )
submit   = browser.find_element_by_id( "submit" )

flatNumber.send_keys( "B-1" )
time.sleep(2)
level.send_keys( "4" )
time.sleep(2)
buildingNumber.send_keys( "Tania" )
time.sleep(2)
submit.click()


wait = WebDriverWait(browser, 5)

try:
    page_loaded = wait.until_not(
    lambda browser: browser.current_url == login_page
)
except TimeoutException:
    self.fail( "Loading timeout expired" )

self.assertEqual(
    browser.current_url,
    correct_page,
    msg = "Successful Login"
)
