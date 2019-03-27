# Documentation
#### Professor Minh's Research Group
#### By Jason Lawrence

## Setup/How to run
TODO

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

### outputGeneration(dir, file, results)
This function takes the results obtained from performing the calculations and writes them to the file. The ouput file naming scheme is as followsThe word "Output" is prepended to the file name.
The format for the output is as follows.

#### Columns
|Column 1 |Column 2 |
|:--------|:--------|
|Ligand Number|ratio of atoms within the cut off vs total atoms|

## Estimate.py

### main()
This function starts the whole program.

### init()
Checks to see if all of the parameters have been inputed. It is also responsible for calling the Utility functions to load and construct the atom objects.

### LigandLoop(Atoms, Ligands)
This function loops through all of the ligands and looks for all of the atoms that are within some distance less than the cutoff. It counts them and find the ratio of atoms within the distance to the total amount of atoms. 

### getDistanceFromLigand(atom, ligand)
This function calculates the distance between the atom and the ligand by using the distance formula. it converst the distance to meters before it returns the distance.

### calcIndividualVol(vol, Ratios)
Uses the total volume of the structure and the ratio of points within some rCutOff of a Ligand atom and calculates the volume.

### findVolume(center, combined)
it finds the farthest point from the center and uses that as the radius for calculating the volume of a sphere.

### Structure
The following graphs show what the structure looks like the red dots are the non ligand atoms and the blue triangles are the ligands
![Figure_1](C:\Users\Jason\Desktop\Projects\Research\VolumeApprox\Documentation\Figure_1.png)

![Figure_2](C:\Users\Jason\Desktop\Projects\Research\VolumeApprox\Documentation\Figure_2.png)

### Sample Output
The following is sample output from running the script on the complex.pqr file
![Output](C:\Users\Jason\Desktop\Projects\Research\VolumeApprox\Documentation\Output.png)