from del_fn import sum


def test_sum():
    assert sum(2, 3) == 5

def test_sum1():
    assert sum(3, 3) == 6

def test_sum2():
    assert sum(5, 3) == 8

def test_sum3():
    assert sum(1, 3) == 4


