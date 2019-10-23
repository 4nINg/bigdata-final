import csv
with open('Intake_Hint_Data.csv','r') as Intake_Hint:
    intake = Intake_Hint.readlines()[1:]
    Intake_Hint_List= csv.reader(intake)

    for intake_hint_data in Intake_Hint_List:
        print(intake_hint_data[0])
        hint = list(intake_hint_data[1].split('\n'))
        print(hint)
