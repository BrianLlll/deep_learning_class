def main():
    sam_name_file=open(r'/Users/libingrui/Desktop/Work_file/Results/sele_name.txt','r')
    outfile=open(r'/Users/libingrui/Desktop/Work_file/Results/path_high_sim.txt','w')
    sam_list=[]
    sam_index=[0]
    n=0
    for sam_lines in sam_name_file:
        sam_lines=sam_lines.strip()
        sam_list.append(sam_lines)
    data_file=open(r'/Users/libingrui/Desktop/Work_file/Data/LINCS_3CellineiPwScores_landmark_6Cla.txt')
    for data_lines in data_file:
        n+=1
        data_lines=data_lines.strip().split('\t')
        if n==1:
            for i in sam_list:
                sam_index.append(data_lines.index(i))
            for t in sam_index:
                outfile.write(str(data_lines[t]+'\t'))
            outfile.write('\n')
        elif n>1 and n<166:
            for t in sam_index:
                outfile.write(str(data_lines[t])+'\t')
            outfile.write('\n')
        #break
    sam_name_file.close()
    data_file.close()
    outfile.close()
main()    
