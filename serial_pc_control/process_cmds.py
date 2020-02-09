#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Process and executes the commands received via serial."""
import re
from typing import Tuple

from serial import Serial

import cmds_mouse
import cmds_keyboard
import device_serial


CMD_START = b"$%@s-"
CMD_START_RE = b"\$\%%@s-%b@\%%\$"
CMD_TYPE_RE = b"\$\%@s-(.*?)@\%\$"
CMD_END = b"$%@end@%$\n"
CMD_END_RE = b"\$\%@end@\%\$"

CMDS = {
    'm-ckl': cmds_mouse.left_click,
    'm-ckr': cmds_mouse.right_click,
    "k-txt": cmds_keyboard.write,
}


def get_next_serial_cmd(serial: Serial) -> bytes:
    cmd_full_str = None
    while not cmd_full_str:
        cmd_full_str = serial.read_until(terminator=CMD_END)
    return cmd_full_str


def parse_serial_msg(cmd_full_str: bytes) -> Tuple[str, str]:
    if not cmd_full_str.startswith(CMD_START):
        raise ValueError("Unexpected start of message.")

    cmd_name_match = re.match(CMD_TYPE_RE, cmd_full_str)
    if not cmd_name_match:
        raise ValueError("Could not parse command type.")

    cmd_name = cmd_name_match.groups()[0]
    cmd_content_match = re.match((CMD_START_RE % cmd_name) + b"(.*?)" + CMD_END_RE, cmd_full_str, flags=re.S)
    if not cmd_content_match:
        raise ValueError("Could not parse command value.")

    cmd_content = cmd_content_match.groups()[0]
    cmd_content = cmd_content.decode("utf-8")
    cmd_name = cmd_name.decode("utf-8")
    return cmd_name, cmd_content


def process_serial_cmds(port: str = None, baud_rate: int = None) -> None:
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
        print("When autodetect is not used both the port and baud rate need "
              "to be provided.")
    print("Connecting to port {} at baud rate {}.".format(port, baud_rate))

    serial = device_serial.connect_device(port=port, baud_rate=baud_rate)
    while True:
        cmd_str = get_next_serial_cmd(serial)
        try:
            cmd_name, cmd_content = parse_serial_msg(cmd_str)
        except Exception as e:
            print("Error processing message: {}\n{}".format(cmd_str))
            print(e)
        print(cmd_str)
        print("{} -> {}".format(cmd_name, cmd_content))
        if cmd_name in CMDS:
            CMDS[cmd_name](cmd_content)


def main() -> None:
    process_serial()


if __name__ == "__main__":
    main()
