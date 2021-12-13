"""Leet Code Algorithm Problem Solutions."""


def solution(num_str: str) -> int:
    """Leet Code 1446 (Easy).

    Given a non-empty array nums containing only positive integers,
    find if the array can be partitioned into two subsets
    such that the sum of elements in both subsets is equal.

    Examples
    - s: "leetcode", result: 2
    - s:,"abbcccddddeeeeedcba", result: 5
    """
    power = 0
    local_power = 1
    prev = None
    for char in num_str:
        if prev == char:
            local_power += 1
        else:
            prev = char
            power = max(power, local_power)
            local_power = 1
    return max(power, local_power)
