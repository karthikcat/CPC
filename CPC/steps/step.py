from behave import *
from selenium import webdriver
from time import sleep
class CPC:
    @given("open CPC application in firefox")
    def step1(content):
        content.fb=webdriver.FirefoxProfile("C:/Users/kartseka/AppData/Roaming/Mozilla/Firefox/Profiles/cmjlc4p3.default-1483087944543")
        content.driver=webdriver.Firefox(content.fb)
        content.driver.get("http://10.78.239.156/cupm/common/index.jsp")
        content.driver.implicitly_wait(60)
    @when('Enter the username as "{username}"')
    def step2(content,username):
        content.driver.implicitly_wait(60)
        content.driver.find_element_by_xpath(".//*[@id='widget_loginPage_username']").click()
        sleep(2)
        content.driver.find_element_by_xpath(".//*[@id='widget_loginPage_username']").send_keys(username)
    @when('Enter the password as "{password}"')
    def step3(content,password):
        content.driver.implicitly_wait(60)
        content.driver.find_element_by_xpath(".//*[@id='loginPage_password']").send_keys(password)
    @then("Press the Login Button")
    def step4(content):
        content.driver.implicitly_wait(60)
        content.driver.find_element_by_xpath(".//*[@id='loginPage']/div/div[6]/div[7]/div[1]/span[1]/span").click()
    @then("Close the Broswer")
    def step5(content):
        sleep(25)
        content.driver.quit()   