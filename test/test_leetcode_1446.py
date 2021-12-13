import leetcode_1446


class TestLeetCode:
    """Test cases for algorithm problem in Leet Code."""

    def test_leetcode_1446(self) -> None:
        """Test leetcode 1446."""
        test_cases = (
            ("leetcode", 2),
            ("abbcccddddeeeeedcba", 5),
            ("hooraaaaaaaaaaay", 11),
            ("tourist", 1),
        )

        for test_case, result in test_cases:
            assert leetcode_1446.solution(test_case) == result
