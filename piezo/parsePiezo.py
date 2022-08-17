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
        vmax = i['v_max']
        eij = i['eij_max']

        # extract the piezoelectric tensor list
        tensors = i['piezoelectric_tensor']
        tensorList = parseTensors(tensors)
        meta = i['meta']
        mID = meta['material_id']
        nsites = meta['nsites']
        volume = meta['volume']
        formula = meta['formula']
        pointGroup = meta['point_group']
        spaceGroup = meta['space_group']
        struct = meta['structure']
        [a, b, c, alpha, beta, gamma] = parseStructure(struct)

        row.append([mID, formula, vmax[0], vmax[1], vmax[2], nsites,
                    pointGroup, spaceGroup, volume, a, b, c, alpha, beta, gamma, eij] + tensorList)

    outputfile = open('piezo.csv', 'w')
    outputfile.write('mID,formula,vm1,vm2,vm3,sites,pointGroup,spaceGroup,volume,a,b,c,alpha,beta,gamma,eij,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18\n')
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

def parseTensors(tensors):
    ttt = list()
    for a in tensors:
        for b in a:
            ttt.append(b)

    return ttt
main()


