#!/usr/bin/env python
# coding: utf-8

from .interactiveapp import InteractiveApplication, ENCODING

class InteractiveLoopApplication(InteractiveApplication):

    def __init__(self, name, desc, version,
                    padding, margin, encoding=ENCODING):

        super(InteractiveLoopApplication, self).__init__(
            name, desc, version, padding, margin, "", encoding)

        
        # loop flags
        self.LOOP_CONTINUE = 1
        self.LOOP_BREAK = 0

    def loop(self, func, input_message):

        loop_flag = self.LOOP_CONTINUE

        while loop_flag == self.LOOP_CONTINUE:

            data = self.input_console(input_message, None, validate=False)
            loop_flag = func(data)

        self.exit(0)

