#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Helper module to detect the serial port of known boards and connect to them.
"""
from collections import namedtuple

from serial import Serial, PARITY_NONE, STOPBITS_ONE
from serial.tools import list_ports


# Devices added in priority order
DeviceInfo = namedtuple('DeviceInfo', ['name','vid', 'pid', 'baud_rate'])
DEVICES = [
    DeviceInfo(name='microbit', vid=0x0D28, pid=0x0204, baud_rate=115200),
    DeviceInfo(name='arduino_uno_0', vid=0x2341, pid=0x0043, baud_rate=9600),
    DeviceInfo(name='arduino_uno_1', vid=0x2341, pid=0x0001, baud_rate=9600),
    DeviceInfo(name='arduino_uno_2', vid=0x2A03, pid=0x0043, baud_rate=9600),
    DeviceInfo(name='arduino_uno_3', vid=0x2341, pid=0x0243, baud_rate=9600),
]


def find_device_port():
    comports = list_ports.comports()
    for device in DEVICES:
        for port in comports:
            if (port.pid == device.pid) and (port.vid == device.vid):
                return device, port.device
    return None, None


def connect_device(port=None, baud_rate=None):
    found_device, found_port = find_device_port()
    if not port:
        port = found_port
        if not port:
            raise Exception("No device specified nor found.")
    if not baud_rate:
        if not found_device:
            raise Exception("Baud rate not specified and device not found.")
        baud_rate = found_device.baud_rate

    return Serial(
            port, baud_rate, timeout=1, parity=PARITY_NONE,
            stopbits=STOPBITS_ONE, rtscts=False, dsrdtr=False)
