import random
def random_process():
    outfile_rand=open(r'/Users/libingrui/Desktop/Work_file/Results/rando_num_6cla_l_p.txt','w')
    with open (r'/Users/libingrui/Desktop/Work_file/Data/LINCS_3CellineiPwScores_landmark_6Cla.txt','r') as mesh_file:
        all_list=[]
        all_data=[]
        for mesh_lines in mesh_file:
            mesh_lines=mesh_lines.strip().split('\t')
            all_list.append(mesh_lines)
#    array_file=np.array(all_list)
    #for i in range(len(all_list)):
        #row_data.append()
    #print((all_list[0][398]))
    for i in range(1,len(all_list[1])):
        #print(len(all_list[1]))
        row_data=[float(x[i]) for x in all_list[1:]]
        #aprint(row_data)
        all_data.append(row_data)
    #print(len(all_data))
    label=[]
    ran_list=[x for x in range(3985)]
    random.shuffle(ran_list)
    for i in ran_list:
        outfile_rand.write(str(i)+'\n')
    
    #print(ran_list)
    rand_alldata=[]
    for i in ran_list:
        #print(all_data[i])
        rand_alldata.append(all_data[i])
    with open(r'/Users/libingrui/Desktop/Work_file/Data/label_6Class.txt','r') as label_file:
        for label_line in label_file:
            label_line=label_line.strip()
            label.append(int(label_line))
    #label=np.array(label)
    outfile1=open(r'/Users/libingrui/Desktop/Work_file/Results/P_random_data_notd_6class_onlyland.txt','w')
    outfile2=open(r'/Users/libingrui/Desktop/Work_file/Results/P_random_label_6class_onlyland.txt','w')
    ran_label=[]
    for i in ran_list:
        ran_label.append(label[i])

    for i in rand_alldata:
        for ti in i:
            outfile1.write(str(ti)+'\t')
        outfile1.write('\n')
    for t in ran_label:
        outfile2.write(str(t)+'\n')

    outfile1.close()
    outfile2.close()
    outfile_rand.close()
    
random_process()   