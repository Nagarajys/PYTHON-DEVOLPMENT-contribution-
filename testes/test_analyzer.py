import unittest

from analyzer import analyze_dataset


class TestDatasetAnalyzer(unittest.TestCase):

    def test_dataset_analysis(self):

        headers = ["name", "age", "score"]

        rows = [

            {"name": "Raj", "age": "19", "score": "90"},

            {"name": "Rahul", "age": "20", "score": ""},

            {"name": "Raj", "age": "19", "score": "90"}

        ]

        result = analyze_dataset(headers, rows)

        self.assertEqual(result["rows"], 3)

        self.assertEqual(result["columns"], 3)

        self.assertEqual(result["duplicates"], 1)

        self.assertEqual(result["missing"]["score"], 1)


if __name__ == "__main__":

    unittest.main()
