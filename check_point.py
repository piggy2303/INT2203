import csv


def read_list():
    array = []
    with open("list.txt","r") as text_file:
        line = ""
        item = []
        count = 0

        number_of_line = 4

        for i in text_file:
            line = i.replace("\n","")

            if count == number_of_line:
                count = 0
                array.append(item)
                item = []

            if count < number_of_line:
                item.append(line)
                count = count + 1
    return array

def write_to_file(path_to_text_file):
    with open(path_to_text_file, mode='w') as class_file:
        array = read_list()

        for i in array:
            class_name = i[0][0:1]
            class_group = i[0][1:3]
            mssv = i[0][3:11]
            point = i[3]
            if class_name == CLASS_NAME and class_group == CLASS_GROUP:            
                class_file.writelines(mssv+ " "+ point +"\n")


CLASS_NAME = "7"
CLASS_GROUP = "N1"
write_to_file("class_"+CLASS_NAME+"_"+CLASS_GROUP+".txt")


