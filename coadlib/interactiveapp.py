#!/usr/bin/env python
# coding: utf-8

from .core import Application, ENCODING


class InteractiveApplication(Application):

    def __init__(self, name, desc, version,
                 padding, margin, prefix, encoding=ENCODING):
        """Initialize interactive application

        args:
        * name - The application name, used by usage msg.
        * desc - The description of application, used by usage msg.
        * version - The application version, used by usage msg.
        * padding - The width from left side of terminal window
                    to the message area.
        * margin - The height from top side of terminal window
                   to the message area.
        * prefix - The affix letter placed after an input string.
                    (ex: '>> ', ': ', etc)
        * encoding - The application encoding.
        """

        super(InteractiveApplication, self).__init__(
            name, desc, version, padding, margin, encoding)

        if not prefix.endswith(" "):
            prefix += " "

        self.prefix = prefix

    def _input(self, msg):

        self.stdout.write(self.pp(msg + self.prefix))
        result = self.stdin.readline()

        return result.strip()

    def input_console(self, msg, valuetype, validate=True):
        """Create input console with prefix.

        This console provides the validate function.

        args:
        * msg - The message of console.
        * valuetype - The value type of input result.
        * validate - The boolean value whether exec validate function or not.
        """

        result = self._input(msg)

        if validate is True:
            return self.validate(valuetype, result)

        else:
            return result

    def validate(self, object, value):

        if not isinstance(value, object):

            try:
                result = object(value)
                return result

            except:
                self.logger.critical(self.pp(
                    u"定義されていない値です。アプリケーションを終了します"))
                self.exit(1)

        else:
            return value
