def main():
    # index_file=open(r'/Users/libingrui/Desktop/Work_file/Results/index_pre_Can.txt','r')
    # ind_list=[]
    # sele_sam=[]
    sd={}
    sm_dic={}
    # for ind_lines in index_file:
    #     ind_lines=ind_lines.strip()
    #     ind_list.append(ind_lines)
    #print(ind_list)
    sample_file=open(r'/Users/libingrui/Desktop/Work_file/Results/select_sam_name.txt','r')
    sele_sam=[]
    for sam_lines in sample_file:
        sam_lines=sam_lines.strip()
        sele_sam.append(sam_lines)
    #for i in ind_list:
        #print(sam_list[int(i)])
        #sele_sam.append(sam_list[int(i)-1])
    #print(sele_sam)
    s_d_file=open(r'/Users/libingrui/Desktop/Work_file/Data/GSE70138_Broad_LINCS_inst_info.txt','r')
    n=0
    for sdlines in s_d_file:
        n+=1
        sdlines=sdlines.strip().split('\t')
        if n>1:
            sd[sdlines[0]]=sdlines[7]
    #print(len(sd.keys()))
    d_smile_file=open(r'/Users/libingrui/Desktop/Work_file/Data/GSE70138_Broad_LINCS_pert_info.txt','r')
    for sm_line in d_smile_file:
        sm_line=sm_line.strip().split('\t')
        sm_dic[sm_line[0]]=sm_line[1]
    #print(len(sm_dic))
    outfile=open(r'/Users/libingrui/Desktop/Work_file/Results/sel_drug_smile.txt','w')
    for n in sele_sam:
        #print(n)
        outfile.write(str(n)+'\t'+str(sd[n])+'\t'+str(sm_dic[sd[n]])+'\n')
    

main()