#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Carlos Pereira Atencio
# SPDX-License-Identifier: MIT
"""
Helper module to detect the serial port of known boards and connect to them.

Or connect to any other serial port.
"""
from collections import namedtuple
from typing import Tuple, Optional

from serial import Serial, PARITY_NONE, STOPBITS_ONE
from serial.tools import list_ports


# Devices added in priority order
DeviceInfo = namedtuple("DeviceInfo", ["name", "vid", "pid", "baud_rate"])
DEVICES = [
    DeviceInfo(name="microbit", vid=0x0D28, pid=0x0204, baud_rate=115200),
    DeviceInfo(name="arduino_uno_0", vid=0x2341, pid=0x0043, baud_rate=9600),
    DeviceInfo(name="arduino_uno_1", vid=0x2341, pid=0x0001, baud_rate=9600),
    DeviceInfo(name="arduino_uno_2", vid=0x2A03, pid=0x0043, baud_rate=9600),
    DeviceInfo(name="arduino_uno_3", vid=0x2341, pid=0x0243, baud_rate=9600),
]


def find_device_port() -> Tuple[Optional[DeviceInfo], Optional[str]]:
    """Iterate through available serial ports until the first match."""
    comports = list_ports.comports()
    for device in DEVICES:
        for port in comports:
            if (port.pid == device.pid) and (port.vid == device.vid):
                return device, port.device
    return None, None


def connect_device(port: str, baud_rate: int) -> Serial:
    """Connect to a given serial port at a given baud rate."""
    return Serial(
        port,
        baud_rate,
        timeout=1,
        parity=PARITY_NONE,
        stopbits=STOPBITS_ONE,
        rtscts=False,
        dsrdtr=False,
    )
