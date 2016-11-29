#!/usr/bin/env python
# coding: utf-8

import platform

from unittest import TestCase
from consoleADL.core import Application

class BaseApplicationTester(TestCase):

    def setUp(self):

        self.app = Application("testapp", "test desc", "1.0", 4, 5)

    def tearDown(self):

        pass

    def test_app_attributes(self):

        if platform.system() == "Windows":
            enc = "shift_jis"
        
        else:
            enc = "utf-8"

        self.assertEqual(self.app.name, "testapp")
        self.assertEqual(self.app.desc, "test desc")
        self.assertEqual(self.app.version, "1.0")
        self.assertEqual(self.app.padding, " "*4)
        self.assertEqual(self.app.margin, "\n"*5)
        self.assertEqual(self.app.encoding, enc)

    def test_app_pp(self):
        
        msg = u"ハロー\n\n"

        result = u"\n" * 5
        result += u"    ハロー\n"
        result += u"    \n"
        result += u"    "

        self.assertEqual(self.app.pp(msg, margin=True), result)
