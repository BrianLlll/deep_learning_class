def main():
    smile_list=[]
    name=[]
    name_sm=[]
    na_index=[]
    outfile=open('/Users/libingrui/Desktop/Work_file/Results/sele_name.txt','w')
    with open('/Users/libingrui/Desktop/Work_file/Results/sele_smile_high_sim.txt','r') as smil_file:
        for lines in  smil_file:
            lines=lines.strip()
            smile_list.append(lines)
    with open('/Users/libingrui/Desktop/Work_file/Results/sel_drug_smile.txt','r') as namefile:
        for lines in namefile:
            lines=lines.strip().split('\t')
            name.append(lines[0])
            name_sm.append(lines[2])
    #print(name_sm)
    for i in smile_list:
        for n in range(len(name_sm)):
            if i==name_sm[n]:
                na_index.append(n)
    print(na_index)
    for n in na_index:
        outfile.write(name[n]+'\n')

main()
            