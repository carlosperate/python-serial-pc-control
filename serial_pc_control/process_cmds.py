#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Carlos Pereira Atencio
# SPDX-License-Identifier: MIT
"""Process and executes the commands received via serial."""
import sys
from typing import Callable, Dict, NoReturn, Tuple

from serial import Serial  # type: ignore

from serial_pc_control import cmds_keyboard
from serial_pc_control import cmds_mouse
from serial_pc_control import device_serial
from serial_pc_control import protocol


CMDS: Dict[str, Callable[[str], None]] = {
    "m-mv": cmds_mouse.move_vertical,
    "m-mh": cmds_mouse.move_horizontal,
    "m-mr": cmds_mouse.move_relative,
    "m-ckl": cmds_mouse.left_click,
    "m-ckr": cmds_mouse.right_click,
    "k-txt": cmds_keyboard.write,
}


def get_serial_config(
    port: str = None, baud_rate: int = None
) -> Tuple[str, int]:
    """Process the given port and baud rate or discover any connected board."""
    if port and baud_rate:
        print("Bypassing auto-detect.")
    elif not port and not baud_rate:
        try:
            found_device, found_port = device_serial.find_device_port()
        except Exception as e:
            print("Error: {}".format(e), file=sys.stderr)
            sys.exit(1)
        print("Found {} device.".format(found_device.name))
        port = found_port
        baud_rate = found_device.baud_rate
    else:
        print(
            "When autodetect is not used both the port and baud rate need to "
            "be provided."
        )
        sys.exit(1)
    print("Connecting to port {} at baud rate {}.".format(port, baud_rate))

    return port, baud_rate


def get_next_serial_cmd(serial: Serial) -> bytes:
    """Wait until it can return full serial command."""
    cmd_full_str = None
    while not cmd_full_str:
        cmd_full_str = serial.read_until(terminator=protocol.CMD_END)
    return cmd_full_str


def process_serial_cmds(serial: Serial, verbose: bool = False) -> NoReturn:
    """Infinite loop to process any incoming serial command."""
    while True:
        cmd_str = get_next_serial_cmd(serial)
        try:
            cmd_name, cmd_content = protocol.parse_cmd(cmd_str)
        except Exception as e:
            print("{}\nError processing message: {!r}".format(e, cmd_str))
        else:
            if verbose:
                print(cmd_str)
            print("{} -> {}".format(cmd_name, cmd_content))
            if cmd_name in CMDS:
                CMDS[cmd_name](cmd_content)


def run(
    port: str = None, baud_rate: int = None, verbose: bool = False
) -> NoReturn:
    """Entry point to the command processor."""
    cmds_mouse.init()
    cmds_keyboard.init()
    protocol.init()
    port, baud_rate = get_serial_config(port, baud_rate)
    serial = device_serial.connect_device(port=port, baud_rate=baud_rate)
    process_serial_cmds(serial, verbose=verbose)


if __name__ == "__main__":
    run()
