from math_function import infinite

def test_infinite():
    assert infinite(10) == float('inf')
    assert infinite(-10) == -float('inf')
    assert infinite(0) == 0

if __name__ == "__main__":
    test_infinite()
    print("Test complete without errors")
