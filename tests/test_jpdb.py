import os
import unittest

# noinspection PyUnresolvedReferences
from jpdb import JPDB


class TestJPDB(unittest.TestCase):

    def setUp(self) -> None:
        self.jpdb = JPDB(
            username=os.environ['JPDB_USERNAME'],
            password=os.environ['JPDB_PASSWORD'],
        )

    def test_login(self):
        self.assertIsNone(self.jpdb.login())

    def test_due_items(self):
        self.assertIsInstance(self.jpdb.due_items, int)

    def test_reviews(self):
        reviews = self.jpdb.reviews
        self.assertIsInstance(reviews, dict)
        self.assertIn('cards_vocabulary_jp_en', reviews)
        self.assertIn('cards_vocabulary_en_jp', reviews)
        self.assertIn('cards_kanji_keyword_char', reviews)
        self.assertIn('cards_kanji_char_keyword', reviews)


if __name__ == '__main__':
    unittest.main()
