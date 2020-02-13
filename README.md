# Serial PC Control

[![GitHub Action Tests status](https://github.com/carlosperate/serial-pc-control/workflows/Tests/badge.svg)](https://github.com/carlosperate/serial-pc-control/actions)
[![GitHub Action Package status](https://github.com/carlosperate/serial-pc-control/workflows/Package/badge.svg)](https://github.com/carlosperate/serial-pc-control/actions)
![Supported Python versions](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue.svg)
[![Code style Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PyPI - License](https://img.shields.io/pypi/l/ubittool.svg)](LICENSE)

Control your PC keyboard and mouse via serial messages from a microcontroller
board like the BBC micro:bit or Arduino.

This is done by loading any of the pre-made libraries into the microcontroller
board, and then executing in the PC the application from this repository.

Embedded libraries to use with this application:
- [x] [BBC micro:bit MicroPython module](https://github.com/carlosperate/micropython-microbit-pc-control/)
- [ ] BBC micro:bit MakeCode extension not yet done
- [ ] Arduino library not yet done

## This Is Currently Under Development!

This project is still under heavy development, so it can be a little bit
unstable or incomplete.

Current way to run install and run it:
```
$ git clone https://github.com/carlosperate/serial-pc-control.git
$ cd serial-pc-control
$ poetry install
$ poetry run python serial_pc_control/process_cmds.py
```

Current status:
- [x] Controlling the mouse position, left click and right click are working.
- [x] Typing text from the keyboard is working.
- [ ] Typing special keys from the keyboard (arrow keys, shift, alt, etc) not
  yet implemented
- [x] Tested in macOS
- [ ] Not yet tested in Windows, although it should work
- [ ] Not yet tested in Linux, although it should work
- [x] Automatically detecting the micro:bit or Arduino serial port is working.
- [ ] Adding command line arguments to manually select the por and baud rate
      should be coming soon.
- [ ] The PyInstaller build for macOS (which can be downloaded from the GH Action)
  currently doesn't work due to this issue:
  https://github.com/pyinstaller/pyinstaller/issues/4130
    - It does work correctly if the script is executed with Python
