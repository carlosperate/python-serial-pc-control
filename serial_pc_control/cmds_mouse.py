#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module descrirption.
"""
import pyautogui


def move_up(pixels):
    pyautogui.moveRel(pixels, 0, duration=0)


def move_down(pixels):
    pixels *= -1
    pyautogui.moveRel(pixels, 0, duration=0)


def move_left(pixels):
    pixels *= -1
    pyautogui.moveRel(0, pixels, duration=0)


def move_right(pixels):
    pyautogui.moveRel(0, pixels, duration=0)


def move_vertical(pixels):
    pyautogui.moveRel(pixels, 0, duration=0)


def move_horizontal(pixels):
    pyautogui.moveRel(0, pixels, duration=0)


def left_click():
    pyautogui.click(clicks=1, interval=0, button='left')


def right_click():
    pyautogui.click(clicks=1, interval=0, button='right')


def scroll(steps)
    pyautogui.scroll(steps)


def main():
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.01


if __name__ == "__main__":
    main()
