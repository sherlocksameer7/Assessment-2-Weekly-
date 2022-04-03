from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def setUp():
    global name,dob,address,pincode,mobile,email,password,confirmpass,driver
    name = input("Enter the name :")
    dob = input("enter the dob :")
    address = input("Enter the address :")
    pincode = input("Enter the pincode :")
    mobile = input("Enter the mobile :")
    email = input("Enter the email :")
    password = input("Enter the password :")
    confirmpass = input("Enter the password again !")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(10)
    driver.close()

def test_Program2_selenium(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/training.php")
    driver.find_element_by_xpath("/html/body/div/div/div[1]/form/table/tbody/tr[1]/td[2]/input").send_keys(email)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[1]/form/table/tbody/tr[2]/td[2]/input").send_keys(password)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[1]/form/table/tbody/tr[3]/td[2]/button").click()
    time.sleep(2)
    driver.find_element_by_name("name").send_keys(name)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input[1]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[3]/td[2]/select/option[4]").click()
    time.sleep(2)
    driver.find_element_by_name("dob").send_keys(dob)
    time.sleep(2)
    driver.find_element_by_name("Address").send_keys(address)
    time.sleep(2)
    driver.find_element_by_name("Pincode").send_keys(pincode)
    time.sleep(2)
    driver.find_element_by_name("Mobile").send_keys(mobile)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[8]/td[2]/input").send_keys(email)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[9]/td[2]/input").send_keys(password)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[10]/td[2]/input").send_keys(confirmpass)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[11]/td[2]/div/input").send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[12]/td[2]/button").click()