#!/usr/bin/env python
# coding: utf-8

from .core import Application, ENCODING


class TestApp(Application):

    def __init__(self):

        super(TestApp, self).__init__(
                    "test", "test app", "1.0", 4, 5, ENCODING)



