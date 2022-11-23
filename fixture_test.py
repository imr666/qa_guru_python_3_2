# Фикстура - некоторый кусок кода, который будет выполняться перед тестом, либо после (пред и постусловие).
#это необходимо для тест-дизайна и правильной структуры кода.

import pytest

@pytest.fixture()
def open_browser():
    b = 'browser'
    print('браузер открыт')
    yield b
    b = ''
    print('браузер закрыт')

@pytest.fixture()
def create_user(open_browser):
    return 35

def test_body(open_browser,create_user):
    assert open_browser == 'browser'
    assert create_user == 5
    # перейти на страницу логина
    # ввести логин и пароль
    # нажать ОК
    # убедиться, что мы перешли на страницу профиля