import unittest
import coeus_unity.assertions as assertions


class AssertionsTestCase(unittest.TestCase):

    @staticmethod
    def verify_message_when_is_none():
        assertions.assert_verify_message(None)

    def test_verify_message_when_is_none(self):
        self.assertRaises(AssertionError, self.verify_message_when_is_none)
