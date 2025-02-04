import csv
import json

csv_file = 'studenter_labb2_v25_Ny.csv'
json_file = 'student_lista.json'

def originalfile(csv_file, json_file):

    #list_of_students = []
    columns = []
    rows = []
    dict_students = {}
    with open(csv_file, 'r', encoding = 'utf-8-sig') as csvfile:
        reader_object = csv.reader(csvfile, delimiter = ';')
        columns = next(reader_object)

        for row in reader_object:
            rows.append(row)


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







