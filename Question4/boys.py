class Boy:
    #common attributes of all boys.

    def __init__(self,name,atr,intel,bud,mreq,typ):
        self.name = name
        self.atr = atr
        self.intel = intel
        self.bud = bud
        self.mreq = mreq
        self.status = 'single'
        self.gname = ''
        self.happiness = 0
        self.type = typ

    def is_elligible(self,mbud,atr):
        if (self.bud >= mbud) and (atr >= self.mreq):
            return True
        else:
            return False
