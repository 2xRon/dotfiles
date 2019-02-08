# -*- coding: utf-8 -*-
#

import subprocess
import os
import os.path

from i3pystatus import Status

status = Status()

status.register("clock",
    format="%H:%M:%S",
    color='#C678DD',
    interval=1,
    on_leftclick="/usr/bin/gsimplecal",)

status.register("clock",
    format="%a %Y-%m-%d",
    color='#61AEEE',
    interval=1,)

status.register("pulseaudio",
    color_unmuted='#98C379',
    color_muted='#E06C75',
    format_muted='[muted]',
    format="{volume}%")

status.register("temp",
    color='#78EAF2',
    )
status.register("keyboard_locks",
    format='{caps} {num}',
    caps_on='Caps Lock',
    caps_off='',
    num_on='Num On',
    num_off='',
    color='#e60053',
    )

status.run()
