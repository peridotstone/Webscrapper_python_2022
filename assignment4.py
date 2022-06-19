import requests
import os


def draw_console():
    os.system('cls')
    print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)")


def Input_chk_URLs(lst_argu):
    temp = input().split(',')
       if ".com" in temp:
            lst_URLs[temp]
        else:


def add_http_URLs(lst_argu):
    for i in range(len(lst_argu)):
        if not "http://" in lst_argu[i]:
            lst_argu[i] = "http://" + (lst_argu[i].strip())
        else:
            lst_argu[i] = lst_argu[i].strip()
    return lst_argu


def requests_URLs(lst_argu):
    dct_temp = {}
    for i in range(len(lst_argu)):
        try:
            dct_temp[f'{requests.get(lst_argu[i], verify=False, timeout=3)}_{i+1}'] = lst_argu[i]
        except requests.exceptions.ConnectionError as error:
            dct_temp[f'ERR_{i+1}'] = lst_argu[i]
    return dct_temp


def draw_result(dct_argu):
    for i in dct_argu:
        if "200" in i:
            print(f'{dct_argu[i]} is up!')
        else:
            print(f'{dct_argu[i]} is down!')


lst_URLs = []
lst_respon = []
int_startover_key = 1


while True:
    if(int_startover_key == 3):
        print("OK, bye")
        break

    if int_startover_key == 1:
        draw_console()

        draw_result(requests_URLs(add_http_URLs(lst_URLs)))
        int_startover_key = 2

    elif int_startover_key == 2:
        temp = input('Do you want to start over? y/n ')
        if(temp == 'y'):
            int_startover_key = 1
        elif(temp == 'n'):
            int_startover_key = 3
