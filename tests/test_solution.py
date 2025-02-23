import unittest
import app.solution as s


class TestSolution(unittest.TestCase):
    def setUp(self):
        pass

    def test_check_connection(self):
        """Test check_connection function with multiple cases."""
        test_cases = [
            ("112233", "332200", True),
            ("112233", "332211", True),
            ("112233", "113322", False),
            ("12", "21", False),
            ("999900", "001234", True),
        ]

        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(s.check_connection(a, b), expected)

    def test_graphify(self):
        """Test graphify function with different lists of numbers."""
        test_cases = [
            (
                ["112233", "332200", "332211"],
                {"112233": ["332200", "332211"], "332200": [], "332211": ["112233"]},
            ),
            (
                ["123456", "561234", "341234"],
                {"123456": ["561234"], "561234": ["341234"], "341234": []},
            ),
            (["111111", "222222"], {"111111": [], "222222": []}),
        ]

        for numbers, expected_graph in test_cases:
            with self.subTest(numbers=numbers):
                self.assertEqual(s.graphify(numbers), expected_graph)

    def test_find_best_sequence(self):
        """Test find_best_sequence function with different sets of numbers."""
        test_cases = [
            (
                ["608017", "248460", "962282", "994725", "177092"],
                ["248460", "608017", "177092"],
            ),
            (["111111", "222222"], ["111111"]),
            (
                ["123456", "567890", "901234"],
                ["123456", "567890", "901234"],
            ),
            ([], []),
        ]

        for numbers, expected_sequence in test_cases:
            with self.subTest(numbers=numbers):
                self.assertEqual(s.find_best_sequence(numbers), expected_sequence)


if __name__ == "__main__":
    unittest.main()
