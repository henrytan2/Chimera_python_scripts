import chimera
from chimera import selection
from chimera import runCommand as rc
from collections import OrderedDict
import csv

sel1 = selection.OSLSelection('#0')
sel2 = selection.OSLSelection('#1')
protein_residues_length = len(sel1.residues()) # Get the number of residues in protein
drug_residues_length = len(sel2.residues()) # Get the number of drugs loaded in 
models = chimera.openModels.list()

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
distance_dict = OrderedDict()
drug_name = []
residue_number = []
distances = []
residue_atoms = []
drug_atoms = []
for j in range(1, drug_residues_length + 1): 
    for i in range(1, protein_residues_length + 1):
        name = models[j].name
        name = name[:-4]
        drug_name.append(name)
        sel3 = selection.OSLSelection('#0:' + str(i))
        res = str(sel3.residues()[0])
        res_number = res[3:-2] #string manipulation to remove the numebrs and match ex(Tyr23)
        res_number = res_number[0] + res_number[1:3].lower() + res_number[4:]
        residue_number.append(res_number)
        d, a1, a2 = min_distance('#0:'+ str(i), '#1.' + str(j))
        distances.append(d)
        res_atom = str(a1.name)
        drug_atom = str(a2.name)
        residue_atoms.append(res_atom)
        drug_atoms.append(drug_atom)
        #print('Minimum distance: ' + str(d)  + ' between ' + str(a1.oslIdent()) + ' and ' +  str(a2.oslIdent()))

distance_dict['Drug Name'] = drug_name
distance_dict['Residue'] = residue_number
distance_dict['Residue Atom'] = residue_atoms
distance_dict['Drug Atom'] = drug_atoms
distance_dict['Distance'] = distances

print('Save as filename...')
filename = raw_input()

with open(filename + '.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(distance_dict.keys())
	writer.writerows(zip(*distance_dict.values()))
