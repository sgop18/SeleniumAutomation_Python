import pytest

from pageObjects.ae_HomePage_POM import AE_HomePage
from pageObjects.ae_LoginPage_POM import AE_LoginPage
from utilities.readConfigProperties import ReadConfigProperties
from utilities.customLogger import LogGen

@pytest.mark.order(2)
class Test_002_Login:
    logger = LogGen.logGeneration()
    
    url=ReadConfigProperties.getApplicationURL()
    vemail=ReadConfigProperties.getValidUserLoginEmail()
    vpassword=ReadConfigProperties.getValidUserLoginPassword()
    invemail=ReadConfigProperties.getInvalidUserLoginEmail()
    invpassword=ReadConfigProperties.getInvalidUserLoginPassword() 
    
       
    def test_HomePageTitle(self,setup): 
        self.logger.info("*******test_HomePageTitle***********")       
        self.driver=setup
        self.driver.get(self.url)
        self.logger.info("*******Fetching Url***********")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
        act_title=self.driver.title
        if act_title == "Automation Exercise":
            self.logger.info("*******Title matches expected Title***********")
            assert True
        else:
            self.driver.save.screenshot("./screenShots/test_HomePageTitle.png")
            self.logger.info("*******Wrong Title***********")
            self.driver.close()
            
    # Inside your test class
    def test_Login_ValidUser(self, setup):
        self.logger.info("*******test_Login_ValidUser***********")
        self.driver = setup
        self.driver.get(self.url)
        self.logger.info("*******Fetching Url***********")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = AE_HomePage(self.driver)
        self.hp.clickSignup_Loginlink()
        self.logger.info("*******Clicked on Login Link***********")

        self.lp = AE_LoginPage(self.driver)
        self.lp.enterLoginemail(self.vemail)
        self.logger.info("*******Entered Login email***********")
        self.lp.enterLoginPassword(self.vpassword)
        self.logger.info("*******Entered Login password***********")
        self.lp.clickLoginButton()

        actLoginMsg = self.lp.checkLoginSuccessMsg()        
        if "Logged in as" in actLoginMsg:
            self.driver.save_screenshot("./screenShot/test_Login_ValidUser_loginsuccess.png")
            self.logger.info("*******Login Successful for Valid user***********")
            assert True
        else:
            self.driver.save_screenshot("./screenShot/test_Login_ValidUser_loginfail.png")
            self.logger.info("*******Login Failed for Valid User***********")
            assert False

            
     
    def test_Login_InvalidUser(self,setup):         
        self.driver=setup
        self.logger.info("*******test_Login_InvalidUser***********")
        self.driver.get(self.url)
        self.logger.info("*******Fetching Url***********")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
        self.hp=AE_HomePage(self.driver)
        self.hp.clickSignup_Loginlink()
        self.logger.info("*******Clicked Login Link***********")
        
        self.lp=AE_LoginPage(self.driver)
        self.lp.enterLoginemail(self.invemail)
        self.logger.info("*******Entered invalid Email***********")
        self.lp.enterLoginPassword(self.invpassword)
        self.logger.info("*******Entered invalid password***********")
        self.lp.clickLoginButton()
        
        actInvalidLoginMsg = self.lp.checkInvalidLoginMessage()     
        
        if "Your email or password is incorrect!" in actInvalidLoginMsg:
            self.driver.save_screenshot("./screenShot/test_Login_InvalidUser_expected.png")
            self.logger.info("*******User Unable to login with invalid Email - Success***********")
            assert True            
        else:
            print("Login Failure.User allowed to login with wrong email/password")
            self.driver.save_screenshot("test_Login_InvalidUser_Notexpected.png")
            self.logger.info("*******User able to login with invalid email - Failure***********")
            assert False
            
        
        
        
        
        
        
            
            
    
        
        