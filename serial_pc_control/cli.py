#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Carlos Pereira Atencio
# SPDX-License-Identifier: MIT
"""Command line interface entry point."""
from typing import NoReturn

import typer  # type: ignore

from serial_pc_control import process_cmds


app = typer.Typer()


@app.command()
def run(port: str = None, baud_rate: int = None) -> NoReturn:
    """Run the Serial PC Control application."""
    process_cmds.main(port=port, baud_rate=baud_rate)


def main():
    """CLI entry point."""
    app()


if __name__ == "__main__":
    main()
