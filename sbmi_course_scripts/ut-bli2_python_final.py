import xml.etree.ElementTree as ET
import numpy as np
in_file_tree=ET.parse('xml_final_2.xml')
in_root=in_file_tree.getroot()
all_data_list=[]
for data_set in in_root.iter('dataset'):
    each_list=[]
    each_list.append(data_set.find('.//DataID').text)
    each_list.append(data_set.find('.//BP_Before').text)
    each_list.append(data_set.find('.//BP_After').text)
    all_data_list.append(each_list)
all_array=np.array(all_data_list)
print('DataID ','Difference(BP_After minor BP_Before)')
for each in all_array:
    print(each[0],int(each[2])-int(each[1]))