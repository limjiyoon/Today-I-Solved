from typing import Any, List, Tuple

import leetcode_416


class TestLeetCode:
    """Test cases for algorithm problem in Leet Code."""

    def test_leetcode_416(self) -> None:
        """Test leetcode 416."""
        test_cases = (
            ([1, 5, 11, 5], True),
            ([1, 2, 3, 5], False),
            ([1], False),
            ([1, 2, 3, 8], False),
        )

        for test_case, result in test_cases:
            assert leetcode_416.solution(test_case) == result
