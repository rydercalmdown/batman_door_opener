import time
from nanoleafapi import discovery, Nanoleaf


def get_nanoleaf_obj():
    """Setup the nanoleaf"""
    print('Setting up nanoleaf')
    nanoleaf_ip = '10.0.0.1'
    return Nanoleaf(nanoleaf_ip)


nano = get_nanoleaf_obj()


def set_nanoleaf_colour(colour):
    # nano.toggle_power()
    nano.set_color(colour) 


def flash_colour(colour, loops=3, delay=0.2):
    count = 0
    nano.set_color(colour)
    time.sleep(delay)
    while count < loops + 1:
        nano.set_color(colour)
        time.sleep(delay)
        nano.set_color((25, 0, 0))
        time.sleep(delay)
        count = count + 1
    nano.set_color(colour)


def pulsate(colour):
    nano.pulsate(colour, 3)
