from nagini_contracts.contracts import *
from typing import Tuple


def main() -> None:
    value = {0: ('asd', 46), 1: ('b', 23), 2: ('dd', 2)}
    Assert(value[0][0] == 'asd')
    Assert(value[2][0] == 'dd')
    s = get_second(value)
    Assert(s == 23)
    Assert(value[2][0] == 'dd')
    append_bla_45(value)
    Assert(value[2][0] == 'dd')
    Assert(get_second(value) == 23)
    Assert(len(value) == 4)
    Assert(value[3][0] == 'bla')
    # TODO: without assertions above, this assertion fails (sometimes)
    Assert(value[2][0] == 'dd')
    Assert(value[3][1] == 45)
    #:: ExpectedOutput(assert.failed:assertion.false)
    Assert(value[0][1] == 47)


def get_second(l: Dict[int, Tuple[str, int]]) -> int:
    Requires(Acc(dict_pred(l), 1/10))
    Requires(1 in l)
    Ensures(Acc(dict_pred(l), 1/10))
    #TODO: Why is this necessary??
    Ensures(Forall(Old(l),
                   lambda k: (k in l and l[k] == Old(l[k]), [[k in l], [l[k]], [Old(l[k])]])))
    Ensures(Result() == l[1][1])
    return l[1][1]


bla45 = ('bla', 45)


def append_bla_45(l: Dict[int, Tuple[str, int]]) -> None:
    Requires(Acc(dict_pred(l)))
    Ensures(Acc(dict_pred(l)))
    Ensures(Implies(Old(3 not in l), len(l) == Old(len(l)) + 1))
    Ensures(Forall(Old(l),
                   lambda k: (k in l and Implies(k != 3, l[k] is Old(l[k])), [[k in l], [l[k]], [Old(l[k])]])))
    Ensures(3 in l and l[3] is bla45)
    l[3] = bla45
