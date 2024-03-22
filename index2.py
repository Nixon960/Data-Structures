#GROUP ONE
class BrowserStack:
    def __init__(self):
        self.stack = []
        self.current_page = None
    
    def navigation(self, url):
        if self.current_page is not None:
            self.stack.append(self.current_page)
            print(self.current_page)
        self.current_page = url
        return f"Current page: {self.current_page}"
    
    def backward(self):
        if self.stack:
            self.current_page = self.stack.pop()
            return f"Backward to: {self.current_page}"
        else:
            return "No previous page to go back"
    
    def forward(self):
        if self.current_page:
            return f"Forward to: {self.current_page}"
        else:
            return "No forward page"

pages = ["www.google.com", "www.github.com", "www.yahoo.com", "www.ucu.com", "www.microsoft.com", "www.skype.com"]
browser = BrowserStack()
print([browser.navigation(page) for page in pages])
print(browser.backward())
print(browser.backward())
print(browser.forward())
print(browser.navigation("www.3wschools.com"))
print(browser.forward())

#Odongokara Oscar 
#Kiisa Angela
#Mutumba Benjamin 
#Buwembo David Denzel 
#Nziriga Isaac Nickson
