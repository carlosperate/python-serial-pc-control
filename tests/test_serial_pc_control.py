#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Carlos Pereira Atencio
# SPDX-License-Identifier: MIT
"""Package tests."""
from serial_pc_control import __version__


def test_version():
    """Test the version is correct."""
    assert __version__ == "0.1.0"
