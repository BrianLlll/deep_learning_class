def main():
    index_file=open(r'/Users/libingrui/Desktop/Work_file/Results/index_pre_Can.txt','r')
    ind_list=[]
    sele_sam=[]
    sd={}
    sm_dic={}
    sam_name=[]
    for ind_lines in index_file:
        ind_lines=ind_lines.strip()
        ind_list.append(ind_lines)
    #print(ind_list)
    sample_file=open(r'/Users/libingrui/Desktop/Work_file/Results/rando_num_6cla_l_p.txt','r')
    outfile=open('/Users/libingrui/Desktop/Work_file/Results/select_sam_name.txt','w')
    sam_list=[]
    for sam_lines in sample_file:
        sam_lines=sam_lines.strip()
        sam_list.append(sam_lines)
    for i in ind_list:
        #print(sam_list[int(i)])
        sele_sam.append(sam_list[int(i)-1])
    with open('/Users/libingrui/Desktop/Work_file/Data/LINCS_3CellineiPwScores_landmark_6cla.txt','r') as infile:
        n=0
        for lines in infile:
            if n==0:
               lines=lines.strip().split('\t')
               print(len(lines))
               for i in sele_sam:
                   sam_name.append(lines[int(i)+1])
            break
    for n in sam_name:
        outfile.write(n+'\n')


main()