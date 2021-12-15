import leetcode_1137


class TestLeetCode:
    """Test cases for algorithm problem in Leet Code."""

    def test_leetcode_1137(self) -> None:
        """Test leetcode 1137."""
        test_cases = (
            (4, 4),
            (25, 1389537),
        )

        for test_case, result in test_cases:
            assert leetcode_1137.solution(test_case) == result
