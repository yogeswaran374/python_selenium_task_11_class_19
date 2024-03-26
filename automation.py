'''access the url for Saucedemo.com and fetch the title of webpage, url & contents present in the page'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class Saucedemo:

    def __init__(self,url, file_name):

        self.url = url
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        self.file_name = file_name
#login into the URL
    def booting_function(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            return True
        except:
            print("Error: The url is not valid")
            return False
#fetch the title of the webpage
    def fetch_title(self):
        if self.booting_function() == True:
            return self.driver.title
        else:
            return False

#fetch the current_URL
    def fetch_url(self):
        if self.booting_function() == True:
            return self.driver.current_url
        else:
            return False

#create a textfile and insert/write the data(contents of webpage)
    def create_file(self):
        file = open(self.file_name, "w")
        file.write(self.driver.page_source)
        return file



if __name__ == "__main__":
    url = "https://www.saucedemo.com/"
    file_name = "Webpage_task_11.txt"
    result = Saucedemo(url,file_name)
    result.booting_function()
    print(result.fetch_title())
    print(result.fetch_url())
    result.create_file()

