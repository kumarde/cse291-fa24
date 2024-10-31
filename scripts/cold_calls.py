import sys
import csv
import random

def read_coldcall_list(f):
    eligible = []
    with open(f, 'r') as infile:
        reader = csv.reader(infile)
        next(reader)
        for row in reader: 
            if row[2] == "2":
                eligible.append(row[1])
    return eligible

def main():
    coldcall_list = sys.argv[1]
    eligible = read_coldcall_list(coldcall_list)
    random.shuffle(eligible)
    print(eligible[0])

if __name__ == "__main__":
    main()
