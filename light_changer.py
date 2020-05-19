"""
A simple python program to allow for setting color of a WiFi connected light to the current color on screen.

Author: David Chen
"""


import requests
import pyscreenshot as ImageGrab

# Configs
# smaller screenshot region -> faster screenshot and faster dominant color determination
SCREENSHOT_REGION = (940, 520, 980, 560)  # coordinates of top left and bottom right of rectangle: (x1, y1, x2, y2)
# enabling USE_COLORTHIEF will provide better results but will run slightly slower
USE_COLORTHIEF = True  # if True, uses ColorThief to grab dominant color, otherwise just use top left pixel color


def get_color(region, colorthief=True):
    """ Screenshot a portion of the screen and return the rgb tuple of the most dominant color """
    im = ImageGrab.grab(bbox=SCREENSHOT_REGION, backend='mss', childprocess=False)
    if colorthief:  # use ColorThief module to grab dominant color from screenshot region
        from colorthief import ColorThief
        im.save('screenshot.png')
        color_thief = ColorThief('screenshot.png')
        color = color_thief.get_color(quality=1)  # dominant color

    else:
        color = im.getpixel((0, 0))  # return color of top left pixel of region
    
    return color


def set_light_color(color):
    """ Set lifx light color to provided rgb tuple """
    if sum(color) <= 30:  # color is very dark, basically black
        color = (0, 0, 100)  # set color to blue since this is the closest to darkness

    rgb = 'rgb:' + ','.join(map(str, color))  # convert (r, g, b) -> rgb:r,g,b

    token = "API TOKEN HERE"

    headers = {
        "Authorization": "Bearer %s" % token,
    }

    # brightness can be set to any value from 0.0 to 1.0, or the line can be removed
    # not always setting max brightness gives greater color accuracy; however, some colors can be pretty dim
    payload = {
        "color": rgb,
        "duration": 0.4,
        "brightness": 1.0,
    }

    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
    return response


if __name__ == '__main__':
    while True:
        try:
            color = get_color(SCREENSHOT_REGION, colorthief=USE_COLORTHIEF)
            set_light_color(color)
        except KeyboardInterrupt:
            set_light_color((255, 255, 255))  # reset light to max brightness after stopping program
            break
