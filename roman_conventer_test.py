from roman_conventer import to_roman_conv
import pytest


@pytest.mark.parametrize('arabic_number, expected_roman', (
            (1, "I"),
            (2, "II"),
            (3, "III")
))
def test_convert_digits_less_than_ten(arabic_number, expected_roman):
    assert to_roman_conv(arabic_number) == expected_roman
