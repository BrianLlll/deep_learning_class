# coding: utf-8
def main():
    n=0
    sam_name=[]
    sa_dru={}
    all_drug=[]
    outfile=open('/Users/libingrui/Desktop/Work_file/Results/all_6cla_drug.txt','w')
    with open('/Users/libingrui/Desktop/Work_file/LINCS_3CellineiPwScores_landmark_6cla.txt','r') as infile:
        for lines in infile:
            if n==0:
               lines=lines.strip().split('\t')
               for i in lines[1:]:
                   sam_name.append(i)
            break
    #print(sam_name)
    t=0
    with open('/Users/libingrui/Desktop/Work_file/GSE70138_Broad_LINCS_inst_info.txt','r') as drugfile:
        for lines in drugfile:
            if t>0:
               lines=lines.strip().split('\t')
               sa_dru[lines[0]]=lines[7]
            t+=1
    #print(sa_dru)
    for m in sam_name:
        all_drug.append(sa_dru[m])
    for t in all_drug:
        outfile.write(t+'\n')

main()
            
        