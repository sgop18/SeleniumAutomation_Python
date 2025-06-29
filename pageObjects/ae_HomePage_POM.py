from selenium import webdriver
from selenium.webdriver.common.by import By


class AE_HomePage:

    def __init__(self,driver):   #driver will come from testcase
        self.driver=driver
    
   
    signup_login_link_css= "a[href='/login']"
    cart_link_xpath= "//body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]"
    deleteAccount_Link_xpath="//a[href='/delete_account']"
    accountDeletedMessage_text_xpath="h2[data-qa='account-deleted']"
    continue_button_xpath="a[data-qa='continue-button']"

    
    def clickSignup_Loginlink(self):
        self.driver.find_element(By.CSS_SELECTOR,self.signup_login_link_css).click()
        
    
    
    def clickCartLink(self):
        self.driver.find_element(By.XPATH,self.cart_link_xpath).click()
        
    def clickDeleteAccount(self):
        self.driver.find_element(By.XPATH,self.deleteAccount_Link_xpath).click()
        
    def checkAccountDelectedMessage(self):
        delMsg=self.driver.find_element(By.XPATH,self.accountDeletedMessage_text_xpath).text
        return delMsg
    
    def clickContinueButton(self):
        self.driver.find_element(By.XPATH,self.continue_button_xpath)
        
        
    