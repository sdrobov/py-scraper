from bs4 import BeautifulSoup
import requests
   
# lists
urls=[]
base_uri = "https://auto-leon.ru/"
   
# function created
def scrape(site):
       
    # getting the request from url
    r = requests.get(site)
       
    # converting the text
    s = BeautifulSoup(r.text, "html.parser")
       
    for i in s.find_all("a"):
        if not "href" in i.attrs:
            continue
          
        href = i.attrs['href']
        if href.startswith("#"):
            continue

        if href.endswith(".jpeg"):
            continue

        if href.endswith(".jpg"):
            continue

        if href.endswith(".png"):
            continue

        if href.startswith("/"):
            href = href.lstrip("/")
            if href.startswith("#"):
                continue
            site = base_uri+href
               
            if site not in urls:
                urls.append(site)
                print(site)
                # calling it self
                scrape(site)
   
# main function
if __name__ =="__main__":
    # calling function
    scrape(base_uri)

