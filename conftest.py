import random
 import pytest


 @pytest.fixture(scope="session")
 def open_browser():
     b = "browser"
     print("Браузер открыт")
     print(f"Случайное число: {random.randint(0, 100)}")
     yield b
     b = ""
     print("Браузер закрыт!")
