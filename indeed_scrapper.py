import requests
import warnings
from bs4 import BeautifulSoup
warnings.filterwarnings("ignore")


PAGE_LIMIT = 50
INDEED_URL_start = f"https://www.indeed.com/jobs?q=python&start="


def parsing_pages(str_url):
    indeed_rq = requests.get(str_url, verify=False)
    indeed_soup = BeautifulSoup(indeed_rq.text, "html.parser")
    pagination = indeed_soup.find("div", {"class": "pagination"})
    pages = pagination.find_all("li")

    return pages


def find_end_of_page():
    search_index = 0
    end_page_num = 0
    is_end_of_page = False

    while not is_end_of_page:
        try:
            temp_parser_pages = parsing_pages(
                f"{INDEED_URL_start}{PAGE_LIMIT*search_index}")

            if temp_parser_pages[-1].find()["aria-label"] != "Next":
                is_end_of_page = True
                break
            elif temp_parser_pages[1].find()["aria-label"] == "Previous":
                pass
            else:
                for i in range(len(temp_parser_pages)):
                    page = temp_parser_pages[i].find().string
                    page_num = int(page) if page is not None else False
                    end_page_num = page_num if end_page_num < page_num else end_page_num
                    print(f'please : {end_page_num}')
                search_index += 1
        except:
            continue

    return end_page_num-1


# end_of_page = 66
end_of_page = 1
jobtitle = []
companytitle = []
locationtitle = []
job_id = []
for i in range(end_of_page):
    try:
        indeed_rq2 = requests.get(
            f"{INDEED_URL_start}{PAGE_LIMIT*i}", verify=False)
        indeed_soup = BeautifulSoup(indeed_rq2.text, "html.parser")

        jobs = indeed_soup.find(
            "ul", {"class": "jobsearch-ResultsList"}).find_all("a", {"class": "jcs-JobTitle"})
        jobtitle += [jobs[i].string for i in range(
            len(jobs)) if jobs[i].string]

        companies = indeed_soup.find(
            "ul", {"class": "jobsearch-ResultsList"}).find_all("span", {"class": "companyName"})
        companytitle += [companies[i].string for i in range(
            len(companies)) if companies[i].string]

        locations = indeed_soup.find(
            "ul", {"class": "jobsearch-ResultsList"}).find_all("div", {"class": "companyLocation"})
        locationtitle += [locations[i].string for i in range(
            len(locations)) if locations[i].string]

        job_ids = indeed_soup.find(
            "ul", {"class": "jobsearch-ResultsList"}).find_all("a", {"class": "jcs-JobTitle"})
        job_id += [job_ids[i]["data-jk"] for i in range(
            len(job_ids)) if job_ids[i]["data-jk"]]

    except Exception as error:
        print(error)
        continue
