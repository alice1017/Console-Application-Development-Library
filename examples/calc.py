#!/usr/bin/env python
# coding: utf-8

from coadlib.apps import InteractiveLoopApplication

app = InteractiveLoopApplication(
    name="calcuation program",
    desc="please input number, and return total.",
    version="1.0", padding=4, margin=3, suffix=" > "
)

app.total = 0


@app.loop
def main():

    response = app.input_console("number", int, validate=False)

    if response == "":
        app.write("total: {:,}".format(app.total))
        return app.STATUS_EXIT

    else:
        try:
            app.total += int(response)
            return app.STATUS_CONTINUE

        except:
            app.write_error("Error: incorrect data.")
            return app.STATUS_CONTINUE


if __name__ == "__main__":

    app.write_usage()
    main()
