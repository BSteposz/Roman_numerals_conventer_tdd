from roman_conventer import to_roman_conv
import pytest


@pytest.mark.parametrize('arabic_number, expected_roman', (
            (1, "I"),
            (2, "II"),
            (3, "III"),
            (4, "IV"),
            (5, "V"),
            (8, "VIII"),
            (9, "IX"),
))
def test_convert_digits_less_than_ten(arabic_number, expected_roman):
    assert to_roman_conv(arabic_number) == expected_roman


@pytest.mark.parametrize('arabic_number, expected_roman', (
            (10, "X"),
            (22, "XXII"),
            (43, "XLIII"),
            (54, "LIV"),
            (85, "LXXXV"),
            (98, "XCVIII"),
            (99, "XCIX"),
))
def test_convert_digits_less_than_100(arabic_number, expected_roman):
    assert to_roman_conv(arabic_number) == expected_roman
