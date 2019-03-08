import math
import Utility
import Atom
import os

def main():
    dir = "C:\\Users\\Jason\\Desktop\\Projects\\Research\\CoulombsLaw\\Files\\Input" # This is the directory with all of the input files to run
    for file in os.listdir(dir):
        Atoms, Ligands = Utility.init(dir, file) # This will return two lists, one for all of the Ligands and another for the General Atoms
        print("The length of the Atoms subset is: " + str(len(Atoms)))
        print("The length of the Ligands subset is: " + str(len(Ligands)))
        #results = init(Atoms, Ligands)
        #Utility.outputGeneration(results)

def init(Atoms, Ligands):
    print("hello")

main()
