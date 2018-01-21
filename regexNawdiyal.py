# Import regular expressions
import re
from rdkit import Chem


inputfile = """C
AR 
A1 
A1- 
A1C2H 
A1C2H-M
A1CH2 
A1CH2OH 
A1CH3 
A1CHO 
A1CO 
C-2-C4H8 
CYC6H4 
CH2CH2COCH3
C2H 
C2H2 
C2H3 
C2H4 
C2H4O1-2
C2H4O2H
C2H5 
C2H5CHO
C2H5CO
C2H5COCH2
C2H5O 
C2H5OH 
C2H5O2
C2H5O2H
C2H6 
C2O 
C3H2 
C3H3 
C3H4 
C3H4P 
C3H5 
C3H6 
C3H6CHO-1
C3H6COCH3-1
C3H8 
C4H 
C4H10 
C4H2 
C4H4 
C4H6 
C4H612 
C4H8-1 
C4H8-2 
C4H9-1 
C4H9-2 
C5H2 
C5H3 
OCYC5H4 
OHCYC5H4- 
CYC5H5- 
OCYC5H5 
CYC5H6
I-A-C5H10
I-A-C5H9P
I-A-C5H9S
I-A-C5H8
C6H 
C6H10 
C6H2 
C6H3 
C6H4-1 
OA1 
OHA1 
C6H6-1 
C6H8 
C6H9-1 
C6H9-2 
CH 
CH2-1 
CH2-3 
CH2CH2OH
CH2CH2CHO 
CH2CHO 
CH2CO 
CH2O 
CH2OH 
CH3 
CH3CHO 
CH3CHCO
CH3CHOH 
CH3CO 
CH3O 
CH3O2 
CH3O2H 
CH3OH 
CH4 
CO 
CO2 
H 
H2 
H2C4O 
H2O 
H2O2 
HCCO 
HCO 
HO2 
HO2CHO
HOCHO
HOCH2O
OHA1CH3-O 
I-C3H7 
N-C3H7CO
N-C3H7CHO
I-C4H3 
I-C4H5 
I-C4H9 
I-C4H10 
I-C6H5 
I-C6H7 
N-C3H7 
N-C3H7O
N-C3H7O2
N-C3H7O2H
N-C4H3 
N-C4H5 
N-C6H7 
O 
O2 
O2CHO
OCHO
OA1CH3-O 
OH 
TOLA2 
N-C6H5 
C-C6H7 
A1C2H2-R1 
A1C2H2-R2 
A1C2H-O 
N2 
C3H5O 
C2H3CHO 
T-C4H9 
CH3CO3 
CH3CO3H
I-C3H7O 
I-C3H7O2 
I-C3H7O2H 
I-C4H9O2 
I-C4H9O2H 
T-C4H9O2 
T-C4H9O2H 
I-C4H8 
I-C4H9O 
I-C3H7CHO 
I-C4H7 
C2H3CO 
CH3CO2 
T-C4H9O 
I-C4H7O 
I-C4H8O2H-I 
I-C4H8O2H-T 
CC4H8O 
I-C4H8O 
C3H5-T 
I-C4H7OH 
I-C3H5CHO 
CH3COCH2 
I-C4H6OH 
I-C4H7CO 
CH3COCH3 
I-C3H5CO 
T-C3H6OH 
T-C4H8O2H-I 
I-C4H8OH 
IO2C4H8OH 
!Soot
A1C2HAC
A2
A2-X
A2R5
A2R5-
A2R5C2H
A3R5
A3R5-
ANC2HAC
A2R5C2H-
A1CH3-M
OA1CH3-M
OHA1CH3-M
A1M1OH3-
C5H11-1
C4H7P-1
C4H7S-1 
FC6H6 !Fulvene 
!---------------------------------------------------------!
!cylohexane Species
!---------------------------------------------------------!
CYC6H11       
CYC6H10       
CYC6H9
CYC6H8
CYC6H7
CYC6H12       
!---------------------------------------------------------!
!1-hexene species
!---------------------------------------------------------!
C4H5O-D1K4R4
C4H5O-D1K3R4
C4H6O-D1K3
C4H6O-D1K4
C5H7-D1D4R3
C5H7O-D1K3R5
C5H7O-D1K5R5
C5H7O-D1K4R5
C5H8-D1D3       
C5H8-D1D4
C5H8O-D1K5
C5H9-D1R3
C5H9-D1R4
C5H9-D1R5
C5H10-1  
C5H10-2       
C5H11-2 
C5H11-3 
C6H9-D1D3R6
C6H9-D1D3R5
C6H9-D1D5R3
C6H10-D1D3
C6H10-D1D4
C6H10O-D1E45
C6H10O-D1E35
C6H10O-D1E34
C6H10O-D1E36
C6H10O-D1E46
C6H10O-D1E56
C6H10O3-D1K3HP4
C6H10O3-D1K3HP5
C6H10O3-D1K3HP6
C6H10O3-D1K4HP3
C6H10O3-D1K4HP5
C6H10O3-D1K4HP6
C6H10O3-D1K5HP3
C6H10O3-D1K5HP4 
C6H10O3-D1K5HP6 
C6H10O3-D1K6HP3
C6H10O3-D1K6HP4
C6H10O3-D1K6HP5
C6H11-D1R3
C6H11-D1R4
C6H11-D1R5
C6H11-D1R6
C6H11O-D1O3
C6H11O-D1O4
C6H11O-D1O5
C6H11O-D1O6
C6H11O2-D1P3
C6H11O2-D1P4
C6H11O2-D1P5
C6H11O2-D1P6
C6H11O2-D1HP3R4
C6H11O2-D1HP3R5
C6H11O2-D1HP3R6
C6H11O2-D1HP4R3
C6H11O2-D1HP4R5
C6H11O2-D1HP4R6
C6H11O2-D1HP5R3 
C6H11O2-D1HP5R4
C6H11O2-D1HP5R6 
C6H11O2-D1HP6R3
C6H11O2-D1HP6R4
C6H11O2-D1HP6R5
C6H11O2H-D1HP3
C6H11O2H-D1HP4  
C6H11O2H-D1HP5
C6H11O2H-D1HP6
C6H11O4-D1HP3P4 
C6H11O4-D1HP3P5
C6H11O4-D1HP3P6
C6H11O4-D1HP4P3
C6H11O4-D1HP4P5
C6H11O4-D1HP4P6
C6H11O4-D1HP5P3
C6H11O4-D1HP5P4
C6H11O4-D1HP5P6
C6H11O4-D1HP6P3
C6H11O4-D1HP6P4
C6H11O4-D1HP6P5
C6H12-d1     
"""


# split my input file into a list and get rid of unwanted entries
inputfile.split()
names = inputfile.split()
names = [x for x in names if "!" not in x]  # gets rid of entries containing an !
names = [x for x in names if "pecies" not in x]  # gets rid of entries containing the word species
# Names is my list full of names

# Now I want to create a dictionary so I can use strings instead of lists
names = dict(zip(names, names))
# x is my string that iterates through the dictionary

raw_smiles = {}
for i, name in names.iteritems():
    s = name
    s = re.sub('A1-', '[C]1CCCCC1', s)
    s = re.sub('A1', 'C1CCCCC1', s)
    s = re.sub('AR', 'Ar', s)
    s = re.sub('CH3', '[CH3]', s)
    s = re.sub('C2H ', '[C]#C', s)
    s = re.sub('CH2', '[CH2]', s)
    s = re.sub('CO2', 'O=C=O', s)
    s = re.sub('OH', 'O', s)
    s = re.sub('O1 ', 'O', s)
    s = re.sub('O2H', 'OO', s)
    s = re.sub('O2 ', '[O][O]', s)
    s = re.sub('O2', 'O[O]', s)
    s = re.sub('CHO ', 'C=O', s)
    s = re.sub('CO', 'O=[C]', s)
    s = re.sub('CH2', '[CH2]', s)
    s = re.sub('COCH2', '(=O)CC', s)
    s = re.sub('COCH3 ', 'CC(C)=O', s)
    s = re.sub('C2H2', 'C#C', s)
    s = re.sub('C2H3', '[CH]=C', s)
    s = re.sub('C2H4', 'C=C', s)
    s = re.sub('C2H5', 'C[CH2]', s)
    s = re.sub('A2', 'C1CCC2CCCCC2C1', s)
    s = re.sub('CHOH', '[CH]O', s)
    s = re.sub('HO2', '[O]O', s)
    s = re.sub('-C4H10', 'CC(C)C', s)

    # for saturated hydrocarbons
    if r'C':
        for i in range(1,10):
            j = str(2*i+2)
            k = str(i)
            if r'C' + re.escape(k) + r'H' + re.escape(j):
                s = re.sub(r'C' + re.escape(k) + r'H' + re.escape(j), 'C' * i, s)
            else:
                continue

    #

    raw_smiles[name] = s  # building my dictionary

smiless = {}
for name, smiles in raw_smiles.iteritems():
    try:
        molecule = Chem.MolFromSmiles(smiles)  # turn it into an rdkit molecule
        smiles = Chem.MolToSmiles(molecule, True)  # turn it back into a (canonical) smiles
    except:
        print "couldn't convert ", name
    smiless[name] = smiles

for name in sorted(smiless.keys()):
    smiles = smiless[name]
    print "{}\t{}\t! Autoconfirm".format(name, smiles)