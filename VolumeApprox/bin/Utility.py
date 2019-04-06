"""
This file was written by Jason Lawrence to be used for Professor Minh's Research Group
"""
import Atom

DEBUG = False # Helps with debugging parsing errors

def init(dir, fileName):
    filePath = dir + "\\" + fileName
    with open(filePath, 'r') as file:
        Atoms, Ligands = Constructor(file)
    file.close()
    return Atoms, Ligands

def Constructor(file):
    Atoms   = []
    Ligands = []
    for line in file.readlines():
        atomInfo = parser(line)
        Atom = buildAtom(atomInfo)
        if Atom.Residue == "LIG":
            Ligands.append(Atom)
        else:
            Atoms.append(Atom)
    return Atoms, Ligands

def parser(line):
    parsed = " ".join(line.split())
    if DEBUG: print(parsed)
    parsedLine = parsed.split(" ")
    if parsedLine[3] == "LIG": # Sets the Radius to be None
        parsedLine.append(0)
    try:
        float(parsedLine[4]) # Works if there is no Chain ID. Chain ID will be set to None
        parsedLine.insert(4, None)
    except:
        pass # Do nothing as thier is a Chain ID
    if len(parsedLine) != 11: # This is incase a  general atom doesn't have a radius.
        parsedLine.append(0)
    if DEBUG: print(parsedLine)
    return parsedLine

def buildAtom(atomInfo):
    return Atom.Atom(atomInfo[0], int(atomInfo[1]), atomInfo[2], atomInfo[3], atomInfo[4],  float(atomInfo[5]), float(atomInfo[6]), float(atomInfo[7]), float(atomInfo[8]), float(atomInfo[9]), float(atomInfo[10]))
"""
def outputGeneration(results):
    outputDir = "C:\\Users\\Jason\\Desktop\\Projects\\Research\\VolumeApprox\\Files\\Output"
    fileName = filePath.split("/")
    filePath = outputDir + "\\Outputcomplex.txt"
    outputFile = open(filePath, 'w+')
    for key in results:
        outputFile.write("Number of random points generated: " + str(key) + " ")
        for res in results[key]:
            outputFile.write(str(num) + ", " + str(ratio) + "\n")
    outputFile.close()
"""
