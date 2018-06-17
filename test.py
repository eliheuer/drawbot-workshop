
# Variables
W, H = 595, 842 # this is rounded A4
PM = 70 # Margin around the page

# Page loop
for pn in range(20):
    newPage(W+2*PM, H+2*PM)
    # Draw the page background and frame
    fill(0.95, 0.95, 0.92)
    stroke(0)
    strokeWidth(0.5)
    rect(PM, PM, W, H)

    # Headline of the page
    fill(0.2, 0.2, 0.92)
    rect(136, 780, 458 , 50)
    # Draw a number of squares
    # And random colors
    for n in range(54):
        stroke(None)
        fill(random(), random(), random(), 0.5)
        rect(random()*200+150, random()*200+254, 224, 390)

saveImage('MyExamplePage.pdf')
saveImage('MyExamplePage.gif')
