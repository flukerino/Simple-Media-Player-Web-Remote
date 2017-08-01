import configparser
import os

from vk_codes import VirtualKey


config = configparser.ConfigParser()
config_filename = "config.ini"
if len(config.read(config_filename)) == 0:
    config["Server"] = { }
    config["Server"]["port"] = "8080"
    config["Keys"] = { }
    config["Keys"]["play"] = "VK_MEDIA_PLAY_PAUSE"
    config["Keys"]["pause"] = "VK_MEDIA_PLAY_PAUSE"
    config["Keys"]["stop"] = "VK_MEDIA_STOP"
    config["Keys"]["next_track"] = "VK_MEDIA_NEXT_TRACK"
    config["Keys"]["prev_track"] = "VK_MEDIA_PREV_TRACK"
    if not os.path.exists(config_filename):
        with open(config_filename, "w") as f:
            config.write(f)

# Parse comma-separated string of either VK constants or integer (hex/decimal) values into list of integer values
def parse_key(input):
    keys = []
    if "," in input:
        keys = input.split(",")
    else:
        keys = [input]
    resolved = []
    for key in keys:
        if hasattr(VirtualKey, key):
            resolved.append(getattr(VirtualKey, key))
        else:
            resolved.append(int(key, 16 if key.startswith("0x") else 10))
    return resolved

SERVER_PORT = int(config["Server"]["port"])
KEYCOMB_PLAY = parse_key(config["Keys"]["play"])
KEYCOMB_PAUSE = parse_key(config["Keys"]["pause"])
KEYCOMB_STOP = parse_key(config["Keys"]["stop"])
KEYCOMB_PREV_TRACK = parse_key(config["Keys"]["prev_track"])
KEYCOMB_NEXT_TRACK =  parse_key(config["Keys"]["next_track"])