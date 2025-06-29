from utilities.customLogger import LogGen
from pageObjects.ae_HomePage_POM import AE_HomePage
from pageObjects.ae_LoginPage_POM import AE_LoginPage
from utilities.readConfigProperties import ReadConfigProperties
from utilities import excelUtils
import pytest

class Test_003_DeleteUser_DDT:
    
    logger=LogGen.logGeneration()
    excelpath = "./testData/deleteUserList.xlsx"
    url=ReadConfigProperties.getApplicationURL()
    
    @pytest.mark.regression
    def test_DeleteUser_DDT(self,setup):
        self.logger.info("*******Test_003_DeleteUser_DDT***********")
        self.driver = setup
        self.hp = AE_HomePage(self.driver)
        self.lp = AE_LoginPage(self.driver)
        
        self.logger.info("*******test_DeleteUser_DDT***********")
        self.driver.get(self.url)
        self.logger.info("*******Fetching Url***********")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
        
        
        self.hp.clickSignup_Loginlink()
        self.logger.info("*******Clicking Login Link***********")
        
        
        
        self.rows=excelUtils.getRowCount(self.excelpath,"Deleteuser")
        self.cols=excelUtils.getColCount(self.excelpath,"Deleteuser")
        
        
        for r in range(1,self.rows+1):
            
            tobeDeleted = excelUtils.readData(self.excelpath,"Deleteuser",r,3)
            loginEmail=excelUtils.readData(self.excelpath,"Deleteuser", r, 1)
            password=excelUtils.readData(self.excelpath, "Deleteuser", r, 2)
            print("to be deleted = "+ tobeDeleted + "and Loginemail = " +loginEmail )
            
            if "Yes" in tobeDeleted:
                try:
                    
                    self.lp.enterLoginemail(loginEmail)
                    self.logger.info("*******Entering email***********")
                    self.lp.enterLoginPassword(password)
                    self.logger.info("*******Entering password***********")
                    self.lp.clickLoginButton()
                    self.logger.info("*******Logging in***********")
                    
                    actInvalidLoginMsg = self.lp.checkInvalidLoginMessage()
                    if "Your email or password is incorrect!" not in actInvalidLoginMsg:
                        self.logger.info("*******Cliking Delete Account***********")
                        self.hp.clickDeleteAccount()                    
                        actDelMsg = self.hp.checkAccountDelectedMessage()
                        self.logger.info("*******Checking account deleted message***********")
                        if "Account deleted" in actDelMsg:
                            self.logger.info("*******Updating Excel***********")
                            excelUtils.writeData(self.excelpath,"Deleteuser",r,4,"Deleted")
                            self.hp.clickContinueButton()
                            assert True
                        else:
                            self.logger.info("*******Not deleted***********")
                    else:
                        self.driver.save_screenshot("./screenShot/test_DeleteUser_DDT_Loginfail.png")
                        self.logger.info("*******User Login failure***********")
                        assert False
                except Exception as e:
                    self.logger.error(f"Error processing row {r}: {str(e)}")
                    excelUtils.writeData(self.excelpath, "Deleteuser", r, 4, "Error")
                    self.driver.save_screenshot(f"./screenShot/error_row_{r}.png")
            elif "No" in tobeDeleted:
                loginEmail = excelUtils.readData(self.excelpath, "Deleteuser", r, 1)
                print("Account Not to be Deleted  -" + loginEmail)
                self.logger.info("*******Account Not to be Deleted***********")
                excelUtils.writeData(self.excelpath, "Deleteuser", r, 4, "Not Deleted") 
            else:
                self.logger.warning(f"Invalid 'ToDelete' flag in row {r}: {tobeDeleted}")
                excelUtils.writeData(self.excelpath, "Deleteuser", r, 4, "Invalid Flag")      
                self.logger.info("Reading next row")
                
                
            
        
        
        
        
        
        
        
       
         
         
        
        
        
        
        
        
        
        
        
        