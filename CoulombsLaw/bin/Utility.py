def init():
    dir = "C:\\Users\\Jason\\Desktop\\Projects\\Research\\CoulombsLaw\\Files" ## replace this with where ever the file is located
    file = open(dir + "\\complex.pqr") #replace this with the file name
    return Constructor(file)

def Constructor(file):
     Atoms   = []
     Ligands = []

     for line
