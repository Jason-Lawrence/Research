# Documentation
#### Professor Minh's Research Group
#### By Jason Lawrence

## Setup/How to run
In the command line navigate to the directory where Estimate.py is saved and then type the following: Estimate.py [Input File] [rCutOff].
The output will be the volume of the ligand structure in Angstroms cubed.

## File Descriptions

## Atom.py

This file holds the class that defines the atom object that will be used for the script.

#### Attributes
|Attribute|Data Type|Description|
|:--------|:--------|:----------|
|Field        |String   |Either "ATOM" or "HETATM" |
|Number       |Int      |The Index of the atom     |
|Name         |String   |Name of the Atom          |
|Residue      |String   |The name of the residue   |
|Chain ID     |String   |Optional String Identifier for the chain ID of the atom|
|ResidueNumber|Int      |THe index of the Residue  |
|X Coordinate |Float    |Describes the location in the X direction in (A)|
|Y Coordinate |Float    |Describes the location in the y direction in (A)|
|Z Coordinate |Float    |Describes the location in the z direction in (A)|
|Charge       |Float    |Describes the charge on the Atom in (C)|
|Radius       |Float    |Describes the Radius of the Atom in (A)|

## Utility.py

This file holds utility functions to be used. This entails opening, parsing, and loading files into the program.
It builds all of the Atoms in the file and provides a list of general atoms and a list of ligands
At the end of the program it takes the results and writes it to a file. Note The DEBUG global variable is initially set to False but can be set to true if You want to see how each line gets parsed.

### Constructor(file)
It is the responsibility of this function to read all of the lines in the input file, send the line to the parser function, and then builds the atom with the parsed info by sending it to the buildAtom Function. 
It checks to see whether the atom should be appended to the Ligand list or the Atoms list. 
In the end, it returns the list of Atoms and Ligands.

### parser(line)
This function strips the line of all of the whitespace and splits the string into the individual components.
It checks to see if it is a Ligand and if it is then appends 0 to the end since they don't have a Radius.
It also checks to see if a Chain ID is present. If one is not given then a None type will be inserted into the correct location.  

### buildAtom(atomInfo)
It takes the information stored in the atom Info list passed in, builds, and returns the atom object.
Please note that all type conversions happen here.

## Estimate.py

### main()
This function starts the whole program.

### init()
Checks to see if all of the parameters have been inputed. It is also responsible for calling the Utility functions to load and construct the atom objects.

### buildLigandStructure(Ligands)
This function returns a set of vertices for a rectangular prism that bounds the ligand structure

### calcVolBox(Vertices)
Uses the vertices that bound the Ligand and calculates the volume of the box.

### MonteCarlo(Ligands, Vertices, rCutOff)
This function is responsible for calling all of the substeps to the monte carlo implementation to estimate the volume of the irregular ligand structure. 

### generateRandomPoints(Vertices)
This function generates random points bounded by the bounding box that encapsulates the Ligand structure.

### checkHits(Ligands, randPnts, rCutOff)
This function counts how many of the points randomly generated are within some rCutOff of any of the ligand points. If they are then that random point is considered to be a hit. 

### getDistanceFromLigand(Ligand, p)
Using the distance formula it calculates the distance between a ligand and a randomly generated point.

## Structure
The following graphs show what the structure looks like. The first graph shows the raw ligands
![Figure_1](C:\Users\Jason\Desktop\Projects\Research\VolumeApprox\Documentation\Ligands.png)

The Second graph shows the ligands encapsulated by the bounding box.
![Figure_2](C:\Users\Jason\Desktop\Projects\Research\VolumeApprox\Documentation\Figure1.png)

## Sample Output
The following is sample output from running the script on the complex.pqr file with varied rCutOffs and amount of randomly generated points.

#### Output with generating 1000 random points
with an rCutOff of 5.
![Output-1a](C:\Users\Jason\Desktop\Projects\Research\VolumeApprox\Documentation\rCutOff-5.png)

with an rCutOff of 15.
![Output-2a](C:\Users\Jason\Desktop\Projects\Research\VolumeApprox\Documentation\rCutOff-15.png)

#### Output with generating 10000 random points
with an rCutOff of 5
![Output-1b](C:\Users\Jason\Desktop\Projects\Research\VolumeApprox\Documentation\rCutOff-5b.png)

with an rCutOff of 15
![Output-2b](C:\Users\Jason\Desktop\Projects\Research\VolumeApprox\Documentation\rCutOff-15b.png)