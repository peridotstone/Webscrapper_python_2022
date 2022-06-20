import requests
import warnings
from bs4 import BeautifulSoup
warnings.filterwarnings("ignore")

INDEED_URL = "https://www.indeed.com"
INDEED_Query_pythonjobs = "/jobs?q=python"


def find_last_page(str_URL, str_query):
    is_last_page = False
    start = 20
    page_count = 0

    while not is_last_page:

        chk_URL = f'{str_URL}{str_query}&start={start+50}'
        indeed_requests = requests.get(chk_URL, verify=False, timeout=3)
        indeed_soup = BeautifulSoup(indeed_requests.text, "html.parser")
        pagination = indeed_soup.find("div", {"class": "pagination"})
        if not pagination is None:
            pages = pagination.find_all('li')
        else:
            continue

        for i in range(len(pages)):
            page_count += 1
            chk_page = pages[i].find()['aria-label']

            if len(pages) == 7:
                page_count -= 2

            if not pages[i].find()['aria-label'] == "Next":
                is_last_page = True
                break

    print(f'recent page_count : {page_count}')
    return page_count - 2


print(find_last_page(INDEED_URL, INDEED_Query_pythonjobs))
