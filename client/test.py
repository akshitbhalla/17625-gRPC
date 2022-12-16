import unittest
from unittest import mock

from client.get_book_titles import get_book_titles
from client.inventory_client import InventoryClient
from service.library_pb2 import Book


# class for test cases using Mocked API Client
class TestGetBookTitles(unittest.TestCase):
    def setUp(self):
        # Setting up mock data
        self.isbn_list = ['1900023189', '780091103', '8193805013']
        self.titles = ['Harry Potter', 'Da Vinci Code', 'Born To Run']
        self.books = [Book(
            isbn='1900023189',
            title='Harry Potter',
            author='JK Rowling',
            genre='FANTASY',
            year=1997
        ), Book(
            isbn='780091103',
            title='Da Vinci Code',
            author='Dan Brown',
            genre='MYSTERY',
            year=2003
        ), Book(
            isbn='8193805013',
            title='Born To Run',
            author='Christopher McDougal',
            genre='THRILLER',
            year=2011
        )]

    # Set up of mock API client for get_book function
    @mock.patch.object(InventoryClient, 'get_book')
    def test_get_book_title(self, mock_get_book):

        # Using mock client
        mock_get_book.side_effect = self.books
        inventory_client = InventoryClient("", "")

        titles = get_book_titles(self.isbn_list, inventory_client)

        self.assertEqual(self.titles, titles)

    # Set up of mock API client for get_book function
    @mock.patch.object(InventoryClient, 'get_book')
    def test_get_book_title_unknown(self, mock_get_book):
        self.isbn_list = ['1900023189', 'unknown', '780091103', 'Not Found']

        def side_effect(isbn: str):
            if isbn == self.isbn_list[0]:
                return self.books[0]
            elif isbn == self.isbn_list[1]:
                return self.books[1]

        # Using mock client
        mock_get_book.side_effect = side_effect
        inventory_client = InventoryClient("", "")

        titles = get_book_titles(self.isbn_list, inventory_client)

        self.assertEqual(self.titles[:2], titles)


# class for Live test cases
class TestGetBookTitlesLive(unittest.TestCase):
    def setUp(self):
        self.isbn_list = ['1900023189', '780091103', '8193805013']
        self.titles = ['Harry Potter', 'Da Vinci Code', 'Born To Run']

        # Using live client here
        self.inventory_client = InventoryClient("localhost", "50051")

    # Using live function here as opposed to above where mock was used
    def test_get_book_title(self):
        titles = get_book_titles(self.isbn_list, self.inventory_client)

        self.assertEqual(self.titles, titles)

    # Using live function here as opposed to above where mock was used
    def test_get_book_title_unknown(self):
        self.isbn_list = ['1900023189', '780091103', '8193805013']
        titles = get_book_titles(self.isbn_list, self.inventory_client)

        self.assertEqual(self.titles, titles)
