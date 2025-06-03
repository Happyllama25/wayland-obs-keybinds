# wayland-obs-keybinds
In Linux Wayland Sessions, keybinds are (currently) only sent to the focused application, breaking OBS's shortcuts function.
This small helper script is based on [Andrew Shark's original script](https://gitlab.com/AndrewShark/obs-scripts) but modified to save the replay buffer instead of start/pause recording.

### How to use
1. In OBS go to Tools --> WebSocket Server Settings
2. Enable the Websocket Server
3. Turn off Enable Authentication* and System Tray Alerts*
4. Clone or save the [`save_replay_buffer.py`](save_replay_buffer.py) to an accessible location - like `~/Videos/Clips/save_replay_buffer.py`

### Set a KDE Shortcut
1. Open your System Settings --> Shortcuts
2. Add New --> Command or Script
3. Set the Command to `python ~/Videos/Clips/replay_buffer_save.py` (or whichever path you saved it to)
4. Add your own custom shortcut (like Alt + `)
5. Apply and test the bind, look in your OBS saved recordings file to see the saved buffers (like `~/Videos/Clips/`)

# *Why turn off System Tray Alerts / Authentication?
Every time a websocket connects or disconnects - like when the script is triggered, OBS will notify you, this option removes that annoyance
You can (and should) enable authentication, you'll have to edit your `save_replay_buffer.py` to set the password 



# TODO
- Notify on saved buffer
