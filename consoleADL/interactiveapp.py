#!/usr/bin/env python
# coding: utf-8

import chardet

from .core import Application, ENCODING


class InteractiveApplication(Application):

    def __init__(self, name, desc, version,
                    padding, margin, prefix, encoding=ENCODING):
        """Initialize interactive application

        args:
        * name - The application name, used by usage msg.
        * desc - The description of application, used by usage msg.
        * version - The application version, used by usage msg.
        * padding - The width from left side of terminal window to the string area.
        * margin - The height from top side of terminal window to the string area.
        * prefix - The affix letter placed after an input string.
                    (ex: '>> ', ': ', etc)
        * encoding - The application encoding. 
        """

        super(InteractiveApplication, self).__init__(
                                    name, desc, version, padding, margin, encoding)

        if not prefix.endswith(" "):
            prefix += " "

        self.prefix = prefix


    def _detect(self, string):

        enc = chardet.detect(string)["encoding"]
        return string.decode(enc, "")


    def _input(self, msg):

        content = self.padding + msg
        self.stream.write(content)
        result = raw_input(self.prefix)

        return self._detect(result)


    def input_console(self, msg, valuetype, validate=True):
        """Create input console with prefix.

        This console provides the validate function.

        args:
        * msg - The message of console.
        * valuetype - The value type of input result.
        * validate - The boolean value whether exec validate function or not.
        """

        #if not isinstance(msg, unicode):
        #    msg = self._detect(msg)

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

                msg = u"{0}定義されていない値です。アプリケーションを終了します".format(self.padding)
                self.logger.critical(msg)
                self.exit(1)
    
        else:

            return value


