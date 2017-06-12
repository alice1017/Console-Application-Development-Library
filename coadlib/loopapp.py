#!/usr/bin/env python
# coding: utf-8

from .interactiveapp import InteractiveApplication, ENCODING


class InteractiveLoopApplication(InteractiveApplication):

    def __init__(self, name, desc, version,
                 padding, margin, suffix, encoding=ENCODING):

        super(InteractiveLoopApplication, self).__init__(
            name, desc, version, padding, margin, suffix, encoding)

        # loop status
        self.STATUS_EXIT = 0
        self.STATUS_CONTINUE = 1

    def loop(self, func):

        def mainloop():

            loop_flag = self.STATUS_CONTINUE

            while loop_flag == self.STATUS_CONTINUE:

                try:
                    loop_flag = func()

                except KeyboardInterrupt:
                    self.write_error("Terminated.")
                    self.exit(0)

            self.exit(0)

        return mainloop
