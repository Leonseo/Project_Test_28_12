import json

"""Программа загружает имя пользователя, если оно было сохранено ранее.
 В противном случае она запрашивает имя пользователя и сохраняет его."""

def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    filename = 'username.json'
    try:
        ''' программа пытается открыть файл
        username.json. Если файл существует,
        программа читает имя пользователя в память'''
        with open(filename) as f:
            '''и выводит сообщение, приветствующее пользователя, в блоке else.'''
            username = json.load(f)
        ''' Если программа запускается впервые, то файл username.json 
        не существует и происходит исключение FileNotFoundError'''
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """"Запрашивает новое имя пользователя."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username} !")

greet_user()




#
# username = input("What is your name? ")
#
# filename = 'username.json'
# with open(filename, 'w') as f:
#     '''Вызывается функция json.dump(), которой
#     передается имя пользователя и объект файла
#     ; функцтя сохвраняет имя пользователя и
#     объект файла, сохраняет имя пользователя в файле'''
#     json.dump(username, f)
#     print(f"We'll remember you when you come back, {username} !")
