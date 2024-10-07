import requests
from bs4 import BeautifulSoup

def scraper(url):
    # requests url info
    r = requests.get(url)

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        
        # finds all links on page and prints them out
        links = soup.find_all("a")
        for link in links:
            href = link.get("href")
            if href:
                print(href)
    else:
        print(f"failed to retrieve webpage info. status code {r.status_code}")
    

def main():
    website = "https://coes.latech.edu/facultystaff-directory/"
    scraper(website)
    
main()
