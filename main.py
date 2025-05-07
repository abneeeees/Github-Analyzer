#in development right now
import requests
from bs4 import BeautifulSoup as bs


url = 'https://github.com/AvneeshKumar01'

response1 = requests.get('https://github.com/AvneeshKumar01')
soup1 = bs(response1.content , "html.parser")

response2 = requests.get("https://github.com/AvneeshKumar01?tab=repositories")
soup2 = bs(response2.content , "html.parser")

def name():
    a = soup1.select('h1.vcard-names')[0]
    words = a.find_all('span')
    data = [str(c.getText()).strip() for c in words]
    try :
        print(f"User-Name :   {data[1]}")
        print(f"Name      :   {data[0]}")
    except:
        print("no info")

def repo():
    a = soup2.find('div' , attrs={ "id" : "user-repositories-list"})
    repos = a.ul.find_all('li')
    
    i=1
    for li in repos:
        all_data = li.select('h3.wb-break-all')[0]

        link = all_data.find_all('a')
        final_link = 'https://github.com'+link[0]['href']
        word = [(str(c.string).strip()) for c in link]
        
        print(i , word[0] , ":" , final_link)
        i+=1

        desc = li.find_all('p')
        full_desc = [str(c.string).strip() for c in desc]

        try :
            print("Description :" , full_desc[0])
        except:
            print("NO description written")

        print("\n")

name()
print("\n")
repo()
print("\n")

