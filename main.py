''' IN DEVELOPMENT RIGHT NOW'''
from selenium import webdriver
import re
from selenium.webdriver.common.by import By

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)
url = "https://github.com/AvneeshKumar01"
driver.get(url=url)

class BasicInf0 :
    
    def __init__(self):
        self.to_store_repos = []
    
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

        for i, (ele1, ele2) in enumerate(zip(repo_names, desc), start=1):
            # print(f"{i}.) {ele1.text} : {ele1.get_attribute('href')}")
            self.to_store_repos.append(ele1.get_attribute('href'))

            # try:
            #     print(f"   description : {ele2.text}\n")
            # except:
            #     print("NO description written")

boj = BasicInf0()
boj.repo()
collected_links = boj.to_store_repos


class RepoInsider(BasicInf0):

    def __init__(self , to_store_repos):
        self.to_store_repos = to_store_repos
        self.total_commit = 0
        self.total_stars = 0

    def no_of_stars(self):
        stars = driver.find_element(By.CSS_SELECTOR , "a.Link.Link--muted > strong")
        self.total_stars += int(stars.text)

    def no_of_commits(self):
        commits = driver.find_element(By.CSS_SELECTOR , 'span.fgColor-default')
        numbers = re.findall(r'\d+', commits.text)
        commit_list = [int(nums) for nums in numbers ]
        self.total_commit += commit_list[0]


    def all_repo_insider(self):
        for links in self.to_store_repos:
            driver.get(links)
            self.no_of_stars()
            self.no_of_commits()

        print(f"Total stars : {self.total_stars}")
        print(f"Total commits : {self.total_commit}")

obj = RepoInsider(collected_links)
obj.all_repo_insider()

class Personal():

    def followers_and_follwing(self):
        self.infos = driver.find_elements(By.CSS_SELECTOR , "div.mb-3 > a > span")

        self.list_for_ratio = []
        for self.info in self.infos:
            self.list_for_ratio.append(self.info.text)

    def no_of_repos(self):
        counter = driver.find_element(By.CSS_SELECTOR , "#repositories-tab > span.Counter")
        print(counter.text)

    def follower_to_follwing_ratio(self):
        ratio = int(self.list_for_ratio[0])/int(self.list_for_ratio[1])
        print(ratio)


    def profile_completion(self):
        pass
