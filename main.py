''' IN DEVELOPMENT RIGHT NOW'''
from selenium import webdriver
from selenium.webdriver.common.by import By

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)
url = "https://github.com/AvneeshKumar01"
driver.get(url=url)

class BasicInf0 :
    def name(self):
        name = driver.find_element(By.CSS_SELECTOR , "span.p-name.vcard-fullname.d-block.overflow-hidden").text
        user_name = driver.find_element(By.CSS_SELECTOR , "span.p-nickname.vcard-username.d-block").text
        print(f"{name}  {user_name}")
    
    def socials(self):
        ulist_of_socials = driver.find_elements(By.CSS_SELECTOR , "li.vcard-detail.pt-1 > a")
        names = driver.find_elements(By.TAG_NAME, "title")

        for name , link in zip(names , ulist_of_socials):
            print(f"{name.text} : {link.get_attribute('href')}")



    def repo(self):
        params = "?tab=repositories"
        driver.get(url+params)

        repo_names = driver.find_elements(By.CSS_SELECTOR , "h3.wb-break-all > a")
        desc = driver.find_elements(By.CSS_SELECTOR , "div.col-10.col-lg-9.d-inline-block > div:nth-child(2)")

        i=1
        for ele1 , ele2 in  zip(repo_names , desc) :
            print(f"{i}.) {ele1.text} : {ele1.get_attribute("href")}")
            i = i+1

            try:
                print(f"   description : {ele2.text}\n")
            except:
                print("NO description written")

    def repo_insider():
        pass

obj = BasicInf0()
# obj.name()
# obj.socials()
# obj.repo()



