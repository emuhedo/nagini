#:: IgnoreFile(26)
from nagini_contracts.contracts import *
from typing import Tuple


def test(a: int, b: int) -> Tuple[int, int]:
    Ensures(
        #:: UnexpectedOutput(postcondition.violated:assertion.false, 26)
        ((True and
        True) and
        True) and
        #:: ExpectedOutput(postcondition.violated:assertion.false)|MissingOutput(postcondition.violated:assertion.false, 26)
        (Result()[0] == a and
        Result()[1] == b)
        )
    return b, a
