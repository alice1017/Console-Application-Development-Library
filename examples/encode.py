#!/usr/bin/env python
# coding: utf-8

import sys
import os

sys.path.insert(0, os.path.abspath(".."))

from coadlib.interactiveapp import InteractiveApplication

app = InteractiveApplication(
    name="Base64 Encoder",
    desc="Encode to base64",
    version="1.0a0", padding=4, margin=3,
    prefix=" > "
)

if __name__ == "__main__":

    app.write_usage()

    context = app.input_console("string", str)
    result = context.encode("base64")

    app.write("Encoded: {}".format(result))
    app.exit(0)



