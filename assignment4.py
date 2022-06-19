import requests
import os

def draw_console():
    os.system('clear')
    print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)")

def chk_startover():
    temp = input('Do you want to start over? y/n ')
    if temp == 'y':
        return True
    elif temp == 'n':
        return False
    else:
        print(f'''That's not a valid answer''')
        return None

def input_chk_URLs(lst_argu):
    lst_argu = list((map(lambda x: x.lower(), list(input().split(',')))))
    
    for s in lst_argu:
        if not ".com" in s:
            print(f'{s} is not a valid URL.')
            return None
    return lst_argu

def add_http_URLs(lst_argu):
    if lst_argu is None:
        return None
    
    for i in range(len(lst_argu)):
        if not "http://" in lst_argu[i]:
            lst_argu[i] = "http://" + (lst_argu[i].strip())
        else:
            lst_argu[i] = lst_argu[i].strip()
    return lst_argu

def requests_URLs(lst_argu):
    if lst_argu is None:
        return None
    
    dct_temp = {}
    for i in range(len(lst_argu)):
        try:
            temp = (requests.get(lst_argu[i], verify=False, timeout=3)).status_code
            dct_temp[f'{temp}_{i+1}'] = lst_argu[i]
        except requests.exceptions.ConnectionError as error:
            dct_temp[f'ERR_{i+1}'] = lst_argu[i]
    return dct_temp

def draw_result(dct_argu):
    if dct_argu is None:
        return None
    
    for i in dct_argu:
        if "200" in i:
            print(f'{dct_argu[i]} is up!')
        else:
            print(f'{dct_argu[i]} is down!')


lst_URLs = []
bool_startover = True

while True:
    if bool_startover is True:
        draw_console()
        draw_result(requests_URLs(add_http_URLs(input_chk_URLs(lst_URLs))))
        bool_startover = chk_startover()
        
    elif bool_startover is None:
        bool_startover = chk_startover() 
        
    elif bool_startover is False:
        print("OK, bye")
        break
