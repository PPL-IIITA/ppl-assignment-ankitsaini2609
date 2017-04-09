from common import Common
class Boy(Common):
    #common attributes of all boys.
    def __init__(self,name,atr,intel,bud,mreq,typ):
        Common.__init__(self,name,atr,intel,typ,bud)
        self.mreq = mreq
        self.status = 'single'
        self.gname = ''
        self.happiness=0

    def is_elligible(self,mbud,atr):
        if (self.bud >= mbud) and (atr >= self.mreq):
            return True
        else:
            return False
