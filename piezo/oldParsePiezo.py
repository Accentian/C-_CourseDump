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
        eij = i['eij_max']
        meta = i['meta']
        mID = meta['material_id']
        nsites = meta['nsites']
        volume = meta['volume']
        formula = meta['formula']
        pointGroup = meta['point_group']
        spaceGroup = meta['space_group']
        struct = meta['structure']
        [a, b, c, alpha, beta, gamma] = parseStructure(struct)

        row.append([mID, nsites, formula, pointGroup, spaceGroup, volume,
                    a, b, c, alpha, beta, gamma, eij])

    outputfile = open('newPiezo.csv', 'w')
    outputfile.write('mID,nsites,formula,pointGroup,spaceGroup,volume,a,b,c,alpha,beta,gamma,eij\n')
    for k in row:
        s = ','.join(str(x) for x in k)
        outputfile.write(s + "\n")

def parseStructure(struct):

    for line in struct.splitlines():
        tokens = line.split('   ')
        if tokens[0] == '_cell_length_a':
            a = tokens[1]
        if tokens[0] == '_cell_length_b':
            b = tokens[1]
        if tokens[0] == '_cell_length_c':
            c = tokens[1]
        if tokens[0] == '_cell_angle_alpha':
            alpha = tokens[1]
        if tokens[0] == '_cell_angle_beta':
            beta = tokens[1]
        if tokens[0] == '_cell_angle_gamma':
            gamma = tokens[1]

    return a, b, c, alpha, beta, gamma
main()


