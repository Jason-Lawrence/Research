import Estimate
import CoulombsLaw
import Utility
import Atom
import sys
import math
import os

def main():
    InputDir   = "C:\\Users\\Jason\\Desktop\\Projects\\Research\\ChargeDensity\\Files\\Input" # This is the directory with all of the input files to run. Needs to be set by user.
    OutputDir  = "C:\\Users\\Jason\\Desktop\\Projects\\Research\\ChargeDensity\\Files\\Output" # This directory is where all of the output files are placed. They are named "Output" + "File Name"
    HoldingDir = "C:\\Users\\Jason\\Desktop\\Projects\\Research\\ChargeDensity\\Files\\Holding" # This directory is used for placing files that have either already been run or files that don't need to be run.

    num = 1000000
    charge, rCut = init()
    for file in os.listdir(InputDir):
        Atoms, Ligands = Utility.init(InputDir, file)
        results  = CoulombsLaw.atomLoop(Atoms, Ligands)
        filtered    = filterResults(results, charge, rCut)
        Vertices = Estimate.buildLigandStructure(Ligands, rCut)
        vol      = Estimate.MonteCarlo(Ligands, Vertices, rCut, num)
        chargeDensity = calcChargeDensity(vol, filtered)
        Utility.outputGeneration(OutputDir, file, chargeDensity, vol)
        os.rename((InputDir + "\\" + file), (HoldingDir + "\\" + file))

        print("The volume of the ligand envelope is " + str(vol))
        print("The Charge Density is " + str(chargeDensity))

def init():
    try:
        if len(sys.argv) != 3:
            print("[ERROR] Not enough Arguments")
            exit(1)
        else:
            charge = float(sys.argv[1])
            rCut   = int(sys.argv[2])
            return charge, rCut

    except EnvironmentError:
        #print("[ERROR] No PQR file given")
        exit(1)

def filterResults(results, charge, rCut):
    count = 0
    filtered = []
    for res in results:
        if abs(res[0]) >= charge and res[1] <= rCut:
            print("Charge is: {0}, the distance is: {1}".format(str(res[0]), str(res[1])))
            filtered.append(res)
            count += 1
    return filtered

def calcChargeDensity(vol, charges):
    count = 0
    for charge in charges:
        count += 1
    return count / vol

main()
