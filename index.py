class BrowserStack:
    def _init_(self):
        self.stack = []
        self.current_index = -1

    def navigation(self, url):
        self.stack = self.stack[:self.current_index + 1]
        self.stack.append(url)
        self.current_index += 1
        return f"Navigated to {url}"

    def backward(self):
        if self.current_index > 0:
            self.current_index -= 1
            return f"Backward to {self.stack[self.current_index]}"
        else:
            return "Can't go backward"

    def forward(self):
        if self.current_index < len(self.stack) - 1:
            self.current_index += 1
            return f"Forward to {self.stack[self.current_index]}"
        else:
            return "Can't go forward"

pages = ["www.google.com", "www.github.com", "www.yahoo.com", "www.ucu.com", "www.microsoft.com", "www.skype.com"]
browser = BrowserStack()
print([browser.navigation(page) for page in pages])
print(browser.backward())
print(browser.backward())
print(browser.forward())
print(browser.navigation("www.3wschools.com"))
print(browser.forward())