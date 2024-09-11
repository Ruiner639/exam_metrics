import pytest
from wrapper import wrapper

def test_wrapper_valid_input():
    assert wrapper(" 123 ") == float('inf')
    assert wrapper("123") == float('inf')
    assert wrapper(123) == float('inf')

def test_wrapper_invalid_input_letters():
    with pytest.raises(ValueError, match="Input should be integer without letters or space."):
        wrapper("semodels")

def test_wrapper_invalid_input_negative():
    with pytest.raises(ValueError, match="Input should be integer without letters or space."):
        wrapper("-123")

def test_wrapper_invalid_input_empty():
    with pytest.raises(ValueError, match="Input should be integer without letters or space."):
        wrapper(" ")

def test_wrapper_invalid_input_mixed():
    with pytest.raises(ValueError, match="Input should be integer without letters or space."):
        wrapper("12lol34")
