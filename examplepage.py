
# Variables
W, H = 595, 842 # this is rounded A4
PM = 70 # Margin around the page
Padding = 40
Frames = 20

# Page loop
for pn in range(20):
    # Draw the page background and frame
    print(pn)
    newPage(W+2*PM, H+2*PM)
    fill(0)
    stroke(0,0,1)
    strokeWidth(0.5)
    rect(PM, PM, W, H)
    
    # Draw a number of squares and random colors
    for n in range(54):
        stroke(None)
        fill(random(), random(), random(), 0.5)
        rect(random()*200+100, random()*200+16, 224, 390)
    
    # Headline of the page
    # x = Margin left (PM) + padding inside page
    # y = Margin bottom (PM) + height - top padding
    # Calculate the angle stepping through 360 degrees by frames
    angle = pn/Frames*360
    # Calculate the sin value of the angle and scale vertical
    # by 50% and move
    # 0.5 moves and transforms the sine wave
    fontSize = (sin(radians(angle))*0.5+0.5)*160+50
    print(pn, angle, fontSize)
    
    fs = FormattedString('Hello World', fontSize=fontSize, fill=1, stroke=None)
    tw, th = textSize(fs)
    text(fs, (PM+W/2-tw/2, PM+H-Padding-th ))


saveImage('MyExamplePage.pdf')
saveImage('MyExamplePage.gif')
