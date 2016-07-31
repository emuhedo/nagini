from py2viper_contracts.contracts import (
    Requires,
    Invariant,
    Implies,
    Assert,
)
from py2viper_contracts.io import IOExists1
from py2viper_contracts.obligations import *


# Test for name conflicts with builtin names.


def over_in_conflict(_cthread: int) -> None:
    Requires(MustTerminate(_cthread))


# Test that measures are always positive.

def over_in_minus_one() -> None:
    #:: Label(over_in_minus_one__MustTerminate)
    Requires(MustTerminate(-1))
    # Negative measure is equivalent to False.
    Assert(False)


def check_over_in_minus_one() -> None:
    #:: ExpectedOutput(call.precondition:obligation_measure.non_positive,over_in_minus_one__MustTerminate)
    over_in_minus_one()


def over_in_minus_one_conditional(b: bool) -> None:
    Requires(Implies(b, MustTerminate(1)))
    #:: Label(over_in_minus_one_conditional__MustTerminate__False)
    Requires(Implies(not b, MustTerminate(-1)))
    # Negative measure is equivalent to False.
    Assert(Implies(not b, False))
    #:: ExpectedOutput(assert.failed:assertion.false)
    Assert(False)


def check_over_in_minus_one_conditional_1() -> None:
    over_in_minus_one_conditional(True)


def check_over_in_minus_one_conditional_2() -> None:
    #:: ExpectedOutput(call.precondition:obligation_measure.non_positive,over_in_minus_one_conditional__MustTerminate__False)
    over_in_minus_one_conditional(False)


# Test that measure bottom is always used.


def over_in_one() -> None:
    Requires(Implies(True, MustTerminate(1)))
    Requires(MustTerminate(1))


def over_in_two_1() -> None:
    Requires(MustTerminate(1))
    Requires(MustTerminate(2))
    #:: ExpectedOutput(leak_check.failed:must_terminate.not_taken)
    over_in_one()


def over_in_two_2() -> None:
    Requires(MustTerminate(2))
    Requires(MustTerminate(1))
    #:: ExpectedOutput(leak_check.failed:must_terminate.not_taken)
    over_in_one()


def over_in_two_3() -> None:
    Requires(Implies(False, MustTerminate(1)))
    Requires(MustTerminate(2))
    over_in_one()


def over_in_two_4() -> None:
    Requires(MustTerminate(2))
    Requires(Implies(False, MustTerminate(1)))
    over_in_one()


def over_in_two_5() -> None:
    Requires(MustTerminate(2))
    #:: ExpectedOutput(leak_check.failed:must_terminate.not_taken)
    over_in_two_4()


# Some positive tests.


def over_in_two() -> None:
    Requires(MustTerminate(2))
    over_in_one()


def over_in_two_6() -> None:
    IOExists1(int)(
        lambda x: (
            Requires(MustTerminate(2))
        )
    )
    over_in_one()


def non_terminating() -> None:
    over_in_one()


# Check that there is always enough termination permission.

def over_in_many(b: bool) -> None:
    Requires(MustTerminate(1))
    Requires(MustTerminate(2))
    Requires(MustTerminate(3))
    Requires(MustTerminate(4))
    Requires(Implies(b, MustTerminate(4)))
    Requires(Implies(b, MustTerminate(5)))
    Requires(Implies(b, MustTerminate(6)))
    Requires(Implies(not b, MustTerminate(1)))
    Requires(Implies(not b, MustTerminate(2)))
    Requires(Implies(not b, MustTerminate(3)))


def non_terminating2(b: bool) -> None:
    over_in_many(b)


def over_in_two7() -> None:
    Requires(MustTerminate(2))
    over_in_many(True)


def over_in_two8() -> None:
    Requires(MustTerminate(2))
    over_in_many(False)


# Calling non-terminating is not-allowed.


def non_terminating3() -> None:
    pass


def terminating_caller() -> None:
    Requires(MustTerminate(2))
    #:: ExpectedOutput(leak_check.failed:must_terminate.not_taken)
    non_terminating3()
