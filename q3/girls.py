from common import Common
class Girl(Common):
    #common attribute of all girls
    def __init__(self,name,atr,intel,bud,typ):
        Common.__init__(self,name,atr,intel,typ,bud)
        self.status = 'single'
        self.bname = ''
        self.happiness = 0

    def is_elligible(self,gfbud):
        if (self.bud <= gfbud):
            return True
        else:
            return False
