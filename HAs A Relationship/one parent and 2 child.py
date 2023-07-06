#One BasePage and Two child Class.
# To understand the concept of selenium(how to write a code)
#It is a show case of Selenium but not actual pgm of selenium

class BasePage:
    
    def __init__(self,drive):
        self.drive=drive
        print("Default Constractor")
        
    def go_to_url(self,url):
        pass
    
    def read_file(self):
        pass
   
    def write_file(self):
        pass
    
class LoginPage(BasePage):
    
    def __init__(self,drive):
        super.__init__(drive)#Call Paent Constractor
        
    def enter_username(self,username):
        pass
    
    def enter_password(self,username):
        pass
    
    def click_login_button(self):
        pass
    
class HomePage(BasePage):
    
    def __init__(self,drive):
        super().__imit__(drive)
        
    def verify_login_success(self):
        pass
    
    def click_logout_button(self):
        pass
    
drive=BasePage()
login=LoginPage(drive)
login._go_to_url("url name") 
login.enter_password("admin")
login.enter_username("admin")
login.click_login_button()    
               