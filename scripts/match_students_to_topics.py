import sys
import csv

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

TOPIC_TO_RESOURCES = {
        '3' : 4,
    '4' : 4,
    '5' : 4,
    '6' : 4,
    '7' : 4,
    '8' : 4,
    '9' : 2,
    '10' : 2
}


def main():
    classlist_f = sys.argv[1]
    topiclist_f = sys.argv[2]

    class_students = set()
    topiclist_students = set()

    with open(classlist_f, 'r') as infile:
        reader = csv.reader(infile, dialect='excel', delimiter='\t')
        next(reader)
        for row in reader:
            class_students.add(row[CL_EMAIL])

    with open(topiclist_f, 'r') as infile:
        reader = csv.reader(infile)
        next(reader)
        for row in reader:
            topiclist_students.add(row[T_EMAIL])

    print(class_students, len(class_students))
    print(topiclist_students, len(topiclist_students))


if __name__ == "__main__":
    main()
