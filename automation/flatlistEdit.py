from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

BASE_URL = "http://123.200.2.57:60842"

# browser = webdriver.Chrome(executable_path='/home/tanvir/Downloads/chromedriver')
browser = webdriver.Firefox(executable_path='/home/tanvir/Downloads/geckodriver')
browser.get(BASE_URL + "/login")
                    #Login testcase will be execuated.



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

browser.get( BASE_URL + "/supervisor/user_dashboard" )
user   = browser.find_element_by_class_name("add_user")
user.click()
time.sleep(2)

browser.get( BASE_URL + "/supervisor/add_user" )
lastName = browser.find_element_by_id("id_lastName")
firstName = browser.find_element_by_id("id_firstName")
phone = browser.find_element_by_id("id_phone")
email = browser.find_element_by_id("id_email")
pinCode = browser.find_element_by_id("id_pinCode")
submit = browser.find_element_by_xpath("/html/body/div/div/div[3]/form/div/div[12]/button[1]")

lastName.send_keys( "Tania")
time.sleep(2)
firstName.send_keys( "Nasrin Sultana")
time.sleep(2)
phone.send_keys("08734567")
time.sleep(2)
email.send_keys( "100t@gmail.com")
time.sleep(2)
pinCode.send_keys( "123" )
time.sleep(2)

submit.click()
time.sleep(2)



                #Flatslist edit & update testcase will be execuated.

browser.get( BASE_URL + "/flats/add_flat" )


#browser.get( BASE_URL + "/flats/25/edit_flat" )


flatNumber = browser.find_element_by_name( "flatNumber" )
level = browser.find_element_by_name( "flatLevel" )
buildingNumber = browser.find_element_by_name( "buildingNumber" )
submit   = browser.find_element_by_id( "submit" )

flatNumber.clear()
level.clear()
buildingNumber.clear()


flatNumber.send_keys( "100" )
time.sleep(2)
level.send_keys( "200" )
time.sleep(2)
buildingNumber.send_keys( "Tania" )
time.sleep(2)

submit.click()

            #Flatslist Delete testcase will be execuated.

browser.get(BASE_URL + "/flats/")
time.sleep(2)
delete   = browser.find_element_by_class_name("delete_button")
delete.click()
time.sleep(1)
yes = browser.find_element_by_id("yes_delete_button")
yes.click()
time.sleep(2)
browser.get(BASE_URL + "/flats/")


#wait = WebDriverWait(browser, 5)
