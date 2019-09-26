"""
This file was written by Jason Lawrence to be used for Professor Minh's Research Group
"""
class Atom:
    def __init__(self, field, num, name, res, id, resNum, x, y, z, charge, radius):
        self.Field         = field   #0
        self.Number        = num     #1
        self.Name          = name    #2
        self.Residue       = res     #3
        self.ChainID       = id      #4
        self.ResidueNumber = resNum  #5
        self.X             = x       #6
        self.Y             = y       #7
        self.Z             = z       #8
        self.Charge        = charge  #9
        self.Radius        = radius  #10
