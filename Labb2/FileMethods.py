import csv
import json

csv_file = 'studenter_labb2_v25_Ny.csv'
json_file = 'student_lista.json'

def originalfile(csv_file, json_file):

    #list_of_students = []
 #   columns = []
 #   rows = []
    dict_students = {}
#    with open(csv_file, 'r', encoding = 'utf-8-sig') as csvfile:
#        reader_object = csv.reader(csvfile, delimiter = ';')
#        columns = next(reader_object)
#
#        for row in reader_object:
#            rows.append(row)


    with open(csv_file, encoding = 'utf-8-sig') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for rows in csv_reader:
            key = rows['efternamn']
            dict_students[key] = rows


    with open(json_file, 'w', encoding= 'utf-8-sig') as jsonf:
        jsonf.write(json.dumps(dict_students, indent = 4, ensure_ascii = False))


def add_student(json_file):
    lastname = input('Ange efternamn: ')
    firstname = input('Ange förnamn: ')
    username = input('Ange användarnamn: ')

    student_dict = {'Efternamn': lastname,'Förnamn': firstname,'Användarnamn': username}
    with open(json_file, 'r', encoding = 'utf-8-sig') as file:
        dict_with_json_data = json.load(file)
        dict_with_json_data[lastname] = student_dict
        file.seek(0)

    with open(json_file, 'w', encoding = 'utf-8-sig') as wfile:
            json.dump(dict_with_json_data, wfile, indent = 4, ensure_ascii = False)

def delete_student(json_file):
    lastname = input('Ange efternamn för personen som ska tas bort')
    new_dict ={}
    with open(json_file, 'r', encoding='utf-8-sig') as jsonf:
        dict_from_jsonf = json.load(jsonf)
        del dict_from_jsonf[lastname]

        for key,value in dict_from_jsonf.items():
            new_dict[key] = value

    with open(json_file, 'w', encoding='utf-8-sig') as wfil:
        json.dump(new_dict,wfil,indent=4, ensure_ascii=False)

def print_json(json_file):
    stream_data = open(json_file, 'r', encoding = 'utf-8-sig')
    load_data_from_stream = json.load(stream_data)
    output = json.dumps(load_data_from_stream, indent = 4, ensure_ascii=False)
    stream_data.close()
    print(output)

def save_json_to_csv(csv_file, json_file):
    header_list = []
    rad_list = []
    with open(json_file, 'r', encoding = 'utf-8-sig') as jsonf:
        json_data = json.load(jsonf)
        for v_json in json_data.values():
            for k in v_json.keys():
                if k not in header_list:
                    header_list.append(k)
            rad_list.append(v_json.copy())
    #print(header_list)
    #print(rad_list)

    with open(csv_file, 'w', newline = '', encoding = 'utf-8-sig') as csvfile:
        skrivarObj = csv.DictWriter(csvfile, fieldnames = header_list)
        skrivarObj.writeheader()
        for data in rad_list:
            skrivarObj.writerow(data)
