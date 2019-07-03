# laserMandala
Engraving Mandala Patterns with CNC Lasers
![Mandala 1](https://i.imgur.com/9oIvgoR.jpg) ![Mandala 2](https://i.imgur.com/DcLne2w.jpg)
## What it is:
This Program lets you generate G-Code for engraving Mandala Patterns with a CNC Laser.
## What you need:
A Python 3 installation.
(And a CNC Laser Cutter of course)
## How you use it:
Open the mandalaGen.py file with your text editor, adjust the parameters and execute it. You will see the Pattern being drawn on the Canvas.
Also, a new .nc-file will appear in the Folder of mandalaGen.py. That's your G-Code.
If you like the pattern, run this with your Laser and you should get a nice Mandala pattern.
## Adjustable Parameters:
### shapeNumber
This parameter determines how many different shapes will be generated.
### symmetry
The Patterns get rotated this many times to achieve a radially symmetrical Mandala.
### maxHeight
The Maximum height of any point in the Patterns.
### xOffset
The shift of the Center of the mandala from the machine zero in x-Direction.
### yOffset
The shift of the Center of the mandala from the machine zero in y-Direction.
### canvasScale
The scale of the canvas used to preview the patterns. Does not affect G-Code.
### laserEnable
This string contains the G-Code to enable the Lase. use \n for new line.
### laserDisable
This string contains the G-Code to disable the Lase. use \n for new line.
### travelSpeed
The Speed used for travelling while the Laser is disabled in your machine's speed unit.
### cutSpeed
The Speed used for cutting while the Laser is enabled in your machine's speed unit.
