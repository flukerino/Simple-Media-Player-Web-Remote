import os
import sys
import time
import win32api

import config

def send_key_combination(vks, ms=100):
    KEYEVENTF_EXTENDEDKEY = 0x0001
    KEYEVENTF_KEYUP = 0x0002
    keys = [] 
    for vk in vks:
        keys.append((vk,win32api.MapVirtualKey(vk, 0)))
    for vk,hw in keys:
        win32api.keybd_event(vk, hw)
    time.sleep(ms/1000)
    for vk,hw in keys:
        win32api.keybd_event(vk, hw, KEYEVENTF_KEYUP)
        
def play():
    send_key_combination(config.KEYCOMB_PLAY)
    
def pause():
    send_key_combination(config.KEYCOMB_PAUSE)
    
def stop():
    send_key_combination(config.KEYCOMB_STOP)
        
def previous_track():
    send_key_combination(config.KEYCOMB_PREV_TRACK)
    
def next_track():
    send_key_combination(config.KEYCOMB_NEXT_TRACK)