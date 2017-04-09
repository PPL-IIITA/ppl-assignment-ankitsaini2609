class Couple:
    #common attributes of couples
    def __init__(self,boy,girl):
        self.boy = boy
        self.girl = girl
        self.happiness = 0
        self.GFT = []

    def set_happiness(self):
        self.happiness = self.girl.happiness + self.boy.happiness
