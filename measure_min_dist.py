from chimera import selection
from chimera import runCommand as rc
from collections import OrderedDict
import csv

sel1 = selection.OSLSelection('#0')
sel2 = selection.OSLSelection('#1')
protein_residues_length = len(sel1.residues()) # Get the number of residues in protein
drug_residues_length = len(sel2.residues()) # Get the number of drugs loaded in 

def min_distance(spec1, spec2):
    s1 = selection.OSLSelection(spec1) # Select the protein 
    s2 = selection.OSLSelection(spec2) # Select the drug
    
    dist = []
    for a1 in s1.atoms():
        for a2 in s2.atoms():
            d = a1.xformCoord().distance(a2.xformCoord()) # Get the distance from atom 1 in protein to atom 2 in drug
            dist.append((d, a1, a2))
    dmin, a1, a2 = min(dist)
    return dmin, a1, a2

for j in range(1, drug_residues_length + 1): 
    for i in range(1, protein_residues_length + 1):
        d, a1, a2 = min_distance('#0:'+ str(i), '#1.' + str(j))
        print('Minimum distance: ' + str(d)  + ' between ' + str(a1.oslIdent()) + ' and ' +  str(a2.oslIdent()))