"""Leet Code Algorithm Problem Solutions."""

from typing import List


def solution(nums: List[int]) -> bool:
    """Leet Code 416 (Medium).

    Given a non-empty array nums containing only positive integers,
    find if the array can be partitioned into two subsets
    such that the sum of elements in both subsets is equal.

    Unittest
    - nums:[1,5,11,5], result: True
    - nums:[1,2,3,5], result: False
    """
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    possible_set = set([0])
    for num in nums:
        tmp_set = set(element + num for element in possible_set)
        possible_set.update(tmp_set)
        if target in possible_set:
            return True
    return False
