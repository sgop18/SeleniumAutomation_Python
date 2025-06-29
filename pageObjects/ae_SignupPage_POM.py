
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

class AE_SignupPage:
    def __init__(self,driver):
        self.driver=driver
        
    newUserSignup_message_xpath="//h2[normalize-space()='New User Signup!']"
    name_textbox_xpath="//input[@placeholder='Name']"
    email_textbox_xpath="//input[@data-qa='signup-email']"
    signup_button_css="button[data-qa='signup-button']"
    signupMessage_text_xpath="//p[normalize-space()='Email Address already exist!']"
    male_rbutton_id="id_gender1"
    female_rbutton_id="id_gender2"
    password_textbox_id="password"
    day_dropdown_id="days"
    month_dropdown_id="months"
    year_dropdown_id="years"
    firstName_textbox_id="first_name"
    lastName_textbox_id="last_name"
    address_textbox_id="address1"
    country_dropdown_id="country"
    state_textbox_id="state"
    city_textbox_id="city"
    zipcode_textbox_id="zipcode"
    mobilenumber_textbox_id="mobile_number"
    createAccount_button_css="button[data-qa='create-account']"
    accountCreated_message_css="h2[data-qa='account-created']"
    continue_button_linkText="Continue"
    logout_link_css="a[href='/logout']"
    
    def checkHeadingNewUserSignUp(self):
        newusersignupheading = self.driver.find_element(By.XPATH,self.newUserSignup_message_xpath).is_displayed()
        return newusersignupheading
    
    def enterName(self,name):
        self.driver.find_element(By.XPATH,self.name_textbox_xpath).clear()
        self.driver.find_element(By.XPATH,self.name_textbox_xpath).send_keys(name)
        
    def enterEmail(self,email):
        self.driver.find_element(By.XPATH,self.email_textbox_xpath).clear()
        self.driver.find_element(By.XPATH,self.email_textbox_xpath).send_keys(email)
        
    def clickSignUpButton(self):
        self.driver.find_element(By.CSS_SELECTOR,self.signup_button_css).click()
        

    def checkSignupMessageEmailAlreadyExists(self):
        try:
            emailexistsmsgEle = self.driver.find_element(By.XPATH, self.signupMessage_text_xpath)
            return emailexistsmsgEle.text
        except NoSuchElementException:
            return ""

        
    def selectTitle(self,title):
        title = title.strip().lower()
        if title == "male":
            self.driver.find_element(By.ID,self.male_rbutton_id).click()
        elif title == "female":
            self.driver.find_element(By.ID,self.female_rbutton_id).click()
            
    def enterPassword(self,password):
        self.driver.find_element(By.ID,self.password_textbox_id).send_keys(password)
        
    def selectDOB(self,day,month,year):
        self.driver.find_element(By.ID,self.day_dropdown_id).send_keys(day)
        self.driver.find_element(By.ID,self.month_dropdown_id).send_keys(month)
        self.driver.find_element(By.ID,self.year_dropdown_id).send_keys(year)
        
    def enterFirstName(self,firstName):
        self.driver.find_element(By.ID,self.firstName_textbox_id).send_keys(firstName)
        
    def enterLastName(self,lastName):
        self.driver.find_element(By.ID,self.lastName_textbox_id).send_keys(lastName)
        
    def enterAddress(self,address):
        self.driver.find_element(By.ID,self.address_textbox_id).send_keys(address)
        
    def selectCountry(self,country):
        select= Select(self.driver.find_element(By.ID,self.country_dropdown_id))
        for option in select.options:
            if country in option.text:
                option.click()
                break
            
    def enterState(self,state):
        self.driver.find_element(By.ID,self.state_textbox_id).send_keys(state)
        
    def enterCity(self,city):
        self.driver.find_element(By.ID,self.city_textbox_id).send_keys(city)
        
    def enterZipCode(self,zipcode):
        self.driver.find_element(By.ID,self.zipcode_textbox_id).send_keys(zipcode)
        
    def enterMobileNumber(self,mobilenumber):
        self.driver.find_element(By.ID,self.mobilenumber_textbox_id).send_keys(mobilenumber)
        
    def clickCreateAccount(self):
        self.driver.find_element(By.CSS_SELECTOR,self.createAccount_button_css).click()
        
    def checkAccountCreation(self):
        accountCreatedmsg=self.driver.find_element(By.CSS_SELECTOR,self.accountCreated_message_css).text
        print(accountCreatedmsg)
        return accountCreatedmsg
    
    def clickContinue(self):
        self.driver.find_element(By.LINK_TEXT,self.continue_button_linkText).click()
        
    def clickLogout(self):
        self.driver.find_element(By.CSS_SELECTOR,self.logout_link_css).click()
        
            
    
        
    
        
        
        
    
        
    

