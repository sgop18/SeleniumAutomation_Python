import configparser

config=configparser.RawConfigParser()
config.read("./configurations/config.ini")

class ReadConfigProperties:
    
    @staticmethod
    def getApplicationURL():
        url=config.get('Application URL info', 'url')
        return url
    
    @staticmethod
    def getValidUserLoginEmail():
        email=config.get('ValidUserLogin info', 'email1')
        return email
    
    @staticmethod    
    def getValidUserLoginPassword():
        password=config.get('ValidUserLogin info', 'password')
        return password
    
    @staticmethod
    def getInvalidUserLoginEmail():
        email=config.get('InvalidUserLogin info', 'email1')
        return email
        
    @staticmethod
    def getInvalidUserLoginPassword():
        password=config.get('InvalidUserLogin info', 'password')
        return password
    
    @staticmethod
    def getName():
        name=config.get('Signup info', 'name')
        return name
    
    @staticmethod
    def getspEmail():
        spemail=config.get('Signup info', 'spemail')
        return spemail
    
    @staticmethod
    def getTitleMale():
        title=config.get('Signup info', 'titlemale')
        return title
    
    @staticmethod
    def getTitleFemale():
        female=config.get('Signup info', 'titlefemale')
        return female
    
    @staticmethod
    def getSpPassword():
        sppassword=config.get('Signup info', 'sppassword')
        return sppassword
    
    @staticmethod
    def getDay():
        day=config.get('Signup info', 'day')
        return day
    
    @staticmethod
    def getMonth():
        month=config.get('Signup info', 'month')
        return month
    
    @staticmethod
    def getYear():
        year=config.get('Signup info', 'year')
        return year
    
    @staticmethod
    def getFirstName():
        firstName=config.get('Signup info', 'firstName')
        return firstName
    
    @staticmethod
    def getLastName():
        lastName=config.get('Signup info', 'lastName')
        return lastName
    
    @staticmethod
    def getAddress():
        address=config.get('Signup info', 'address')
        return address
    
    @staticmethod
    def getCountry():
        country=config.get('Signup info', 'country')
        return country
    
    @staticmethod
    def getState():
        state=config.get('Signup info', 'state')
        return state
    
    @staticmethod
    def getCity():
        city=config.get('Signup info', 'city')
        return city
    
    @staticmethod
    def getZipCode():
        zipcode=config.get('Signup info', 'zipcode')
        return zipcode
    
    @staticmethod
    def getMobileNumber():
        mobilenumber=config.get('Signup info', 'mobilenumber')
        return mobilenumber
        


