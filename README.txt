PYTHON SCRIPTS
==================

measure_c1_dist.py
___________________

This script measures the distance between the alpha carbon on every residue of the protein and C1 on every ligand viewed on ViewDock. Inside the csv file, the first column shows the drug name on ViewDock and the top row corresponds to the residue number and the type of residue.

Instructions:
1. Open protein chain
2. View ligands through ViewDock
3. Open IDLE window under Tools>General Controls>IDLE
4. Open python script 'measure_c1_dist.py'
5. The IDLE menu will prompt you to save file name as
6. The output file will be named 'yourfilename.csv' in the same directory as this python script

Change log:
(4/2/2019): The script is now able to get the drug name and residue types

measure_min_dist.py
____________________

This script determines the shortest distance between the closest atom on each residue and the closest atom on the drug for each drug. 

Example: Minimum distance: 23.6298027499 between #0:124.A@N and #1.23:1@H263 

Selection notation: #(model number):(residue number)@(atom type) 

Instructions:
1. Open protein chain
2. View ligands through ViewDock
3. Open IDLE window under Tools>General Controls>IDLE
4. Open python script 'measure_min_dist.py
5. On the IDLE Window, it will output the minimum distance between the closest atom on the two structures.

measure_min_dist_0.1.py
_________________________

Same as measure_min_dist.py, but now writes the data into a csv file.

Drug Name = drug name
Residue = residue/amino acid on the protein
Residue Atom = Atom that is closest to the drug on the residue/amino acid
Drug Atom = Atom on the drug that is closest to the residue/amino acid
Distance = distance in Angstroms

prep_ligand_ff99SB_charge0.py
______________________________

This script prepares ligands by adding hydrogens and adding charges with the options:
Standard residues: AMBER ff99SB
Other residues: Gasteiger
Net Charge: +0
Charge Method: Gasteiger

Instructions:
1. Place the script in the same folder as the all the .sdf files you would like to prep
2. Open Chimera and open the script
3. In the same folder the prepped ligand .mol2 file will appear
4. The script will also output a .mol2 file with all the drugs