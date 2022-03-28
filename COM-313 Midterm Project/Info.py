class Info:
    def __init__(self, nAlt,nEgo, pAlt,pEgo):
        self.nAlt = nAlt
        self.nEgo = nEgo
        self.pAlt = pAlt
        self.pEgo = pEgo

    def setnAlt(self, nAlt):
        self.nAlt = nAlt

    def setnEgo(self, nEgo):
        self.nEgo = nEgo

    def setpAlt(self, pAlt):
        self.pAlt = pAlt

    def setpEgo(self, pEgo):
        self.pEgo = pEgo

    def infoTest(self):
        print(self.nAlt, self.nEgo, self.pAlt, self.pEgo)
