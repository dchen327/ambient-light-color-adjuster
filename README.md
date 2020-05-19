## Introduction:
This is a simple python program that changes the color of my Lifx A19 bulb to the 
color on my screen.

## Usage:
Currently this program only works for lifx bulbs and linux. However, if your lightbulb 
has an api, it shouldn't be too hard to configure it. I'm using pyscreenshot to take 
a screenshot of a single pixel to find its color, but on other OSes other python modules 
can be used. Finally, if the one pixel sample is too small, experimenting with ColorThief
can make it easier to grab the dominant color from an image. Use Ctrl+C to stop the program.

## Demo:
![GeometryDash](https://user-images.githubusercontent.com/37674516/82279834-6f80b100-995b-11ea-9344-ab22306bae63.gif)
