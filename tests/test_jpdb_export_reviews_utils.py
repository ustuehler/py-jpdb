import doctest

import jpdb.export.reviews.utils


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(jpdb.export.reviews.utils))
    return tests
