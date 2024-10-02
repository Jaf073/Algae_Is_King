import requests
from bs4 import BeautifulSoup

def scraper(url):
    # requests
    r = requests.get(url)

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        # finds titles as an example
        titles = soup.find_all("h1")
        print(titles)

    else:
        print(f"failed to retrieve webpage info. status code {r.status_code}")

def main():
    website = input("enter website url: ")
    scraper(website)

main()
