#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Carlos Pereira Atencio
# SPDX-License-Identifier: MIT
"""Functions to run keyboard commands on the host PC."""
import pyautogui  # type: ignore


def init() -> None:
    """Configure pyautogui for smoth keyboard operation."""
    pyautogui.FAILSAFE = False
    pyautogui.MINIMUM_DURATION = 0.0
    pyautogui.MINIMUM_SLEEP = 0.0
    pyautogui.PAUSE = 0.0


def write(text: str) -> None:
    """Types in the keyboard the given text.

    :param text: Text to type.
    """
    if not text:
        return
    pyautogui.typewrite(text, interval=0)


def press(key: str) -> None:
    """Presses a key in the keyboard.

    :param key: Key to press.
    """
    if not key:
        return
    pyautogui.press(key, interval=0.0)


def key_down(key: str) -> None:
    """Presses down a key in the keyboard.

    :param key: Key to press down.
    """
    if not key:
        return
    pyautogui.keyDown(key)


def key_up(key: str) -> None:
    """Release a key in the keyboard.

    :param key: Key to release.
    """
    if not key:
        return
    pyautogui.keyUp(key)
