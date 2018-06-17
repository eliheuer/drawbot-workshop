import os

A4 = 595, 842

class Image(object):
    def __init__(self, path, x, y, w, h):
        self.path = path
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
    def draw(self, page):
        #Headline
        fill(random(), random(), random())
        stroke(None)
        rect(page.padding+self.x, page.padding+self.y, self.w, self.h)
        fontSize(32)
        font('Verdana')
        fill(0)
 
class Text(object):
    def __init__(self, s, x, y, w, h):
        self.s = s
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
    def draw(self, page):
        #Headline
        fill(0.8)
        stroke(None)
        rect(page.padding, page.padding, self.w, self.h)
        fontSize(32)
        font('Verdana')
        fill(0)
        text('Headline of the article', (page.padding, page.h-2*page.padding))
        
class Page(object):
    def __init__(self, w, h, title=None, padding=None):
        self.w = w
        self.h = h
        self.title = title or 'untitled'
        self.padding = padding or 20
        self.elements = []

    def __repr__(self):
        #return 'test'
        return '%s(w=%d,h=%d,%s)' % (self.__class__.__name__, self.w, self.h, self.title)

    def draw(self):
        newPage(self.w, self.h)
        stroke(0.6)
        fill(None)
        # Info
        rect(self.padding, self.padding, self.w-2*self.padding, self.h-2*self.padding)
        
        for element in self.elements:
            element.draw(self)
            
#-------------------

W, H = A4
page = Page(W, H, 'MySpread')
page.elements.append(Text('Hello World', 0, 400, 23, 45))
page.elements.append(Image('aaa', 0, 300, 50, 50))
page.elements.append(Image('aaa', 0, 394, 150, 150))
page.draw()

saveImage('example.pdf')