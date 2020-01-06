import unittest
from unittest.mock import patch

import account

# test if the previous version of accounts data is the same as the new
#

NEW_FNAME = "test_account_data.json"


class TestAccount(unittest.TestCase):
    def test_pull(self):
        data = account.Account.pull(NEW_FNAME)
        self.assertIsInstance(data, dict)

    def test_save(self):
        data = account.Account.pull(source=NEW_FNAME)
        print(data)

        import os
        before = os.path.getsize(NEW_FNAME)
        print("before", before)
        data['testuser'] = []
        print(data)
        account.Account.save(data, NEW_FNAME)
        after = os.path.getsize(NEW_FNAME)

        print("before", before)
        print("after", after)

        result = True if before < after else False

        self.assertTrue(result)
