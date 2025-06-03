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

cl = obs.ReqClient(host='localhost', port=4455, password='EZBQzHhaaQTOPDTx', timeout=3)

# Uncomment the line below and replace your password if you've enabled authentication for your websocket
# (and comment the above cl line)
# cl = obs.ReqClient(host='localhost', port=4455, password='password-here', timeout=3)

rp = cl.get_replay_buffer_status()

# active = rp.output_active

cl.save_replay_buffer()


# if not active:
#     cl.start_replay_buffer()
# else:
#     cl.save_replay_buffer()
