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
        print(line)
        atomInfo = parser(line)
        if len(atomInfo) == 10: #True if there is no Chain ID. Chain ID will be set to an empty string ""
            atomInfo.insert(4, "")
        atom = buildAtom(atomInfo)

        if line[2] == "LIG":
            Ligands.append(atom)
        else:
            Atoms.append(atom)

    return Atoms, Ligands

def parser(line):
    parsed = " ".join(line.split())
    print(parsed)
    parsedLine = parsed.split(" ")
    print(parsedLine)
    return parsedLine

def buildAtom(atomInfo):
    return Atom.Atom(atomInfo[0], int(atomInfo[1]), atomInfo[2], atomInfo[3], atomInfo[4], int(atomInfo[5]), float(atomInfo[6]), float(atomInfo[7]), float(atomInfo[8]), float(atomInfo[9]), float(atomInfo[10])) 
