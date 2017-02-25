class Girl:
    #common attribute of all girls
    def __init__(self,name,atr,intel,bud):
        self.name = name
        self.atr = atr
        self.intel = intel
        self.bud = bud
        self.status = 'single'
        self.bname = ''

    def is_elligible(self,gfbud):
        if (self.bud <= gfbud):
            return True
        else:
            return False
