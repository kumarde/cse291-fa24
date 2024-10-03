import sys
import csv
from matching.games import StudentAllocation
import random

CL_SEC_ID = 0
CL_PID = 1
CL_NAME = 2
CL_PRONOUNS = 3
CL_CREDITS = 4
CL_COLLEGE = 5
CL_MAJOR = 6
CL_LEVEL = 7
CL_EMAIL = 8

T_NAME = 1
T_EMAIL = 2
T_CONTENT_MODERATION = 3
T_INFORMATION_MANIPULATION = 4
T_HARASSMENT = 5
T_YOUTH = 6
T_IPS = 7
T_DESIGN = 8
T_ETHICS = 9
T_REGULATION = 10
T_OPEN_TO_PRESENTING = 11

INDEX_TO_NAME = {
#    3   :   "Content Moderation",
    4   :   "Information Manipulation",
    5   :   "Harassment",
    6   :   "Youth Safety",
    7   :   "Intimate Partner Surveillance",
    8   :   "Design and Interventions",
    9   :   "Ethics",
    10  :   "Regulation"
}

project_to_capacity = {
#    "Content Moderation" : 4,
    "Information Manipulation" : 4,
    "Harassment" : 4,
    "Youth Safety" : 4,
    "Design and Interventions" : 4,
    "Intimate Partner Surveillance" : 4,
    "Ethics" : 2,
    'Regulation' : 2
}

def main():
    classlist_f = sys.argv[1]
    topiclist_f = sys.argv[2]

    class_students = set()
    topiclist_students = set()
    student_to_would_present = {}

    with open(classlist_f, 'r') as infile:
        reader = csv.reader(infile, dialect='excel', delimiter='\t')
        next(reader)
        for row in reader:
            class_students.add(row[CL_EMAIL])

    students_to_preferences = {}

    with open(topiclist_f, 'r') as infile:
        reader = csv.reader(infile)
        next(reader)
        for row in reader:
            email = row[T_EMAIL]
            topiclist_students.add(email)
            ranks = row[T_CONTENT_MODERATION:T_REGULATION+1]
            preferences = []
            #print(email)
            for i in range(1,8):
                index_of_topic = ranks.index(str(i)) + 3
                if index_of_topic == 3:
                    continue
                preferences.append(INDEX_TO_NAME[index_of_topic])
            students_to_preferences[email] = preferences
            student_to_would_present[email] = row[T_OPEN_TO_PRESENTING]
  
    topiclist_students = list(topiclist_students)

    project_to_supervisor = {}
    for t in project_to_capacity:
        project_to_supervisor[t] = 'Deepak'

    supervisor_to_capacity = {
        'Deepak':   len(topiclist_students)
    }

    random.shuffle(topiclist_students)
    supervisor_to_preferences = {
        'Deepak'    :   topiclist_students 
    }

    #print(supervisor_to_preferences)
    game = StudentAllocation.create_from_dictionaries(
        students_to_preferences,
        supervisor_to_preferences,
        project_to_supervisor,
        project_to_capacity,
        supervisor_to_capacity
    )

    matching = game.solve(optimal="student")
    matching_dict = dict(matching)
    writer = csv.writer(sys.stdout)
    print(student_to_would_present)
    for topic, students in matching_dict.items():
        for s in students:
            writer.writerow([s,topic])
            #print(topic, s, student_to_would_present[str(s)])

if __name__ == "__main__":
    main()
