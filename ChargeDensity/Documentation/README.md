# Documentation
#### Professor Minh's Research Group
#### By Jason Lawrence

## Setup/How to run
In the command line navigate to the directory where CalculateChargeDensity.py is saved and then type the following: CalculateChargeDensity.py [Input File] [charge] [rCutOff]. The output will be the Charge Density.

## CalculateChargeDensity.py
To calculate the charge density it uses the previous scripts being Estimat.py and CoulombsLaw.py to calculate the volume of the ligand structure with an rCut value and filter the charges based on the input parameters. It then finds the net charge and divides by the volume of the structure.

### Output with parameters: Charge = 0.6 and rCut = 8 
![Output](C:\Users\Jason\Desktop\Projects\Research\ChargeDensity\Documentation\output1.png)