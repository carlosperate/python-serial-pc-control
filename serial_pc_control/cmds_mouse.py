#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions to run mouse commands on the host PC."""
import pyautogui


def move_up(pixels: str) -> None:
    """Moves the mouse up a number of pixels.

    :param pixels: Number of pixels to move the mouse pointer.
    """
    pyautogui.moveRel(pixels, 0, duration=0)


def move_down(pixels: str) -> None:
    """Moves the mouse down a number of pixels.

    :param pixels: Number of pixels to move the mouse pointer.
    """
    pixels *= -1
    pyautogui.moveRel(pixels, 0, duration=0)


def move_left(pixels: str) -> None:
    """Moves the mouse left a number of pixels.

    :param pixels: Number of pixels to move the mouse pointer.
    """
    pixels *= -1
    pyautogui.moveRel(0, pixels, duration=0)


def move_right(pixels: str) -> None:
    """Moves the mouse right a number of pixels.

    :param pixels: Number of pixels to move the mouse pointer.
    """
    pyautogui.moveRel(0, pixels, duration=0)


def move_vertical(pixels: str) -> None:
    """Moves the mouse vertically a number of pixels.

    :param pixels: Number of pixels to move the mouse pointer, a positive
        number will move up and negative down.
    """
    pyautogui.moveRel(pixels, 0, duration=0)


def move_horizontal(pixels: str) -> None:
    """Moves the mouse horizontally a number of pixels.

    :param pixels: Number of pixels to move the mouse pointer, a positive
        number will move right and negative left.
    """
    pyautogui.moveRel(0, pixels, duration=0)


def left_click(throw_away: None = None) -> None:
    """Performs a left click action.

    :param throw_away: The command parser always sends a parameter, for this
        command nothing is expected, so it will throw an error if something is
        sent.
    """
    if throw_away:
        raise ValueError("The left click command does not expect a value.")
    pyautogui.click(clicks=1, interval=0, button='left')


def right_click(throw_away: None = None) -> None:
    """Performs a right click action.

    :param throw_away: The command parser always sends a parameter, for this
        command nothing is expected, so it will throw an error if something is
        sent.
    """
    if throw_away:
        raise ValueError("The right click command does not expect a value.")
    pyautogui.click(clicks=1, interval=0, button='right')


def scroll(steps: str) -> None:
    """Moves the mouse horizontally a number of pixels.

    :param pixels: Number of pixels to move the mouse pointer, a positive
        number will move right and negative left.
    """
    pyautogui.scroll(steps)


def main() -> None:
    """Main entry point."""
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.01


if __name__ == "__main__":
    main()
