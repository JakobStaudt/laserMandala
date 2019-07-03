import turtle
import random
import math

shapeNumber = 4
symmetry = 12
maxHeight = 30

xOffset = 0
yOffset = 0

scale = 10

laserEnable = ";Enabling Laser\nM400\nG4 P500\nM106\nM400\n"
laserDisable = ";Disabling Laser\nM400\nM107\nM400\n"

gCode = "G90\nG0 F3000\nG1 F1200\n"

turtle.speed(0)

def randShape():
    shapeType = random.randint(1,20)
    if shapeType <= 10:
        shapeType = 1
    elif shapeType <= 15:
        shapeType = 2
    else:
        shapeType = 3
        
    if shapeType == 1:
        print("pattern")
        points = [[0, 0]]
        height = random.randint(maxHeight // 2, maxHeight)
        for x in range(random.randint(3, 4)):
            y = random.randint(0, height)
            x = random.randint(0, y + 10)
            point = [x, y]
            points.append(point)
        pointsBuf = points.copy()
        points.append([0, height])
        for point in pointsBuf[::-1]:
            points.append([-point[0], point[1]])

        shapePoints =  []

        for i in range(symmetry):
            degangle = (i / symmetry) * 360.0
            for point in points:
                angle = math.radians(degangle)
                oldx = point[0]
                oldy = point[1]
                x = oldx * math.cos(angle) - oldy * math.sin(angle)
                y = oldy * math.cos(angle) + oldx * math.sin(angle)
                shapePoints.append([x, y])
            shapePoints.append("newShape")

        return shapePoints

    elif shapeType == 2:
        points = []
        step = random.randint(1, 3)
        if step == 1:
            step = 10
            print("circle")
        if step == 2:
            step = (360/symmetry)
            print("symmetryagon")
        if step == 3:
            step = (360/symmetry) * 2
            print("half symmetryagon")
        step = int(step)
        r = random.randint(maxHeight // 3, maxHeight)
        for angle in range(0, 360, step):
            angle = math.radians(angle)
            x = r * math.cos(angle)
            y = r * math.sin(angle)
            points.append([x, y])
        points.append([r, 0])
        return points

    elif shapeType == 3:
        print("offsetCircles")
        points = []
        step = 20
        hOffset = random.randint(10, maxHeight)
        r = random.randint(3, maxHeight // 4)
        for angle in range(0, 360, step):
            angle = math.radians(angle)
            x = r * math.cos(angle)
            y = r * math.sin(angle) + hOffset
            points.append([x, y])
        points.append([r, hOffset])

        shapePoints =  []

        for i in range(symmetry):
            degangle = (i / symmetry) * 360.0
            for point in points:
                angle = math.radians(degangle)
                oldx = point[0]
                oldy = point[1]
                x = oldx * math.cos(angle) - oldy * math.sin(angle)
                y = oldy * math.cos(angle) + oldx * math.sin(angle)
                shapePoints.append([x, y])
            shapePoints.append("newShape")

        return shapePoints


def drawShape(shape):
    penPos = False
    global gCode
    turtle.goto(shape[0][0] * scale, shape[0][1] * scale)
    turtle.pendown()
    penPos = True
    #gCode += "G0 X" + str(shape[0][0] + xOffset) + " Y" + str(shape[0][1] + yOffset) + " Z10\n"
    x = shape[0][0] + xOffset
    y = shape[0][1] + yOffset
    gCode += "G0 X" + str(format(x, '.4f')) + " Y" + str(format(y, '.4f')) + " Z0\n"
    gCode += laserEnable
    for point in shape[1:]:
        if point == "newShape":
            penPos = False
            turtle.penup()
            gCode += laserDisable
        else:
            x = point[0]
            y = point[1]
            turtle.goto(x * scale, y * scale)
            x += xOffset
            y += yOffset
            gCode += "G1 X" + str(format(x, '.4f')) + " Y" + str(format(y, '.4f')) + " Z0\n"
            if not penPos:
                turtle.pendown()
                gCode += laserEnable
                penPos = True
    turtle.penup()
    gCode += laserDisable
    #gCode += "G0 X" + str(x) + " Y" + str(y) + " Z10\n"

turtle.penup()

shapes = []
for i in range(shapeNumber):
    shape = randShape()
    shapes.append(shape)

for shape in shapes:
    drawShape(shape)

f = open("test.nc", "w")
f.write(gCode)
f.close()

_ = input()
