class Girl:
    #common attribute of all girls
    def __init__(self,name,atr,intel,bud,typ):
        self.name = name
        self.atr = atr
        self.intel = intel
        self.bud = bud
        self.status = 'single'
        self.bname = ''
        self.happiness = 0
        self.type = typ

    def is_elligible(self,gfbud):
        if (self.bud <= gfbud):
            return True
        else:
            return False
