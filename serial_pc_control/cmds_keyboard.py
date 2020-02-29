#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Carlos Pereira Atencio
# SPDX-License-Identifier: MIT
"""Functions to run keyboard commands on the host PC."""
import pyautogui  # type: ignore


def init() -> None:
    """Run initialisation code. Nothing yet."""
    return


def write(text: str) -> None:
    """Types in the keyboard the given text.

    :param text: Text to type.
    """
    if not text:
        return
    pyautogui.typewrite(text, interval=0)


def press(key: str) -> None:
    """Presses a special key in the keyboard.

    :param ley: Key to press.
    """
    if not key:
        return
    pyautogui.press(key)
