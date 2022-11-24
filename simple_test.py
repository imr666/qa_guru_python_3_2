def test_something():
    assert 1 == 2, "Мы проверяем это просто для теста, оно должно падать"


def test_something2():
    a = 1 / 0


def test_something3():
    pass


def test_something4():
    pass


def other_function():
    pass


def test_one():
    assert_digit(4, 5)


def assert_digit(one, two):
    assert one > two, "второе число не меньше первого"