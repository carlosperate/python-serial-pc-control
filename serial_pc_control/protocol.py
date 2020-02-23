#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Carlos Pereira Atencio
# SPDX-License-Identifier: MIT
"""Serial protocol."""
import re
from typing import Tuple

CMD_START = b"|@s-"
CMD_START_RE = b"\|@s-%b@\|"  # noqa: W605
CMD_TYPE_RE = b"\|@s-(.*?)@\|"  # noqa: W605
CMD_END = b"|@e@|\n"
CMD_END_RE = b"\|@e@\|"  # noqa: W605


def init() -> None:
    """Initialise the protocol. Nothing to do here yet."""
    pass


def parse_cmd(cmd_full_str: bytes) -> Tuple[str, str]:
    """Parse the type of a command from a full messsage."""
    if not cmd_full_str.startswith(CMD_START):
        raise ValueError("Unexpected start of message.")

    cmd_name_match = re.match(CMD_TYPE_RE, cmd_full_str)
    if not cmd_name_match:
        raise ValueError("Could not parse command type.")

    cmd_name = cmd_name_match.groups()[0]
    cmd_content_match = re.match(
        (CMD_START_RE % cmd_name) + b"(.*?)" + CMD_END_RE,
        cmd_full_str,
        flags=re.S,
    )
    if not cmd_content_match:
        raise ValueError("Could not parse command value.")

    cmd_content = cmd_content_match.groups()[0]
    return cmd_name.decode("utf-8"), cmd_content.decode("utf-8")
