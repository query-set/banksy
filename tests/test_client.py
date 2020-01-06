import unittest
from unittest.mock import MagicMock, patch

from client import Client, ClientManager

NEW_FNAME = 'test_client_data.json'




class TestClient(unittest.TestCase):
    def test_data_source_extension(self):
        self.assertTrue(client.CLIENT_FNAME.endswith('.json'))

    def test_pull(self):
        data = client.Client.pull(NEW_FNAME)
        self.assertIsInstance(data, dict)

    def test_create(self):

    # @patch.object(client.Client().create(NEW_FNAME), create(NEW_FNAME).login,)
    # @patch.object(client.Client().create(NEW_FNAME).pas, "bar")
    # def test_client_creation_by_checking_filesize_before_and_after(self):
    #     import os
    #     before = os.path.getsize(NEW_FNAME)
    #     client.Client.create(source=NEW_FNAME)
    #     after = os.path.getsize(NEW_FNAME)
    #     self.assertTrue(before < after)
