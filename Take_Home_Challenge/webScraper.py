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
    coes = "https://coes.latech.edu/facultystaff-directory/"
    ans = "https://ans.latech.edu/faculty-staff-directory/"
    cehs = "https://education.latech.edu/academic-programs/psychology-behavioral-sciences/staff-faculty-directory/"
    cla = "https://liberalarts.latech.edu/faculty-staff-directory/"
    

    scraper(ans)
    print("ans_end")
    scraper(cehs)
    print("cechs_end")
    scraper(cla)
    print("cla_end")
    scraper(coes)
    print("coes_end")

main()
