"""Leet Code Algorithm Problem Solutions."""


def solution(num: int) -> int:
    """Leet Code 1137 (Easy).

    The Tribonacci sequence Tn is defined as follows:
    T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
    Given n, return the value of Tn.

    Examples
    - n:4, result: 4
    - n:25, result: 1389537
    """
    cur, nxt, nxt_nxt = 0, 1, 1
    for _ in range(num):
        cur, nxt, nxt_nxt = nxt, nxt_nxt, cur + nxt + nxt_nxt
    return cur
