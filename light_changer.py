import requests
import pyscreenshot as ImageGrab


def get_color():
    """ Screenshot a portion of the screen and return the rgb tuple of the most dominant color """
    im = ImageGrab.grab(bbox=(0, 1079, 1, 1080), backend='mss', childprocess=False)
    im.save('screenshot.png')
    color = im.getpixel((0, 0))
    
    return color


def set_light_color(color):
    """ Set lifx light color to provided rgb tuple """
    rgb = 'rgb:' + ','.join(map(str, color))  # convert (r, g, b) -> rgb:r,g,b

    token = "API TOKEN HERE"

    headers = {
        "Authorization": "Bearer %s" % token,
    }

    payload = {
        "color": rgb,
        "duration": 0.3,
        "brightness": 1.0,
    }

    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
    return response


if __name__ == '__main__':
    while True:
        try:
            color = get_color()
            set_light_color(color)
        except KeyboardInterrupt:
            set_light_color((255, 255, 255))
            break


