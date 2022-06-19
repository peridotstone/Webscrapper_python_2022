import requests
import warnings
from bs4 import BeautifulSoup

warnings.filterwarnings("ignore")

indeed_result = requests.get(
    "https://www.indeed.com/jobs?q=python&limit=50", verify=False, timeout=3)

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

pages = pagination.find_all('a')
spans=[]

for page in pages:
    spans.append(page.find("span"))
    
print(spans[:-1])