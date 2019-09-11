def main():
    name_list=[]
    sa_dru={}
    t=0
    outfile=open('/Users/libingrui/Desktop/Work_file/Results/top100_7path_sam_brd.txt','w')
    with open ('/Users/libingrui/Desktop/Work_file/Results/sele_sam_high_sim_top100.txt') as namefile:
        for lines in namefile:
            lines=lines.strip()
            name_list.append(lines)
    with open('/Users/libingrui/Desktop/Work_file/Data/GSE70138_Broad_LINCS_inst_info.txt','r') as drugfile:
        for lines in drugfile:
            if t>0:
               lines=lines.strip().split('\t')
               sa_dru[lines[0]]=lines[7]
            t+=1
    for i in name_list:
        outfile.write(i+'\t'+sa_dru[i]+'\n')

main()