"""
Again, the code is broken, you need to create 4 functions.
  - add_to_dict: Add a word to a dict.
  - get_from_dict: Get a word from inside a dict.
  - update_word: Update a word inside of the dict.
  - delete_from_dict: Delete a word from the dict.


All this functions should check for errors, follow the comments to see all cases you need to cover.


There should be NO ERRORS from Python in the console.
"""


import os


def add_to_dict(dict_obj=None, str_key=None, str_word=None):
    pass
    try:
        if type(dict_obj) is not dict:
            print(f'You need to send a dictionary. you sent: {type(dict_obj)}')
        elif str_word is None:
            print("You need to send a word and a definition")
        else:
            if str_key in dict_obj:
                print(f'''{str_key} is already on the dictionary. won't add.''')
            else:
                dict_obj[str_key] = str_word
                print('{} has been added'.format(str_key))
    except:
        return "occur ERR"


def get_from_dict(dict_obj=None, str_key=1, str_word=1):
    pass
    try:
        if type(dict_obj) is not dict:
            print(f'You need to send a dictionary. you sent: {type(dict_obj)}')
        elif str_word*str_key is 1:
            print("You need to send a word to search for.")
        else:
            if not str_key in dict_obj:
                print(f'{str_key} was not found in this dict')
            else:
                print(f'{str_key} : {dict_obj[str_key]}')
    except:
        return "occur ERR"


def update_word(dict_obj=None, str_key=None, str_word=None):
    pass
    try:
        if type(dict_obj) is not dict:
            print(f'You need to send a dictionary. you sent: {type(dict_obj)}')
        elif str_word is None or str_key is None:
            print("You need to send a word and a definition to update")
        else:
            if not str_key in dict_obj:
                print(
                    f'''{str_key} is not on the dict. can't update non-existing word.''')
            else:
                dict_obj[str_key] = str_word
                print(f'{str_key} has been updated to: {dict_obj[str_key]}')
    except:
        return "occur ERR"


def delete_from_dict(dict_obj=None, str_key=None):
    pass
    try:
        if type(dict_obj) is not dict:
            print(
                f'You need to send a dictionary. you sent: {type(dict_obj)}')
        elif str_key is None:
            print("You need to specify a word to delete")
        else:
            if not str_key in dict_obj:
                print(
                    f'''{str_key} is not in this dict. won't delete.''')
            else:
                del dict_obj[str_key]
                print(f'{str_key} has been deleted.')
    except:
        return "occur ERR"


# \/\/\/\/\/\/\ DO NOT TOUCH  \/\/\/\/\/\/\


os.system('cls')


my_english_dict = {}


print("\n###### add_to_dict ######\n")


# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")


# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")


# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")


# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")


print("\n\n###### get_from_dict ######\n")


# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")


# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)


# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")


# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### update_word ######\n")


# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")


# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")


# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")


# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")


# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### delete_from_dict ######\n")


# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")


# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)


# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")


# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")


# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


# # # \/\/\/\/\/\/\ END DO NOT TOUCH  \/\/\/\/\/\/\
