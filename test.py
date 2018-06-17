# Test
print('hello world'*10)
print(231231 * 646464)
print(random())

fill(0.95, 0.95, 0.92)
stroke(0)
strokeWidth(0.5)

# main
rect(254, 72, 500 ,842)

for n in range(50):
    fill(random(), random(), random())
    rect(random()*200+150, random()*200+254, 224, 390)

rect(200, 200, 340, 50)
saveImage('MyExamplePage.pdf')