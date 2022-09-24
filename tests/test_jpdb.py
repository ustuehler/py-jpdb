import datetime
import doctest
import os
import unittest

import jpdb


def JPDB():
    return jpdb.JPDB(
        username=os.environ['JPDB_USERNAME'],
        password=os.environ['JPDB_PASSWORD'],
    )


class TestJPDB(unittest.TestCase):

    def setUp(self) -> None:
        self.jpdb = JPDB()

    def test_login(self):
        self.assertIsNone(self.jpdb.login())

    def test_due_items(self):
        self.assertIsInstance(self.jpdb.due_items, int)

    def test_reviews(self):
        reviews = self.jpdb.reviews

        # It is possible that the user account which we use for testing has
        # not done any reviews, yet. We should verify that the review history
        # is indeed empty before accepting None here.
        last_review_timestamp = reviews.last_review_timestamp
        if last_review_timestamp is not None:
            self.assertIsInstance(last_review_timestamp, datetime.datetime)

        self.assertIsInstance(reviews.data, dict)
        self.assertIn('cards_vocabulary_jp_en', reviews.data)
        self.assertIn('cards_vocabulary_en_jp', reviews.data)
        self.assertIn('cards_kanji_keyword_char', reviews.data)
        self.assertIn('cards_kanji_char_keyword', reviews.data)


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(jpdb, extraglobs={
        'jpdb': JPDB(),
    }))
    return tests


if __name__ == '__main__':
    unittest.main()
