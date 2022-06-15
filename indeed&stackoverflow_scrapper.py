import requests
import bs4

indeed_result = requests.get(
    "https://www.indeed.com/jobs?q=python&limit=50", verify=False)
