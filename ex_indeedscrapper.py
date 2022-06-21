from bs4 import BeautifulSoup
import requests

LIMIT = 50
URL = f'https://www.indeed.com/jobs?q=python&limit={LIMIT}'


def check_is_first_page_last():
    is_first_page_last = False
    max_page_num = 0

    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find('div', class_='pagination')
    pages = pagination('li')

    for i in range(len(pages) - 1):  # Excludes the next button
        page_num = int(pages[i].findChild().string)
        if page_num > max_page_num:
            max_page_num = page_num

    if pages[-1].findChild()['aria-label'] != 'Next':
        # First page is the last page
        is_first_page_last = True

    return is_first_page_last, max_page_num, pages


def extract_pages():
    is_end_of_pages, max_page_num, pages = check_is_first_page_last()
    page_index = 0

    while not is_end_of_pages:
        if pages[-1].findChild()['aria-label'] == 'Next':
            # There's at least one more page.
            result = get_page(page_index)
            soup = BeautifulSoup(result.text, 'html.parser')
            pagination = soup.find('div', class_='pagination')
            pages = pagination('li')
            for i in range(1, len(pages)):  # Excludes the previous button
                li_child = pages[i].findChild().string
                if li_child is None:
                    continue
                else:
                    page_num = int(li_child)
                    if page_num > max_page_num:
                        max_page_num = page_num
        else:
            is_end_of_pages = True

        page_index += 1

    return max_page_num


def get_page(page_index):
    return requests.get(URL + f'&start={(page_index + 1) * LIMIT}', verify=False)


extract_pages()
