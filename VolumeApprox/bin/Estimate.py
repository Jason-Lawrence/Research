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
    #num     = int(sys.argv[3])
    #plotLigands(Ligands)
    Vertices = buildLigandStructure(Ligands, rCutOff)
    #plotBoundingBox(Ligands, Vertices)
    #testNumRandomPoints(Ligands, Vertices)
    testrCutOffGrowth(Ligands, Vertices)
    #print("The volume is approximately: " + str(vol) + " Angstroms cubed")
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

def testNumRandomPoints(Ligands, Vertices):
    rCutOff = 5
    nums = [10000, 50000, 100000, 500000, 1000000, 1500000, 2000000]
    results = {}
    countout = 0
    for num in nums:
        countin = 0
        sum = 0
        for _ in range(10):
            countin += 1
            vol = MonteCarlo(Ligands, Vertices, rCutOff, num)
            sum += vol
            if num not in results:
                results[num] = [vol]
            else:
                results[num].append(vol)
            print("Count: " + str(countin))
        avg = sum / countin
        results[num].append(avg)
        print("For " + str(num) + " points randomly generated")
        print("Results: " + str(results[num]))
        print("The Avg. is " + str(avg))
    analyzeResults(results)
    return 1

def analyzeResults(results):
    # Calculate the standard deviation for each key
    fig = plt.figure()
    for key in results:
        sum = 0
        mean = results[key].pop(len(results[key])-1)
        for res in results[key]:
            sum += (math.pow(res - mean, 2))
        stdDev = math.sqrt(sum / len(results[key]))
        Min = min(results[key])
        Max = max(results[key])
        x = [key, key, key]
        y = [Min, Max, mean]
        plt.scatter(x, y)
    plt.show()

def testrCutOffGrowth(Ligands, Vertices):
    num = 1000000
    rCutOff = 5
    results = {}
    for _ in range(10):
        sum = 0
        for _ in range(5):
            vol = MonteCarlo(Ligands, Vertices, rCutOff, num)
            sum += vol
        avg = sum / 5
        results[rCutOff] = avg
        print("rCutOff: " + str(rCutOff) + " , Volume: " + str(results[rCutOff]))
        rCutOff += 1
    analyzerCutOff(results)

def analyzerCutOff(results):
    fig = plt.figure()
    x = []
    y = []
    for key in results:
        x.append(key)
        y.append(results[key])
    plt.scatter(x, y)
    plt.xlabel("rCutOff")
    plt.ylabel("Volume")
    plt.show()

def MonteCarlo(Ligands, Vertices, rCutOff, num):
    randPnts = generateRandomPoints(Vertices, num)
    hits     = checkHits(Ligands, randPnts, rCutOff)
    volBox   = calcVolBox(Vertices)
    volLigs  = volBox * (float(hits) / len(randPnts))
    return volLigs

def generateRandomPoints(Vertices, num):
    randPnts = []
    for _ in range(num):
        xval = random.uniform(Vertices[0][0], Vertices[7][0])
        yval = random.uniform(Vertices[0][1], Vertices[7][1])
        zval = random.uniform(Vertices[0][2], Vertices[7][2])
        randPnts.append((xval, yval, zval))
    return randPnts

def checkHits(Ligands, randPnts, rCutOff):
    hits = 0
    for point in randPnts:
        hits += checkPoint(Ligands, point, rCutOff)
    return hits

def checkPoint(Ligands, point, rCutOff):
    for lig in Ligands:
        dist = getDistanceFromLigand(lig, point)
        if dist <= rCutOff:
            return 1
    return 0

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

def buildLigandStructure(Ligands, rCutOff):
    LigX, LigY, LigZ = getXYZLists(Ligands)
    # Get initial values
    Xmin = LigX[0] - rCutOff
    Xmax = LigX[0] + rCutOff
    Ymin = LigY[0] - rCutOff
    Ymax = LigY[0] + rCutOff
    Zmin = LigZ[0] - rCutOff
    Zmax = LigZ[0] + rCutOff

    for x in range(len(Ligands)):
        if LigX[x] - rCutOff < Xmin:
            Xmin = LigX[x] - rCutOff

        elif LigX[x] + rCutOff > Xmax:
            Xmax = LigX[x] + rCutOff
    for x in range(len(Ligands)):
        if LigY[x] - rCutOff < Ymin:
            Ymin = LigY[x] - rCutOff

        elif LigY[x] + rCutOff > Ymax:
            Ymax = LigY[x] + rCutOff
    for x in range(len(Ligands)):
        if LigZ[x] - rCutOff < Zmin:
            Zmin = LigZ[x] - rCutOff

        elif LigZ[x] + rCutOff > Zmax:
            Zmax = LigZ[x] + rCutOff

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
