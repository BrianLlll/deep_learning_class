un_list=[]
all_data_label=[]
outfile=open(r'/Users/libingrui/Desktop/combin_input_label.txt','w')
with open(r'/Users/libingrui/Desktop/cell_type_uniq.txt','r') as data_un_file:
    for un_line in data_un_file:
        un_list.append(un_line.strip())
with open(r'/Users/libingrui/Desktop/combine_all_data_title.txt') as data_all_title_file:
    for data_all_title_lines in data_all_title_file:
        data_all_title_lines=data_all_title_lines.strip()
        data_list=[2 for i in range(15)]
        data_list[un_list.index(data_all_title_lines)]=1
        all_data_label.append(data_list)
for each in all_data_label:
    for unit in each:
        outfile.write(str(unit)+'\t')
    outfile.write('\n')
# gene_list=[]
# outfile=open(r'/Users/libingrui/Desktop/hpca_sele_gene_expr.txt','w')
# with open(r'/Users/libingrui/Desktop/blue_sele_gene.txt','r') as gene_file:
#     for gene_lines in gene_file:
#         gene_lines=gene_lines.strip()
#         gene_list.append(gene_lines)
# n=0
# with open(r'/Users/libingrui/Desktop/hpca_data_expr_sele.txt','r') as data_file:
#     for lines in data_file:
#         lines=lines.strip().split('\t')
#         n+=1
#         if n==1:
#             lines='\t'.join(lines)
#             outfile.write(lines+'\n')
#         else:
#             if lines[0] in gene_list:
#                 lines='\t'.join(lines)
#                 outfile.write(lines+'\n')

            









