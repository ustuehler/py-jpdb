import json
import os
import unittest

from jpdb.export.reviews import Reviews


class TestJPDBExportReviews(unittest.TestCase):

    def setUp(self) -> None:
        fixtures_dir = os.path.join(os.path.dirname(__file__), 'fixtures')
        fixture_file = os.path.join(fixtures_dir, 'reviews.json')

        with open(fixture_file) as f:
            data = json.loads(f.read())

        self.reviews = Reviews(data)

    def test_last_review_timestamp(self):
        expected = '2022-09-24 11:28:58+00:00'

        self.assertEqual(str(self.reviews.last_review_timestamp), expected)


if __name__ == '__main__':
    unittest.main()
