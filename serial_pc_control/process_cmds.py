#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Carlos Pereira Atencio
# SPDX-License-Identifier: MIT
"""Process and executes the commands received via serial."""
from typing import Tuple

from serial import Serial

from serial_pc_control import cmds_mouse
from serial_pc_control import cmds_keyboard
from serial_pc_control import device_serial
from serial_pc_control import protocol


CMDS = {
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
        found_device, found_port = device_serial.find_device_port()
        if not (found_port or found_device):
            raise Exception("Could not find a known device connected.")
        print("Found {} device.".format(found_device.name))
        port = found_port
        baud_rate = found_device.baud_rate
    else:
        print(
            "When autodetect is not used both the port and baud rate need to "
            "be provided."
        )
    print("Connecting to port {} at baud rate {}.".format(port, baud_rate))

    return port, baud_rate


def get_next_serial_cmd(serial: Serial) -> bytes:
    """Wait until it can return full serial command."""
    cmd_full_str = None
    while not cmd_full_str:
        cmd_full_str = serial.read_until(terminator=protocol.CMD_END)
    return cmd_full_str


def process_serial_cmds(serial) -> None:
    """Infinite loop to process any incoming serial command."""
    while True:
        cmd_str = get_next_serial_cmd(serial)
        try:
            cmd_name, cmd_content = protocol.parse_cmd(cmd_str)
        except Exception as e:
            print("Error processing message: {}\n{}".format(cmd_str))
            print(e)
        print(cmd_str)
        print("{} -> {}".format(cmd_name, cmd_content))
        if cmd_name in CMDS:
            CMDS[cmd_name](cmd_content)


def main(port: str = None, baud_rate: int = None) -> None:
    """Entry point to the command processor."""
    cmds_mouse.init()
    cmds_keyboard.init()
    protocol.init()
    port, baud_rate = get_serial_config(port, baud_rate)
    serial = device_serial.connect_device(port=port, baud_rate=baud_rate)
    process_serial_cmds(serial)


if __name__ == "__main__":
    main()
