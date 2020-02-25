#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Carlos Pereira Atencio
# SPDX-License-Identifier: MIT
"""Package main entry point, goes to the CLI."""

from serial_pc_control import cli


def main():
    """Entry point for the Serial PC Control Python package."""
    cli.main()


if __name__ == "__main__":
    main()
