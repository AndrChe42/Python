import pytest
from string_utils import StringUtils


stringutils = StringUtils()

# Capitalize


def test_capitalize_lower_case():
    assert StringUtils().capitalize("skypro") == "Skypro"


def test_capitalize_upper_case_first_letter():
    assert StringUtils().capitalize("Skypro") == "Skypro"


def test_capitalize_empty_string():
    assert StringUtils().capitalize("") == ""


def test_capitalize_multiple_words():
    assert StringUtils().capitalize("aBcDe") == "Abcde"

# Trim


def test_trim_leading_spaces():
    assert StringUtils().trim("   skypro") == "skypro"


def test_trim_multiple_leading_spaces():
    assert StringUtils().trim("      skypro") == "skypro"


def test_trim_no_leading_spaces():
    assert StringUtils().trim("skypro") == "skypro"


def test_trim_empty_string():
    assert StringUtils().trim("") == ""


# Contains


def test_contains_symbol_in_string():
    assert StringUtils().contains("SkyPro", "S") is True


def test_contains_symbol_not_in_string():
    assert StringUtils().contains("SkyPro", "U") is False


def test_contains_empty_string():
    assert StringUtils().contains("", "S") is False


def test_contains_symbol_empty_string():
    assert StringUtils.contains("", "") is False


# Delete


def test_delete_symbol_single_char():
    assert StringUtils().delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_multiple_occurrences():
    assert StringUtils().delete_symbol("aaa", "a") == ""


def test_delete_symbol_substring():
    assert StringUtils().delete_symbol("SkyPro", "Pro") == "Sky"


def test_delete_symbol_not_found():
    assert StringUtils().delete_symbol("SkyPro", "X") == "SkyPro"


def test_delete_symbol_empty_string():
    assert StringUtils().delete_symbol("", "a") == ""

# result = stringutils.contains("", "B")
# print(f"{result}")

# result = stringutils.delete_symbol("SkyPro SkyPro", "A")
# print(f"{result}")
