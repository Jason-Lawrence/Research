# Documentation
#### Professor Minh's Research Group
#### By Jason Lawrence

## Setup/How to run
In CoulombsLaw.py the directory paths will have to be changed to where they are on your system. Make sure all
of the input files are located in the Input directory you set. After the script runs on an input file the 
input file will be moved to the Holding directory. The output of the script will be created, written, and placed in the
Output directory. All input files must be PQR files. Units for charge is C, and Radius/XYZ coordinates are in Angstroms.

To run the program go to the bin directory and in the cmd type CoulombsLaw.py and then press enter. The program will then be initiated.

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
At the end of the program it takes the results and writes it to a file. 

### init(dir, fileName)
This function is responsible for opening the Input File passed to it located in the Input Directory. 
Once it has opened the file it passes the file to the constructor function to build the list of Atoms and Ligands, 
and return them.

### Constructor(file)
It is the responsibility of this function to read all of the lines in the input file, send the line to the parser function, and then builds the atom with the parsed info by sending it to the buildAtom Function. 
It checks to see whether the atom should be appended to the Ligand list or the Atoms list. 
In the end, it retruns the list of Atoms and Ligands.

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
|Column 1 |Column 2 |Column 3   |
|:--------|:--------|:----------|
|Charge of the Atom|Distance between the Atom and the closest Ligand|The force between the Atom and the Ligand|

## CoulombsLaw.py

### main()
This function starts the program. It iterates through the Input Directory and runs the script on all of the input files. It first passes them into the Utility functions by calling Utility.init() to load the file and build all of the Atom and Ligand objects for the script. It then passes in the Atoms and Ligands lists to the atomLoop function.
Once the results are calculated it passes the results into Utility.outputGeneration() function to write the output.
It finally moves the Input file to the Holding Directory

### atomLoop(Atoms, Ligands)
This function loops through all of the atoms and finds the ligand closest to it. Once it finds the ligand it passes the atom, ligand, and the distance between them to the coulombsLaw function to calculate the force. It appends the result to the results list. The results list is a list of 3-tuples formatted as explained above in Utility.outputGeneration.

### coulombsLaw(atom, ligand, dist)
This is used to calculate the force between the atom and the ligand. I use 9 * 10^9 N * m^2/C^2 for Coulombs Constant
I also convert the units for the answer to be in Kcal per mol. 

### getDistance(atom, ligand)
This function calculates the distance between the atom and the ligand by using the distance formula. it converst the distance to meters before it returns the distance.
