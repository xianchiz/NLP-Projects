"""Test gerund-matching regular expression."""
import re

import pytest


# *** ADD YOUR PATTERN BELOW *** #
# pattern = r""
pattern = r"[a-z]{2,}ing"
# *** ADD YOUR PATTERN ABOVE *** #


test_cases = [
    ("singing is my favorite hobby.", True),
    ("eating food makes me happy.", True),
    ("he loves writing books", True),
    ("she thinks typing the computer all day is tired", True),
    ("he gets used to saving money", True),
    ("let's go climbing", True),
    ("they ring the door bell", False),
    ("the king of the mountain is not a monkey", False)

]


@pytest.mark.parametrize("string,matches", test_cases)
def test_name_matching(string, matches: bool):
    """Test whether pattern correctly matches or does not match input."""
    assert (re.fullmatch(pattern, string) is not None) == matches
