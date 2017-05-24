#!/usr/bin/env python
# coding: utf-8

from unittest import TestCase
from coadlib.core import ENCODING
from coadlib.interactiveapp import InteractiveApplication

class InteractiveApplicationTester(TestCase):

    def setUp(self):

        self.app = InteractiveApplication(
                    "testapp", "app desc", "1.0", 4, 5,
                    prefix=">>>", encoding=ENCODING)

    def tearDown(self):

        pass

    def test_app_attrs(self):

        self.assertEqual(self.app.prefix, ">>> ")
 
