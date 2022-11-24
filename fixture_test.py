# Фикстура - некоторый кусок кода, который будет выполняться перед тестом, либо после (пред и постусловие).
#это необходимо для тест-дизайна и правильной структуры кода.

import pytest
import random

@pytest.fixture()
def open_browser():
    b = 'browser'
    print('браузер открыт')
    yield b
    b = ''
    print('браузер закрыт')

@pytest.fixture()
def create_user(open_browser):
    return 'username','password'

def test_body(open_browser,create_user):
    assert open_browser == 'browser'
    assert create_user == 25
    # перейти на страницу логина
    # ввести логин и пароль
    # нажать ОК
    # убедиться, что мы перешли на страницу профиля

def test_body2(open_browser, create_user):
    pass

def test_body3(open_browser,create_user):
    pass