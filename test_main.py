# test_main.py
import pytest
from main import add_numbers

# Test that will pass
def test_add_numbers_pass():
    assert add_numbers(3, 5) == 8

# Test that will fail
def test_add_numbers_fail():
    assert add_numbers(3, "5") == 8  # This will raise a TypeError
