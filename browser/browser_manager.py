from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Open Chrome
#Open URL
#Close Chrome
class BrowserManager:

    def __init__(self):
        self.driver = None

    def start_browser(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        self.driver.maximize_window()

    def open_url(self, url):
        self.driver.get(url)

    def close_browser(self):
        if self.driver:
            self.driver.quit()