import requests
import pyscreenshot as ImageGrab
from colorthief import ColorThief


def get_dominant_colour():
    """ Screenshot a portion of the screen and return the rgb tuple of the most dominant color """
    im = ImageGrab.grab(bbox=(0, 1060, 10, 1080), backend='mss', childprocess=False)
    im.save('screenshot.png')
    color_thief = ColorThief('screenshot.png')
    dominant_color = color_thief.get_color(quality=1)
    
    return dominant_color


def set_light_color(color):
    """ Set lifx light color to provided rgb tuple """
    rgb = 'rgb:' + ','.join(map(str, color))  # convert (r, g, b) -> rgb:r,g,b

    token = ""

    headers = {
        "Authorization": "Bearer %s" % token,
    }

    payload = {
        "color": rgb,
    }

    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
    return response


if __name__ == '__main__':
    while True:
        try:
            color = get_dominant_colour()
            set_light_color(color)
        except KeyboardInterrupt:
            set_light_color((255, 255, 255))
            break


