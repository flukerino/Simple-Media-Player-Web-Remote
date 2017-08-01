# Simple Media Player Web Remote
A minimal Python script running a web server to serve a page with playback controls, e.g. for use on mobile devices. Each button emulates a keypress on the host (media buttons or custom buttons set as hotkeys with the media player).

## Setup
Set the HTTP port and hotkeys in config.ini. The hotkey combinations can be a comma-separated list of constant names or integer values. Refer to vk_codes.py or [this MSDN article][Virtual-Key Codes (Windows)]).

Example using the media buttons alone:

    play=VK_MEDIA_PLAY_PAUSE
    pause=VK_MEDIA_PLAY_PAUSE
    stop=VK_MEDIA_STOP
    next_track=VK_MEDIA_NEXT_TRACK
    prev_track=VK_MEDIA_PREV_TRACK


Example using a key combination of CTRL+ALT+<1,2,3,4 and 5> respectively:

    play=VK_CONTROL,VK_MENU,0x31
    pause=VK_CONTROL,VK_MENU,0x32
    stop=VK_CONTROL,VK_MENU,0x33
    next_track=VK_CONTROL,VK_MENU,0x35
    prev_track=VK_CONTROL,VK_MENU,0x34

Run server.py to start the server. 

The playback icons used are part of the GNOME theme:
http://ftp.gnome.org/pub/GNOME/sources/gnome-icon-theme/

[Virtual-Key Codes (Windows)]: https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx
