from goodreads.client import GoodreadsClient


class GoodReadsClientStub(GoodreadsClient):

    def __init__(self, api_key, api_secret):
        super().__init__(api_key, api_secret)

    def retrieve_book(self, title, author):
        if author is None:
            return self.retrieve_book_by_title(title)
        else:
            return self.retrieve_book_by_author(author,title)

    def retrieve_book_by_title(self, title):
        response = super().request('/book/title.xml', {'title': title})
        book = self.book(book_id=response['book']['id'])
        return book

    def retrieve_book_by_author(self, author_name,title):
        book = self.retrieve_book_by_title(title)
        for author in book.authors:
            if author.name == author_name:
                return book
        raise ValueError ('Unable to find book written by {}'.format(author_name))

