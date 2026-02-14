import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# Тесты для метода capitalize
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# Тесты для метода trim
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("      hello", "hello"),
    ("world", "world"),
    ("   multiple spaces   ", "multiple spaces   "),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "skypro"),
    ("", ""),
    ("   ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# Тесты для метода contains
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("SkyPro", "P", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("SkyPro", "z", False),
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

# Тесты для метода delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("hello world", "l", "heo word"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),
    ("hello", "z", "hello"),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
