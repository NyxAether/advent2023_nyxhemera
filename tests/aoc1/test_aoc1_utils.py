

from advent2023.aoc1.aoc_utils import extract_first_last_digit, transform_text_digits_to_digits


def test_extract_first_last_digit():
    assert extract_first_last_digit("9twonineonefourpttbgkxt8two") == 98
    assert extract_first_last_digit("fv9") == 99
    assert extract_first_last_digit("5qcmjsfk6zxjld1") == 51
    assert extract_first_last_digit("fkjstnvmchsr9q699") == 99
    assert extract_first_last_digit("nine78three") == 78
    assert extract_first_last_digit("4rcs6bhbbgzhsstwomnineksbxfzj8") == 48
    assert extract_first_last_digit("4fmblhqninefive6qbkm") == 46
    assert extract_first_last_digit("zsgjbfrjfour1sp3") == 13
    assert extract_first_last_digit("zbfeightfive1oneonernfd") == 11
    assert extract_first_last_digit("5bxtfvzczbhtzfourqglqdxsc") == 55
    assert extract_first_last_digit("f9five7five8ddvseven") == 98
    assert extract_first_last_digit("23bszpdxfjmzg") == 23


def test_transform_text_digits_to_digits():
    assert transform_text_digits_to_digits("xtwone3four") == "2134"
    assert transform_text_digits_to_digits("9twonineonefourpttbgkxt8two") == "9291482"
    assert transform_text_digits_to_digits("fv9") == "9"
    assert transform_text_digits_to_digits("5qcmjsfk6zxjld1") == "561"
    assert transform_text_digits_to_digits("fkjstnvmchsr9q699") == "9699"
    assert transform_text_digits_to_digits("nine78three") == "9783"
    assert transform_text_digits_to_digits("4rcs6bhbbgzhsstwomnineksbxfzj8") == "46298"
    assert transform_text_digits_to_digits("4fmblhqninefive6qbkm") == "4956"
    assert transform_text_digits_to_digits("zsgjbfrjfour1sp3") == "413"
    assert transform_text_digits_to_digits("zbfeightfive1oneonernfd") == "85111"
    assert transform_text_digits_to_digits("5bxtfvzczbhtzfourqglqdxsc") == "54"
    assert transform_text_digits_to_digits("f9five7five8ddvseven") == "957587"
    assert transform_text_digits_to_digits("23bszpdxfjmzg") == "23"
