from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AE_LoginPage:
    
    #constructor
    def __init__(self,driver):
        self.driver=driver
    
    
    loginEmail_textbox_css="input[data-qa='login-email']"
    loginPassword_textbox_css="input[data-qa='login-password']"
    login_button_css="button[data-qa='login-button']"
    logout_link_css="a[href='/logout']"
    loginMessage_text_xpath="//a[contains(text(),'Logged in as')]"
    invalidLoginMessage_text_xpath="//p[normalize-space()='Your email or password is incorrect!']"
    
    
  
    def enterLoginemail(self,emailid):
        self.driver.find_element(By.CSS_SELECTOR,self.loginEmail_textbox_css).send_keys(emailid)
       
        
       
       
    def enterLoginPassword(self,password):
        self.driver.find_element(By.CSS_SELECTOR,self.loginPassword_textbox_css).send_keys(password)
       
    
    def clickLoginButton(self):
        self.driver.find_element(By.CSS_SELECTOR,self.login_button_css).click()
       
    def clickLogoutLink(self):
        self.driver.find_element(By.CSS_SELECTOR,self.logout_link_css).click()
             
    
    
    # Inside AE_LoginPage class
    def checkLoginSuccessMsg(self):
        loginMsg = self.driver.find_element(By.XPATH, self.loginMessage_text_xpath).text
        print(loginMsg)
        return loginMsg
    
    def checkInvalidLoginMessage(self):
        invalidLoginMessageEle = self.driver.find_element(By.XPATH,self.invalidLoginMessage_text_xpath)       
        invalidLoginMsg=invalidLoginMessageEle.text
        return invalidLoginMsg                               