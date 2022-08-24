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


if __name__ == '__main__':
    unittest.main()
