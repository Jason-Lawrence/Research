"""
This file holds utility functions to be used. This entails opening, parsing, and loading files into the program.
It builds all of the Atoms in the file and provides a list of general atoms and a list of ligands
At the end of the program it takes the results and writes it to a file.
This file was written by Jason Lawrence to be used for Professor Minh's Research Group
"""
import Atom

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
    parsedLine = parsed.split(" ")
    if parsedLine[3] == "LIG": # Sets the Radius to be None
        parsedLine.append(0)
    try:
        float(parsedLine[4]) # Works if there is no Chain ID. Chain ID will be set to None
        parsedLine.insert(4, None)
    except:
        pass # Do nothing as thier is a Chain ID
    while len(parsedLine) < 11:
        parsedLine.append(0)
    return parsedLine

def buildAtom(atomInfo):
    return Atom.Atom(atomInfo[0], int(atomInfo[1]), atomInfo[2], atomInfo[3], atomInfo[4],  float(atomInfo[5]), float(atomInfo[6]), float(atomInfo[7]), float(atomInfo[8]), float(atomInfo[9]), float(atomInfo[10]))

def outputGeneration(dir, file, results):
    filePath = dir + "\\Output" + file
    outputFile = open(filePath, 'w+')
    for charge, distance, force in results:
        outputFile.write(str(charge) + ", " + str(distance) + ", " + str(force) + "\n")
    outputFile.close()
