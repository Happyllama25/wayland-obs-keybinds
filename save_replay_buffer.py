#!/usr/bin/env python3

# Author: Happyllama25
# Homepage: https://github.com/Happyllama25/wayland-obs-keybinds

# Based on:
# Author: Andrew Shark
# Project: https://gitlab.com/AndrewShark/obs-scripts

# License: GPLv3

# This script allows you to use a single shortcut to start and save the replay buffer
# in a Wayland session

import obsws_python as obs

cl = obs.ReqClient(host='localhost', port=4455, password='generate-your-password', timeout=3)
rp = cl.get_replay_buffer_status()
active = rp.output_active

if not active:
    cl.start_replay_buffer()
else:
    cl.save_replay_buffer()
