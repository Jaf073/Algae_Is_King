import requests
from bs4 import BeautifulSoup

def scraper(url):
    # requests url info
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
        
    # finds all links on page and prints them out
    links = soup.find_all("a")
    for link in links:
        href = link.get("href")
        if href:
            print(href)
    

def main():
    # website that the scraper goes though
    website = "https://coes.latech.edu/facultystaff-directory/"

    scraper(website)
    
main()
