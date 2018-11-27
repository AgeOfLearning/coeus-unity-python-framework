import unittest
import coeus_unity.commands as commands


class CommandsTestCase(unittest.TestCase):

    @staticmethod
    def verify_message_when_is_none():
        commands.assert_verify_message(None)

    def test_verify_message_when_is_none(self):
        self.assertRaises(AssertionError, self.verify_message_when_is_none)
