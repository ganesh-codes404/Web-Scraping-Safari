import requests
from bs4 import BeautifulSoup
import csv
url = "https://github.com/trending"
headers = {"User-Agent": "Mozilla/5.0"}
#initialising soup and requests
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

repos = soup.find_all("article", class_="Box-row")[:5]
data = []

for r in repos:
    h2_tag = r.find("h2") #we find the h2 tag here to find the name of the repo 
    a_tag = h2_tag.find("a")
    name = a_tag.get_text(strip=True).replace(' ', '').replace('\n', '')
    link = "https://github.com" + r.h2.a["href"]
    data.append([name, link])

with open("trending_repos.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Repository Name", "Link"])
    writer.writerows(data)

print("CSV saved.")
