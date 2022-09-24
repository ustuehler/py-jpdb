from datetime import datetime
from zoneinfo import ZoneInfo

from .utils import DictData, ListData

TIMEZONE = ZoneInfo('UTC')


class CardReview(DictData):
    """Represents one occurrence in the review history of a single card."""

    @property
    def timestamp(self):
        """The date and time when this review took place."""
        return datetime.fromtimestamp(self.data['timestamp'], tz=TIMEZONE)


class CardReviewList(ListData):
    """Represents the review history of a single card."""

    @property
    def __item_class__(self):
        return CardReview

    @property
    def last_timestamp(self) -> datetime or None:
        """Returns the timestamp of the last review in this list."""

        return self[-1].timestamp if len(self) > 0 else None


class Card(DictData):
    """Represents a single card along with its optional review history."""

    @property
    def reviews(self):
        """The review history for this particular card."""
        return CardReviewList(self.data['reviews'])

    @property
    def last_review_timestamp(self) -> datetime or None:
        """Returns the timestamp of the last review of this card."""
        return self.reviews.last_timestamp


class CardList(ListData):
    """Represents a read-only list of either vocabulary or Kanji cards."""

    @property
    def __item_class__(self):
        return Card

    @property
    def last_review_timestamp(self) -> datetime or None:
        """Returns the timestamp of the last review of any card in this list."""

        timestamps = [
            card.last_review_timestamp
            for card in self
            if card.last_review_timestamp is not None
        ]

        return max(timestamps) if len(timestamps) > 0 else None


class Reviews(DictData):
    """Interprets the data of an `exported review history
    <https://jpdb.io/export/reviews.json>`_ from jpdb.io.
    """

    @property
    def cards_kanji_keyword_char(self):
        """List of Keyword > Kanji cards."""
        return CardList(self.data['cards_kanji_keyword_char'])

    @property
    def cards_kanji_char_keyword(self):
        """List of Kanji > Keyword cards."""
        return CardList(self.data['cards_kanji_char_keyword'])

    @property
    def cards_vocabulary_jp_en(self):
        """List of Japanese > English vocabulary cards."""
        return CardList(self.data['cards_vocabulary_jp_en'])

    @property
    def cards_vocabulary_en_jp(self):
        """List of English > Japanese vocabulary cards."""
        return CardList(self.data['cards_vocabulary_en_jp'])

    @property
    def last_review_timestamp(self):
        """Returns the timestamp of the very last review in the exported review
        history as an approximation of the overall age of the exported data.
        """

        return max([
            cards.last_review_timestamp

            for cards in [
                self.cards_kanji_keyword_char,
                self.cards_kanji_char_keyword,
                self.cards_vocabulary_jp_en,
                self.cards_vocabulary_en_jp,
            ]

            if cards.last_review_timestamp is not None
        ])
