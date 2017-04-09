class Couple:
    #common attributes of couples
    def __init__(self,boy,girl):
        self.boy = boy
        self.girl = girl
        self.happiness = 0
        self.compatibility = 0
        self.GFT = []

    def set_happiness(self):
        self.happiness = self.girl.happiness + self.boy.happiness

    def set_compatibility(self):
        m = self.boy.bud - self.girl.bud
        n = abs(self.boy.intel - self.girl.intel)
        o = abs(self.boy.atr - self.girl.atr)
        self.compatibility = m+n+o
