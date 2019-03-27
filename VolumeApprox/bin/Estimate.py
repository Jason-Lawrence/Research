import math
import sys
import Atom
import Utility
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
    Atoms, Ligands = init()
    rCutOff = float(sys.argv[2])
    plot(Atoms, Ligands)
    Ratios = ligandLoop(Ligands, Atoms, rCutOff)
    combined = Atoms + Ligands
    center = findCenter(combined)
    vol = findVolume(center, combined)
    vols = calcIndividualVol(vol, Ratios)
    Utility.outputGeneration(vols, sys.argv[1])
    print("The volume is approximately: " + str(vol) + " Angstroms cubed")
    return 1
def init():
    try:
        if len(sys.argv) != 3:
            print("[Error] Not enough Arguments")
            exit(1)
        else:
            filePath = sys.argv[1]
            with open(filePath, 'r') as file:
                atoms, ligands = Utility.Constructor(file)
            file.close()
            return atoms, ligands

    except EnvironmentError:
        print("[Error] No PQR file given")
        exit(1)

def ligandLoop(Ligands, Atoms, rCutOff):
    Ratios = []
    for ligand in Ligands:
        count = 0
        for atom in Atoms:
            dist = getDistanceFromLigand(ligand, atom)
            if dist <= rCutOff:
                count += 1
        ratio = count / len(Atoms)
        Ratios.append((ligand.Number, ratio))
    return Ratios

def getDistanceFromLigand(ligand, atom):
        return math.sqrt(math.pow(ligand.X - atom.X, 2) + math.pow(ligand.Y - atom.Y,2) + math.pow(ligand.Z - atom.Z, 2))

def calcIndividualVol(vol, Ratios):
    vols = []
    for r in Ratios:
        vols.append((r[0], r[1] * vol))
    return vols

def findVolume(center, combined):
    distance = getFarthestPoint(center, combined)
    return (4/3) * math.pi * math.pow(distance, 3)

def getDistanceFromCenter(center, atom):
    return math.sqrt(math.pow(center[0] - atom.X, 2) + math.pow(center[1] - atom.Y,2) + math.pow(center[2] - atom.Z, 2))

def findCenter(combined):
    sumX, sumY, sumZ = 0, 0, 0

    for atom in combined:
        sumX += atom.X
        sumY += atom.Y
        sumZ += atom.Z

    centerX = sumX / len(combined)
    centerY = sumY / len(combined)
    centerZ = sumZ / len(combined)
    print("The coordinates of the center are " + str(centerX) + ", "+ str(centerY) + ", " + str(centerZ))
    return centerX, centerY, centerZ

def getFarthestPoint(center, combined):
    greatestDist = 0
    for atom in combined:
        distance = getDistanceFromCenter(center, atom)
        if greatestDist < distance:
            greatestDist = distance
            farthestAtom = atom

    return greatestDist

def plot(Atoms, Ligands):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    AtomX, AtomY, AtomZ = getXYZLists(Atoms)
    LigX, LigY, LigZ = getXYZLists(Ligands)
    ax.scatter(AtomX, AtomY, AtomZ, c='r', marker='o')
    ax.scatter(LigX, LigY, LigZ, c='b', marker='^')
    ax.set_xlabel("X Label")
    ax.set_ylabel("Y Label")
    ax.set_zlabel("Z Label")
    plt.show()

def getXYZLists(list):
    x, y, z = [], [], []
    for element in list:
        x.append(element.X)
        y.append(element.Y)
        z.append(element.Z)
    return x, y, z

main()
