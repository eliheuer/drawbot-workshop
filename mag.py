
A4 = 595, 842

class Page(object):

    def __init__(self, w, h, title=None, padding=None):
        self.w = w
        self.h = h
        self.title = title or 'untitled'
        self.padding = padding or 20

    def __repr__(self):
        return 'test'
        #return '%s(w=%d,h=%d)' %(self.__class__.__name__, self.w, self.h, self.title)

    def draw(self):
        newPage(self.w, self.h)
        stroke(0.6)
        fill(None)
        rect(self.padding, self,padding,
            self.w-2*self.padding, self.h-2*self.padding)
            
#-------------------

W, H = A4
page = Page(W, H, 'MySpread')
print(page)
page.draw()





