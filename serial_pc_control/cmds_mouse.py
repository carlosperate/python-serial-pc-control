#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Carlos Pereira Atencio
# SPDX-License-Identifier: MIT
"""Functions to run mouse commands on the host PC."""
import pyautogui


def init() -> None:
    """Configure pyautogui for smooth mouse movement."""
    pyautogui.FAILSAFE = False
    pyautogui.MINIMUM_DURATION = 0.0
    pyautogui.MINIMUM_SLEEP = 0.0
    pyautogui.PAUSE = 0.0


def move_up(pixels: str) -> None:
    """Move the mouse up a number of pixels.

    :param pixels: Number of pixels to move the mouse pointer.
    """
    pyautogui.moveRel(
        xOffset=int(pixels), yOffset=0, duration=0.0, pause=None, _pause=False
    )


def move_down(pixels: str) -> None:
    """Move the mouse down a number of pixels.

    :param pixels: Number of pixels to move the mouse pointer.
    """
    pixels *= -1
    pyautogui.moveRel(
        xOffset=int(pixels), yOffset=0, duration=0.0, pause=None, _pause=False
    )


def move_left(pixels: str) -> None:
    """Move the mouse left a number of pixels.

    :param pixels: Number of pixels to move the mouse pointer.
    """
    pixels *= -1
    pyautogui.moveRel(
        xOffset=0, yOffset=int(pixels), duration=0.0, pause=None, _pause=False
    )


def move_right(pixels: str) -> None:
    """Move the mouse right a number of pixels.

    :param pixels: Number of pixels to move the mouse pointer.
    """
    pyautogui.moveRel(
        xOffset=0, yOffset=int(pixels), duration=0.0, pause=None, _pause=False
    )


def move_vertical(pixels: str) -> None:
    """Move the mouse vertically a number of pixels.

    :param pixels: Number of pixels to move the mouse pointer, a positive
        number will move up and negative down.
    """
    pyautogui.moveRel(
        xOffset=0, yOffset=int(pixels), duration=0.0, pause=None, _pause=False
    )


def move_horizontal(pixels: str) -> None:
    """Move the mouse horizontally a number of pixels.

    :param pixels: Number of pixels to move the mouse pointer, a positive
        number will move right and negative left.
    """
    pyautogui.moveRel(
        xOffset=int(pixels), yOffset=0, duration=0.0, pause=None, _pause=False
    )


def move_relative(pixels_x_y: str) -> None:
    """Move the mouse horizontally a number of pixels.

    :param pixels: Number of pixels to move the mouse pointer, a positive
        number will move right and negative left.
    """
    x_and_y = pixels_x_y.split(" ")
    x = int(x_and_y[0])
    y = int(x_and_y[1])
    pyautogui.moveRel(
            xOffset=x, yOffset=y, duration=0.0, pause=None, _pause=False)


def left_click(throw_away: None = None) -> None:
    """Perform a left click action.

    :param throw_away: The command parser always sends a parameter, for this
        command nothing is expected, so it will throw an error if something is
        sent.
    """
    if throw_away:
        raise ValueError("The left click command does not expect a value.")
    pyautogui.click(clicks=1, interval=0.0, button="left")


def right_click(throw_away: None = None) -> None:
    """Perform a right click action.

    :param throw_away: The command parser always sends a parameter, for this
        command nothing is expected, so it will throw an error if something is
        sent.
    """
    if throw_away:
        raise ValueError("The right click command does not expect a value.")
    pyautogui.click(clicks=1, interval=0.0, button="right")


def scroll(steps: str) -> None:
    """Move the mouse horizontally a number of pixels.

    :param steps: Number of pixels to move the mouse pointer, a positive
        number will move right and negative left.
    """
    pyautogui.scroll(steps)
