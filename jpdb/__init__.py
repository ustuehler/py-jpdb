"""Experimental web interface client for jpdb."""

import mechanicalsoup
import re

from jpdb.export.reviews import Reviews


class JPDB:
    """Experimental client for jpdb implementing a small subset of the web
    interface functionality available via `jpdb <https://jpdb.io/>`_, and
    some experimental functionality on top of that.
    """
    BASE_URL = 'https://jpdb.io'

    INDEX_PATH = '/'
    LOGIN_PATH = '/login'
    EXPORT_REVIEWS_JSON_PATH = '/export/reviews.json'

    # Pattern matched on the index page indicating how many due cards there are
    # for review, if any. The sentence will be continued differently, depending
    # on whether all due cards are of the same type (i.e., only vocabulary or
    # only kanji cards), or of different types (vocabulary and kanji). That is
    # why we only match a partial sentence here.
    DUE_ITEMS_PATTERN = 'You have (\\d+) due '
    # The match group as returned by `re.match()` which indicates the number of
    # due cards, iff any.
    DUE_ITEMS_MATCH_GROUP = 1

    # Pattern which, when present on the index page, indicates that there are
    # no more due cards available for learning. As with the sentence indicating
    # the number of due cards, this sentence as well will continue differently,
    # depending on the types of new cards that are available for learning.
    NEW_ITEMS_PATTERN = 'You have (\\d+) new '

    # Pattern matched in every page's site header when we are not currently
    # signed in.
    LOGIN_REQUIRED_PATTERN = 'Login or Sign up'

    def __init__(self, username: str, password: str):
        """Construct a new client for jpdb using the given credentials to
        authenticate as a particular user.

        :param username: The name of an existing jpdb user account.
        :param password: The password of the existing jpdb user account.
        """
        self._username = username
        self._password = password

        self._browser = mechanicalsoup.StatefulBrowser()

    def login(self) -> None:
        """Validate the login credentials given in the constructor of this
        class and establish the session context for user-specific features.
        """
        login_url = self.BASE_URL + self.LOGIN_PATH
        index_url = self.BASE_URL + self.INDEX_PATH

        self._browser.open(login_url)

        # If a login is required, we will see a form that we have to fill out;
        # otherwise, if we are already logged in, we will have been redirected
        # to the index page.
        if self._browser.url == login_url:
            self._browser.select_form('form[action="/login"]')
            self._browser['username'] = self._username
            self._browser['password'] = self._password
            self._browser['remember-me'] = True
            self._browser.submit_selected()

        # If we're logged in now, we'll have been redirected to the index page;
        # otherwise, we'll still be on the login page (invalid credentials) or
        # on some error page (never happened to me).
        if self._browser.url != index_url:
            raise JPDBLoginError(
                actual_url=self._browser.url,
                expected_url=index_url,
                username=self._username)

    @property
    def due_items(self) -> int:
        """Return the current number of items due for review, regardless of
        whether it is vocabulary cards, Kanji cards, or both which are due.
        """
        self._auto_login()
        self._navigate_to(self.INDEX_PATH)

        # Attempt to match the pattern which identifies the number of due
        # items directly. This won't match of there aren't any items due.
        m = self._search_page(self.DUE_ITEMS_PATTERN)
        if m:
            return int(m.group(self.DUE_ITEMS_MATCH_GROUP))

        # The above pattern doesn't match when there are zero due items, but
        # the following pattern should still match, assuming that the user has
        # any new items to learn.
        if self._search_page(self.NEW_ITEMS_PATTERN):
            return 0

        raise JPDBDueItemsError('expected patterns not found on page '
                                '(neither "%s" nor "%s")' %
                                (self.DUE_ITEMS_PATTERN,
                                 self.NEW_ITEMS_PATTERN))

    @property
    def reviews(self) -> Reviews:
        """An export of the user's entire review history so far.

        The format of the export is subject to change according to the website,
        and not all data may be accessible through the returned object. However,
        you can access the underlying raw data using the `data` attribute of the
        returned object.

        For example:

        >>> type(jpdb.reviews.data)
        <class 'dict'>
        """
        self._auto_login()
        resp = self._navigate_to(self.EXPORT_REVIEWS_JSON_PATH)
        if not bool(resp):
            raise JPDBReviewsError(resp)

        return Reviews(resp.json())

    def _navigate_to(self, path) -> object:
        """Navigate to the given `path` relative to the base URL and verify
        that we didn't get redirected elsewhere before returning the Response
        object.
        """
        url = self.BASE_URL + path
        resp = self._browser.open(url)
        if self._browser.url != url:
            raise JPDBNavigationError(
                actual_url=self._browser.url,
                expected_url=url)

        return resp

    def _auto_login(self):
        """Attempt to sign in automatically, if we're not already signed in.
        """
        # If we haven't used the browser before, we assume that we don't have
        # a login session either and will first attempt to log in.
        if not self._browser.page or \
                self._search_page(self.LOGIN_REQUIRED_PATTERN):
            self.login()

    def _search_page(self, pattern):
        """Search for the given regular expression pattern and return either
        the match object, or None.
        """
        # If we haven't used the browser before, no page will be open and thus
        # the pattern can't match.
        if not self._browser.page:
            return None

        return re.search(pattern, self._browser.page.text)


class JPDBError(RuntimeError):
    """Base class for expected errors raised directly by :class:`JPDB`."""
    pass


class JPDBDueItemsError(JPDBError):
    """Error raised when :class:`JPDB` is unable to retrieve the current number
    of items due for review.
    """
    def __init__(self, message):
        super().__init__(message)


class JPDBReviewsError(JPDBError):
    """Error raised when :class:`JPDB` is unable to export the review history.
    """
    def __init__(self, response):
        super().__init__(
            f'unable to export reviews: request failed with'
            f' status code {response.status_code}')


class JPDBNavigationError(JPDBError):
    """Error raised when :class:`JPDB` is unable to navigate to a specific page
    on the jpdb website.
    """
    def __init__(self, actual_url, expected_url, message=None):
        if message:
            message += ': '
        else:
            message = ''

        super().__init__('%sexpected to navigate to %s, but landed at %s' %
                         (message, expected_url, actual_url))


class JPDBLoginError(JPDBNavigationError):
    """Error raised when :class:`JPDB` is unable to complete the login process
    using the supplied user credentials.
    """
    def __init__(self, actual_url, expected_url, username):
        super().__init__(
            actual_url=actual_url,
            expected_url=expected_url,
            message='login failed with username: %s' % username)
