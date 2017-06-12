# coadlib - Console Application Development Library

**Coadlib** is a python library for develop console application.

**Co** nsole **A** pplication **D** evelopment **Lib**rary

## Application classes

* [Application](#application)
* [InteractiveApplication](#interactiveapplication)
* [InteractiveLoopApplication](#interactiveloopapplication)

### Application

**The base application class.**

Supported encoding, IO, etc.

#### params

* `name` - application name
* `desc` - applicationi description
* `version` - application version
* `padding` - the **width size** from left side of terminal window to string area.
* `margin` - the **height size** from top side of terminal window to string area.
* `encoding` - application encoding. by default, the program decides encoding by your platform.

#### main methods

* `write(msg)` - print message too stream with new line.
* `write_error(msg)` - print error message to stream with new line.
* `write_usage()` - generate usage message from application name, version, description, and print it.
* `exit(status)` - exit application with status code.

### InteractiveApplication

Inherited the [application](#Application) class, added new methods to **input message from user**.

#### params

The `Application` class params:

* name
* desc
* version
* padding
* margin

new param:

* `suffix` - the **suffix letter** placed after an input string.

#### main methods

* `input_console(msg, valuetype, validate=True)` - display input console with suffix, supported validate.

### InteractiveLoopApplication

The InteractiveLoopApplication provides a **decorator** for **looping to function**.

#### params

Parameters are same of InteractiveApplication class.

#### main methods

* `loop` - The decorator

#### example

```py
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
```

