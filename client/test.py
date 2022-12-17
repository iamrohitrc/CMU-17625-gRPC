import unittest
from unittest import mock

from service.inventory_model_pb2 import *
from client.inventory_client import InventoryServiceClient
from client.get_book_titles import get_book_titles

# class for mock server testing - actual server need not be running for this class's tests
class GetBookTitleTest(unittest.TestCase):
    def setUp(self):
        # populate some dummy in-memory data for tests
        self.books = [
            Book(
                isbn='abc101',
                title='Shoe Dog',
                author='Phil Knight',
                genre='BIOGRAPHY',
                year=2016
            ),
            Book(
                isbn='abc102',
                title='Hit Refresh',
                author='Greg Shaw',
                genre='TECHNOLOGY',
                year=2017
            )
        ]
        # input isbn values for test
        self.isbnList = ['abc101', 'abc102']
        # expected output for above input values for tests
        self.titles = ['Shoe Dog', 'Hit Refresh']

    @mock.patch.object(InventoryServiceClient, 'get_book_details')
    def test_get_book_titles_success(self, mock_grpc_get_book_details):
        mock_grpc_get_book_details.side_effect = self.books
        inventory_service_client = InventoryServiceClient("test_address", "test_port")
        titles = get_book_titles(inventory_service_client, self.isbnList)
        self.assertEqual(self.titles, titles)

    @mock.patch.object(InventoryServiceClient, 'get_book_details')
    def test_get_book_titles_not_found(self, mock_grpc_get_book_details):
        self.isbnList = ['abc101', 'abc102', 'abc103']

        def side_effect(isbn: str):
            if isbn == self.isbnList[0]:
                return self.books[0]
            elif isbn == self.isbnList[1]:
                return self.books[1]

        mock_grpc_get_book_details.side_effect = side_effect
        inventory_service_client = InventoryServiceClient("test_address", "test_port")

        titles = get_book_titles(inventory_service_client, self.isbnList)
        print(titles)
        self.assertEqual(self.titles[:2], titles)


class GetBookTitleTestLive(unittest.TestCase):
    def setUp(self):
        self.titles = ['Shoe Dog', 'Hit Refresh']
        self.isbnList = ['abc101', 'abc102']
        self.inventory_service_client = InventoryServiceClient("localhost", "50051")

    def test_get_book_titles_success(self):
        titles = get_book_titles(self.inventory_service_client, self.isbnList)
        self.assertEqual(self.titles, titles)

    def test_get_book_titles_not_found(self):
        self.isbnList = ['abc101', 'abc102', 'abc103']
        titles = get_book_titles(self.inventory_service_client, self.isbnList)
        self.assertEqual(self.titles, titles)
