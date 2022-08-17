import json

def main():
# Open json file
    f = open('piezo.json')
    # data is a list of dictionaries
    data = json.load(f)

    # list to store piezoelectric constant
    row = list()

    # list to store meta data
    meta = list()

    for i in data:
        meta = i['meta']
        poscar = meta['poscar']
        [ag1_I1, ag_I] = parsePoscar(poscar)

    row.append([ag1_I1, ag_I])
    
    outputfile = open('poscar.csv', 'w')
    outputfile.write('ag1_I1,ag_I\n')
    for k in row:
        s = ','.join(str(x) for x in k)
        outputfile.write(s + "\n")

def parsePoscar(poscar):
    for line in poscar.splitlines():
        tokens = line.split('   ')
        if tokens[0] == 'Ag1 T1':
            ag1_I1 = tokens[1]
        if tokens[0] == 'Ag T':
            ag_I = tokens[1]

    return ag1_I1, ag_I
main()


