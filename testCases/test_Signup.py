import pytest

from utilities.customLogger import LogGen

from pageObjects.ae_HomePage_POM import AE_HomePage
from pageObjects.ae_SignupPage_POM import AE_SignupPage
from utilities.readConfigProperties import ReadConfigProperties

@pytest.mark.order(1)
class Test_001_Signup:
    
    logger = LogGen.logGeneration()
    
    url=ReadConfigProperties.getApplicationURL()
    titlemale = ReadConfigProperties.getTitleMale()
    titlefemale = ReadConfigProperties.getTitleFemale()
    name = ReadConfigProperties.getName()
    spemail = ReadConfigProperties.getspEmail()
    sppassword = ReadConfigProperties.getSpPassword()
    day = ReadConfigProperties.getDay()
    month = ReadConfigProperties.getMonth()
    year = ReadConfigProperties.getYear()
    firstName = ReadConfigProperties.getFirstName()
    lastName = ReadConfigProperties.getLastName()
    address = ReadConfigProperties.getAddress()
    country = ReadConfigProperties.getCountry()
    state = ReadConfigProperties.getState()
    city = ReadConfigProperties.getCity()
    zipcode = ReadConfigProperties.getZipCode()
    mobilenumber = ReadConfigProperties.getMobileNumber()   
    
     
    
    def test_SignUp(self,setup):
        
        self.logger.info("*******test_SignUp***********")
        self.driver = setup
        self.driver.get(self.url)
        self.logger.info("*******Url fetched***********")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
        self.hp=AE_HomePage(self.driver)
        self.hp.clickSignup_Loginlink()
        self.logger.info("*******Clicked on Signup***********")
        
        self.sp=AE_SignupPage(self.driver)
        newUserSignupheading=self.sp.checkHeadingNewUserSignUp()
        self.logger.info("*******Checking New User Signup Heading***********")
        assert newUserSignupheading, "New User Signup heading not visible"
        
        self.sp.enterName(self.name)
        self.logger.info("*******First Name Entered***********")
        self.sp.enterEmail(self.spemail)
        self.logger.info("*******Email Entered***********")
        self.sp.clickSignUpButton()
        self.logger.info("*******Clicked on Signup button***********")
        
        actsignUpmsg = self.sp.checkSignupMessageEmailAlreadyExists()
        print(actsignUpmsg)
        if "Email Address already exist!" in actsignUpmsg:
            self.logger.info("*******Signup failed as Email already exists***********")
            self.driver.save_screenshot("./screenShot/Test_001_Signup_emailexists.png")
            assert False
        else:
            print("Proceeding with signup...")
        self.logger.info("*******New Email used for Signup***********")
        self.sp.selectTitle(self.titlemale)
        self.logger.info("*******Selected Title***********")
        self.sp.enterPassword(self.sppassword)
        self.logger.info("*******Password Created***********")
        self.sp.selectDOB(self.day,self.month,self.year)
        self.logger.info("*******Entering Account details***********")
        self.sp.enterFirstName(self.firstName)
        self.sp.enterLastName(self.lastName)
        self.logger.info("*******Entering address***********")
        self.sp.enterAddress(self.address)
        self.sp.selectCountry(self.country)
        self.sp.enterState(self.state)
        self.sp.enterCity(self.city)
        self.sp.enterZipCode(self.zipcode)
        self.sp.enterMobileNumber(self.mobilenumber)
        self.sp.clickCreateAccount()
        self.logger.info("*******Clicking account creation button***********")
        
        acctCreationMsg=self.sp.checkAccountCreation()
        if "ACCOUNT CREATED!" in acctCreationMsg:
            print("Account Signup Success")
            self.driver.save_screenshot("./screenShot/Test_001_Signup_pass.png")
            self.logger.info("*******Account Successfully created***********")
            assert True
        else:
            print(acctCreationMsg)
            self.driver.save_screenshot("./screenShot/Test_001_Signup_fail.png")
            self.logger.info("*******Account not created***********")
            assert False
                    
        self.sp.clickContinue()
        self.sp.clickLogout()
        self.logger.info("*******User Logged Out***********")
            
        
        
        
        