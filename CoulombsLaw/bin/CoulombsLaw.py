import math
import Utility
import Atom
import os

def main():
    InputDir   = "C:\\Users\\Jason\\Desktop\\Projects\\Research\\CoulombsLaw\\Files\\Input" # This is the directory with all of the input files to run
    OutputDir  = "C:\\Users\\Jason\\Desktop\\Projects\\Research\\CoulombsLaw\\Files\\Output"
    HoldingDir = "C:\\Users\\Jason\\Desktop\\Projects\\Research\\CoulombsLaw\\Files\\Holding" # This directory is used for

    for file in os.listdir(InputDir):
        Atoms, Ligands = Utility.init(InputDir, file) # This will return two lists, one for all of the Ligands and another for the General Atoms
        print("The length of the Atoms subset is: " + str(len(Atoms)))
        print("The length of the Ligands subset is: " + str(len(Ligands)))
        results = atomLoop(Atoms, Ligands)
        Utility.outputGeneration(OutputDir, file, results)
        #os.rename((InputDir + "\\" + file), (HoldingDir + "\\" + file))


    print("All Done")

def atomLoop(Atoms, Ligands):
    k = 9 * math.pow(10, 9) # This is Coulombs constant k in N * m^2/C^2
    results = []
    for atom in Atoms:
        minDist = getDistance(atom, Ligands[0])
        closest = Ligands[0]
        for ligand in Ligands:
            dist = getDistance(atom, ligand)
            if dist < minDist: # Find the Ligand closest to the atom
                closestLigand = ligand
                minDist = dist
        force = coulombsLaw(atom, closestLigand, minDist) # calculate the force
        minDist = minDist * math.pow(10, 10) # Change the distance back to angstroms
        results.append((atom.Charge, minDist, force))
    return results

def coulombsLaw(atom, ligand, dist):
    k = 9 * math.pow(10, 9) # This is Coulombs constant k in N * m^2/C^2
    force = (k * atom.Charge * ligand.Charge) / math.pow(dist, 2)
    force = force / (4185 * (6.0221409 * math.pow(10, 23)))
    return force

def getDistance(atom, ligand):
    dist = math.sqrt(math.pow(ligand.X - atom.X, 2) + math.pow(ligand.Y - atom.Y,2) + math.pow(ligand.Z -atom.Z, 2))
    dist = dist * math.pow(10, -10)
    return dist




def getVectorAngle(atom, ligand):
    atomMag    = math.sqrt(math.pow(atom.X, 2)+ math.pow(atom.Y, 2) + math.pow(atom.Z, 2))
    ligandMag  = math.sqrt(math.pow(ligand.X, 2)+ math.pow(ligand.Y, 2) + math.pow(ligand.Z, 2))
    dotProduct = ( ligand.X * atom.X) + (ligand.Y * atom.Y) + (ligand.Z * atom.Z)
    angle = math.acos(dotProduct / (atomMag * ligandMag))
    return angle

def getUnitVector(atom, ligand):
    x = (ligand.X - atom.X) * math.pow(10, -10)
    y = (ligand.Y - atom.Y) * math.pow(10, -10)
    z = (ligand.Z - atom.Z) * math.pow(10, -10)

    vectorMag = getDistance(atom, ligand)
    ax = x/vectorMag
    ay = y/vectorMag
    az = z/vectorMag
    return (ax, ay, az)

def checkRadius(Atoms, atom):
    subset = []
    radius = atom.Radius * math.pow(10, -10)
    for a in Atoms:
        dist = getDistance(a, atom)
        if dist <= radius:
            subset.append(a)
    return subset

main()
