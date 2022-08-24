"""Experimental web interface client for jpdb."""

import mechanicalsoup
import re


class JPDB:
    """Experimental client for jpdb implementing a small subset of the web
    interface functionality available via `jpdb <https://jpdb.io/>`_, and
    some experimental functionality on top of that.
    """
    BASE_URL = 'https://jpdb.io'

    INDEX_PATH = '/'
    LOGIN_PATH = '/login'

    def __init__(self, username: str, password: str):
        """Construct a new client for jpdb using the given credentials to
        authenticate as a particular user, and the given ``requests`` module.

        :param username: The name of an existing jpdb user account.
        :param password: The password of the existing jpdb user account.
        """
        self._username = username
        self._password = password

        self._browser = mechanicalsoup.StatefulBrowser()

    def login(self) -> None:
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
            raise JPDBLoginError(self._username)


class JPDBError(RuntimeError):
    """Base class for expected errors raised directly by :class:`JPDB`."""
    pass


class JPDBLoginError(JPDBError):
    """Error raised when :class:`JPDB` is unable to complete the login process
    using the supplied user credentials.
    """
    def __init__(self, username):
        super().__init__('login failed with username: %s' % username)
