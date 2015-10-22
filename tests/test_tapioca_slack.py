# coding: utf-8

import unittest

from tapioca_slack import Slack


class TestTapiocaSlack(unittest.TestCase):

    def setUp(self):
        self.wrapper = Slack()


if __name__ == '__main__':
    unittest.main()
