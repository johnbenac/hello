from adder import add_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(-5, -5) == -10
    assert add_numbers(0, 0) == 0
    assert add_numbers(1.5, 2.5) == 4.0 