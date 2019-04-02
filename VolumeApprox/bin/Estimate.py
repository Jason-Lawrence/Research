import math
import sys
import Atom
import Utility
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection


def main():
    Atoms, Ligands = init()
    rCutOff = float(sys.argv[2])
    #plotLigands(Ligands)
    Vertices = buildLigandStructure(Ligands)
    #plotBoundingBox(Ligands, Vertices)
    vol = MonteCarlo(Ligands, Vertices, rCutOff)
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

def MonteCarlo(Ligands, Vertices, rCutOff):
    randPnts = generateRandomPoints(Vertices)
    hits     = checkHits(Ligands, randPnts, rCutOff)
    volBox   = calcVolBox(Vertices)
    volLigs  = volBox * (hits / len(randPnts))
    return volLigs

def generateRandomPoints(Vertices):
    randPnts = []
    for _ in range(1000):
        xval = random.gauss(Vertices[0][0], Vertices[7][0])
        yval = random.gauss(Vertices[0][1], Vertices[7][1])
        zval = random.gauss(Vertices[0][2], Vertices[7][2])
        randPnts.append((xval, yval, zval))
    return randPnts

def checkHits(Ligands, randPnts, rCutOff):
    hits = 0
    for point in randPnts:
        for lig in Ligands:
            dist = getDistanceFromLigand(lig, point)
            if dist < rCutOff:
                hits += 1
                continue
    return hits

def getDistanceFromLigand(ligand, p):
    return math.sqrt(math.pow(ligand.X - p[0], 2) + math.pow(ligand.Y - p[1], 2) + math.pow(ligand.Z - p[2], 2))

def calcVolBox(Vertices):
    width  = getDistBetweenPnts(Vertices[0], Vertices[1])
    length = getDistBetweenPnts(Vertices[0], Vertices[4])
    height = getDistBetweenPnts(Vertices[0], Vertices[2])
    vol = width * length * height
    return vol

def getDistBetweenPnts(p1, p2):
    return math.sqrt(math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2) + math.pow(p2[2] - p1[2], 2))

def buildLigandStructure(Ligands):
    LigX, LigY, LigZ = getXYZLists(Ligands)
    # Get initial values
    Xmin = LigX[0]
    Xmax = LigX[0]
    Ymin = LigY[0]
    Ymax = LigY[0]
    Zmin = LigZ[0]
    Zmax = LigZ[0]

    for x in range(len(Ligands)):
        if LigX[x] < Xmin:
            Xmin = LigX[x]

        elif LigX[x] > Xmax:
            Xmax = LigX[x]
    for x in range(len(Ligands)):
        if LigY[x] < Ymin:
            Ymin = LigY[x]

        elif LigY[x] > Ymax:
            Ymax = LigY[x]
    for x in range(len(Ligands)):
        if LigZ[x] < Zmin:
            Zmin = LigZ[x]

        elif LigZ[x] > Zmax:
            Zmax = LigZ[x]

    Vertices = []
    Xs = [Xmin, Xmax]
    Ys = [Ymin, Ymax]
    Zs = [Zmin, Zmax]

    for x in Xs:
        for y in Ys:
            for z in Zs:
                 Vertices.append((x, y, z))
    return Vertices

def plotBoundingBox(Ligands, v):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    LigX, LigY, LigZ = getXYZLists(Ligands)

    verts = [[v[0], v[2], v[3], v[1]],
             [v[4], v[5], v[7], v[6]],
             [v[0], v[4], v[6], v[2]],
             [v[0], v[1], v[5], v[4]],
             [v[2], v[3], v[7], v[6]],
             [v[1], v[3], v[7], v[5]]]

    collection = Poly3DCollection(verts, linewidths=1, edgecolors='r', alpha= 0.4)
    face_color = [0.75, 0.75, 0.75]
    collection.set_facecolor(face_color)
    ax.add_collection3d(collection)

    ax.scatter(LigX, LigY, LigZ, c='b', marker='^')

    ax.set_xlabel("X Label")
    ax.set_ylabel("Y Label")
    ax.set_zlabel("Z Label")
    plt.show()

def plotLigands(Ligands):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    LigX, LigY, LigZ = getXYZLists(Ligands)
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
