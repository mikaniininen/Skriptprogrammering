
import FileMethods


def main():
    csv_file = 'studenter_labb2_v25_Ny.csv'
    json_file = 'student_lista.json'
    while True:
        print('******Labb 2 meny******')
        print('1. Läs in cvs-fil till json-fil')
        print('2. Lägg till person')
        print('3. Ta bort person')
        print('4. Visa all data som finns i .json-filen')
        print('5. Spara json filen till .csv filen')
        print('6. Avsluta programmet')
        print('***********************')
        user_choice = int(input())

        match user_choice:
            case 1:
                FileMethods.originalfile(csv_file, json_file)
            case 2:
                FileMethods.add_student(json_file)
            case 3:
                FileMethods.delete_student(json_file)
            case 4:
                FileMethods.print_json(json_file)
            case _:
                print('Ogiltigt val')






main()

